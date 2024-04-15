import uvicorn
import os
from fastapi import FastAPI, status, HTTPException
from connectdb import engine
from connectdb import sess
from crud import getPrimes
from schema import Primegen, Data
from dotenv import load_dotenv


# Load ENV variables
load_dotenv()


# FastAPI with Meta data
app = FastAPI(
    title="Primegen",
    description="Generate list of prime numbers within a given range.",
    summary="Give a lower and upper bound and choose algorithm type and get back primes within that range.",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Ayush Mali",
        "url": "https://xyz.com",
        "email": "xyz@xyz.com",
    },
    license_info={
        "name": "The GNU General Public License v3.0",
        "url": "https://www.gnu.org/licenses/gpl-3.0.en.html",
    },
)


# Route function
@app.post(
    "/api/getprimes",
    response_model=Primegen,
    summary="Get all Primes using V1 [fast] or V2 [faster] or V3 [fastest] algorithm",
    status_code=status.HTTP_201_CREATED,
)
async def algov1(data: Data):
    """
    Get all primes between the lower and upper bound using V1 or V2 or V3 algorithm:

    - **algo**: V1 or V2 or V3
    - **lowerBound**: required [Numbers greater than 0]
    - **upperBound**: required [Numbers greater than 0]
    """

    if data.algo not in ("V1", "V2", "V3"):
        raise HTTPException(status_code=422, detail="Only V1 or V2 or V3 allowed")

    print("Server Hit!")
    data = await getPrimes(sess, data)
    return data
