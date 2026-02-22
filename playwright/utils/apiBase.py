from playwright.sync_api import Playwright
orderPayLoad = {
    "orders": [
        {
            "country": "Argentina",
            "productOrderedId": "6960eac0c941646b7a8b3e68"
        }
    ]
}

class APIUtils:

    def getToken(self,playwright:Playwright):
        apiRequestContext = playwright.request.new_context(base_url="https://rahulshettyacademy.com")  # base url
        response = apiRequestContext.post(url="/api/ecom/auth/login",
                               data={ "userEmail": "gabito.onj@gmail.com", "userPassword": "Gabito2025"})
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]

    def createOrder(self,playwright:Playwright):
        token = self.getToken(playwright)
        apiRequestContext = playwright.request.new_context(base_url="https://rahulshettyacademy.com")  #base url
        response = apiRequestContext.post("/api/ecom/order/create-order",
                               data=orderPayLoad,
                               headers= {"Authorization": token,
                                         "content-type": "application/json" })
        print(response.json())
        response_body = response.json()
        orderId = response_body["orders"][0]
        return  orderId
