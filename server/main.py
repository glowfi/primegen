from fastapi import Depends, FastAPI, Request, status, HTTPException
from connectdb import engine
from connectdb import sess
from crud import get_primes
from schema import InputData, OutputData
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


# async def common_parameters(
#     req: Request, q: str | None = None, skip: int = 0, limit: int = 100
# ):
#     req.state.user = {"a": 1, "new": True}
#     return {"q": q, "skip": skip, "limit": limit, "body": req.url}


# @app.get("/")
# async def test(req: Request, data: dict = Depends(common_parameters)):
#     print(req.cookies, req.state.user)
#     print("Test Data34")
#     return data


# Route function
@app.post(
    "/api/getprimes",
    response_model=OutputData,
    summary="Get all Primes using V1 [fast] or V2 [faster] or V3 [fastest] algorithm",
    status_code=status.HTTP_201_CREATED,
    tags=["Endpoints"],
)
async def get_all_primes(data: InputData):
    """
    Get all primes between the lower and upper bound using V1 or V2 or V3 algorithm:

    - **algo**: V1 or V2 or V3
    - **lowerBound**: required [Numbers greater than 0]
    - **upperBound**: required [Numbers greater than 0]
    """

    if data.algo not in ("V1", "V2", "V3"):
        raise HTTPException(status_code=422, detail="Only V1 or V2 or V3 allowed")

    print("server hit!")
    data = await get_primes(sess, data)
    return data
