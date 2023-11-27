from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fpdf import FPDF


class PodDetails(BaseModel):
    pod_number: str
    date_of_delivery: str
    time_of_delivery: str
    delivery_location: str
    delivery_picture: str
    receiver_name: str
    receiver_signature: str


app = FastAPI()

pdf = FPDF()

pdf.set_text_color(0, 0, 0)

templates = Jinja2Templates(directory="templates")


pod = {
    "pod_number": "123456789",
    "customer_name": "Royal Melbourne",
    "date_of_delivery": "01-11-2023",
    "time_of_delivery": "12:00",
    "delivery_location": "Melbourne",
    "delivery_picture": "https://www.google.com",
    "receiver_name": "John Doe",
    "receiver_signature": "https://signaturely.com/wp-content/uploads/2020/04/embellished-letters-signaturely.svg",
}


@app.get("/")
async def hello(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "pod_details": pod}
    )


@app.post("/email-pod")
async def email_pod_pdf(pod_details: PodDetails, request: Request):
    parsed_html = templates.TemplateResponse(
        "index.html", {"request": request, "pod_details": pod_details}
    )
    pdf.add_page()
    pdf.write_html(parsed_html.body.decode("utf-8"))
    pdf.output("output.pdf")
    return {"message": "Email sent successfully"}
