from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from tables import PrimeGen
import time
import algo
from schema import Data


async def get_primes(sessmaker: async_sessionmaker[AsyncSession], data: Data):
    async with sessmaker() as session:
        start = time.time()
        out = []

        if data.algo == "V1":
            out = await algo.algo_V1(data.upperBound, data.lowerBound)
        elif data.algo == "V2":
            out = await algo.algo_V2(data.upperBound, data.lowerBound)
        elif data.algo == "V3":
            out = await algo.algo_V3(data.upperBound, data.lowerBound)

        end = time.time()

        timeElapsed = end - start

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
