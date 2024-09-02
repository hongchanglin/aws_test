
### HTTP Status Codes: A Summary

HTTP status codes are standardized codes that indicate the outcome of an HTTP request. They are issued by a server in response to a client's request and are categorized into five classes, each representing a different type of response.

#### **1. Informational Responses (1xx)**

These codes indicate that the request was received and understood, and the client should continue the process.

- **100 Continue:** The initial part of the request was received and has not yet been rejected by the server.
- **101 Switching Protocols:** The server is switching to the protocol requested by the client.

#### **2. Success Responses (2xx)**

These codes indicate that the client's request was successfully received, understood, and accepted.

- **200 OK:** The request has succeeded, and the server has returned the requested resource.
- **201 Created:** The request has been fulfilled, and a new resource has been created as a result.
- **202 Accepted:** The request has been accepted for processing, but the processing is not complete.
- **204 No Content:** The server successfully processed the request, but no content is returned.

#### **3. Redirection Responses (3xx)**

These codes indicate that further action is needed from the client to complete the request.

- **301 Moved Permanently:** The requested resource has been permanently moved to a new URL.
- **302 Found:** The requested resource is temporarily located at a different URL.
- **304 Not Modified:** The resource has not been modified since the last request, so the client can use the cached version.

#### **4. Client Error Responses (4xx)**

These codes indicate that there was a problem with the client's request.

- **400 Bad Request:** The server could not understand the request due to invalid syntax.
- **401 Unauthorized:** The client must authenticate itself to get the requested response.
- **403 Forbidden:** The client does not have permission to access the requested resource.
- **404 Not Found:** The server could not find the requested resource.
- **405 Method Not Allowed:** The request method is not supported for the requested resource.
- **409 Conflict:** The request conflicts with the current state of the server.

#### **5. Server Error Responses (5xx)**

These codes indicate that the server encountered an error while processing the request.

- **500 Internal Server Error:** The server encountered a situation it doesn't know how to handle.
- **501 Not Implemented:** The server does not support the functionality required to fulfill the request.
- **502 Bad Gateway:** The server received an invalid response from an inbound server.
- **503 Service Unavailable:** The server is not ready to handle the request, often due to maintenance or overload.
- **504 Gateway Timeout:** The server did not receive a timely response from an upstream server.

### **Key Points to Remember:**

- **Status Code Classes:** The first digit of the status code categorizes the response (1xx informational, 2xx success, 3xx redirection, 4xx client error, 5xx server error).
- **Common Codes:** Familiarize yourself with the most common codes like 200 (OK), 404 (Not Found), 500 (Internal Server Error), etc.
- **Response Context:** Always consider both the status code and the accompanying message/body to fully understand the server's response.
- **Best Practices:** Return appropriate status codes to accurately represent the outcome of the request and to help clients handle responses correctly.

Understanding and correctly using HTTP status codes is essential for effective web development and API design, ensuring clear communication between the client and server.