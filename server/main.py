from fastapi import Depends, FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from connectdb import engine
from connectdb import sess
from crud import get_primes
from schema import InputData
from dotenv import load_dotenv
import inspect
import algo


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

# services_url = {
#     "url": {"abc": "https:asda.//asdasd"},
#     "function": {"V1": algo.algo_V1, "V2": algo.algo_V2},
# }

# ls = [("v1", "ref"), ("v2", "ref"), ("v3", "ref")]


# def add_all_functions():
#     register_algo_urls(algo.algo_V1, "V1")
#     register_algo_urls(algo.algo_V2, "V2")


# add_all_functions()


# def register_algo_urls(data, alg_ver):
#     print("Adding Algorithm...")

#     if alg_ver in services_url["url"] or alg_ver in services_url["function"]:
#         raise Exception("ALgo already exists!")

#     if isinstance(data, "str"):
#         services_url["url"][alg_ver] = data
#     elif inspect.isfunction(data):
#         services_url["function"][alg_ver] = data
#     else:
#         raise Exception("Invalid Data format!")


# def execute_algo(alg_ver, lower, upper):
#     if alg_ver in services_url["url"]:
#         # Do a post request using http handler
#         pass
#     elif alg_ver in services_url["function"]:
#         data = services_url["function"][alg_ver](lower, upper)
#     else:
#         raise Exception("Algo does not exists")


# Validation Error
@app.exception_handler(RequestValidationError)
async def custom_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        content=jsonable_encoder({"Errors": exc.errors()}),
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )


# Route function
@app.post(
    "/api/getprimes",
    summary="Get all Primes using V1 [fast] or V2 [faster] or V3 [fastest] algorithm",
    tags=["Endpoints"],
)
async def get_all_primes(data: InputData):
    """
    Get all primes between the lower and upper bound using V1 or V2 or V3 algorithm:

    - **algo**: V1 or V2 or V3
    - **lowerBound**: required [Numbers greater than 0]
    - **upperBound**: required [Numbers greater than 0]
    """

    try:
        data = await get_primes(sess, data)  # type: ignore
        return JSONResponse(
            content=jsonable_encoder({"data": data, "errors": None}),
            status_code=status.HTTP_201_CREATED,
        )

    except Exception as e:
        return JSONResponse(
            content=jsonable_encoder({"data": None, "errors": str(e)}),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
