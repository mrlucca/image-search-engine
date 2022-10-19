from datetime import datetime

from fastapi import FastAPI, File, UploadFile
from aiofile import async_open

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/register/image")
async def send_image_to_background_process(image: UploadFile = File(...)):
    """
    Nesse parametro você deve mandar uma imagem para ser processada na extração de textos
    """
    tail_file_name = image.filename
    now = datetime.now()
    file_lines = image.file.read()
    print(file_lines)
    file_name = "./temp/" + str(now) + "_" + tail_file_name
    async with async_open(file_name, 'wb+') as afp:
        await afp.write(file_lines)

    return {
        "msg": f"file {file_name} send to process image",
        "success": True
    }


@app.post("/register/images")
async def send_many_images_to_background_process(images: UploadFile = File(...)):
    """"""
    return {
        "message": f"Hello {images.filename}"
    }
