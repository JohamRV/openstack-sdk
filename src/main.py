from fastapi import FastAPI
from .router.glance import ImageRouter
from .router.keystone import AuthenticationRouter
from .router.neutron import NetworkRouter, SecurityGroupRouter, RuleRouter, SubnetRouter
from .router.nova import FlavorRoute, KeyPairRouter, ServerRouter
import dotenv

#dotenv.load_dotenv("./env/.env")
app = FastAPI()

app.include_router(ImageRouter.router)
app.include_router(AuthenticationRouter.router)
#app.include_router(NetworkRouter.router)
#app.include_router(SecurityGroupRouter.router)
#app.include_router(RuleRouter.router)
#app.include_router(SubnetRouter.router)
#app.include_router(NetworkRouter.router)
#app.include_router(FlavorRoute.router)
#app.include_router(KeyPairRouter.router)
#pp.include_router(ServerRouter.router)
@app.get("/")
async def root():
    return {"message": "Hello World"}