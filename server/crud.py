from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from tables import PrimeGen
import time
import algo
from schema import InputData
import requests


async def async_wrapper(lower, upper, _algo):
    out = []
    if _algo == "V1":
        out = algo.algo_V1(lower, upper)
    elif _algo == "V2":
        out = algo.algo_V2(lower, upper)
    elif _algo == "V3":
        out = algo.algo_V3(lower, upper)

    # print(out, lower, upper, _algo)

    return out


async def get_primes(sessmaker: async_sessionmaker[AsyncSession], data: InputData):
    async with sessmaker() as session:
        start = time.time()

        # Choose algo based on the input given
        out = await async_wrapper(data.upperBound, data.lowerBound, data.algo)

        end = time.time()

        timeElapsed = end - start

        try:
            # Insert data into the database
            newPrime = PrimeGen(
                algo=data.algo,
                upperBound=data.upperBound,
                lowerBound=data.lowerBound,
                timeElapsed=timeElapsed,
                result=",".join([str(x) for x in out]),
                primeLength=len(out),
            )
            session.add(newPrime)
            await session.commit()
            return newPrime

        except Exception as e:
            raise Exception(f"Database Insertion Failed {str(e)}")
