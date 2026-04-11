# Interface ExtendedRequest

**Source:** `java.naming\javax\naming\ldap\ExtendedRequest.html`

### Class Description

```java
public interface
ExtendedRequest

extends
Serializable
```

This interface represents an LDAPv3 extended operation request as defined in

RFC 2251

.

```java
ExtendedRequest ::= [APPLICATION 23] SEQUENCE {
requestName [0] LDAPOID,
requestValue [1] OCTET STRING OPTIONAL }
```

It comprises an object identifier string and an optional ASN.1 BER
encoded value.

The methods in this class are used by the service provider to construct
the bits to send to the LDAP server. Applications typically only deal with
the classes that implement this interface, supplying them with
any information required for a particular extended operation request.
It would then pass such a class as an argument to the

LdapContext.extendedOperation()

method for performing the
LDAPv3 extended operation.

For example, suppose the LDAP server supported a 'get time' extended operation.
It would supply GetTimeRequest and GetTimeResponse classes:

```java
public class GetTimeRequest implements ExtendedRequest {
public GetTimeRequest() {... };
public ExtendedResponse createExtendedResponse(String id,
byte[] berValue, int offset, int length)
throws NamingException {
return new GetTimeResponse(id, berValue, offset, length);
}
...
}
public class GetTimeResponse implements ExtendedResponse {
long time;
public GetTimeResponse(String id, byte[] berValue, int offset,
int length) throws NamingException {
time = ... // decode berValue to get time
}
public java.util.Date getDate() { return new java.util.Date(time) };
public long getTime() { return time };
...
}
```

A program would use then these classes as follows:

```java
GetTimeResponse resp =
(GetTimeResponse) ectx.extendedOperation(new GetTimeRequest());
long time = resp.getTime();
```

**All Superinterfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getID()

Retrieves the object identifier of the request.

**Returns:**
- The non-null object identifier string representing the LDAP

ExtendedRequest.requestName

component.

---

#### byte[] getEncodedValue()

Retrieves the ASN.1 BER encoded value of the LDAP extended operation
request. Null is returned if the value is absent.

The result is the raw BER bytes including the tag and length of
the request value. It does not include the request OID.
This method is called by the service provider to get the bits to
put into the extended operation to be sent to the LDAP server.

**Returns:**
- A possibly null byte array representing the ASN.1 BER encoded
contents of the LDAP

ExtendedRequest.requestValue

component.

**Throws:**
- IllegalStateException

- If the encoded value cannot be retrieved
because the request contains insufficient or invalid data/state.

---

#### ExtendedResponse
createExtendedResponse​(
String
id,
byte[] berValue,
int offset,
int length)
throws
NamingException

Creates the response object that corresponds to this request.

After the service provider has sent the extended operation request
to the LDAP server, it will receive a response from the server.
If the operation failed, the provider will throw a NamingException.
If the operation succeeded, the provider will invoke this method
using the data that it got back in the response.
It is the job of this method to return a class that implements
the ExtendedResponse interface that is appropriate for the
extended operation request.

For example, a Start TLS extended request class would need to know
how to process a Start TLS extended response. It does this by creating
a class that implements ExtendedResponse.

**Parameters:**
- id

- The possibly null object identifier of the response
control.
- berValue

- The possibly null ASN.1 BER encoded value of the
response control.
This is the raw BER bytes including the tag and length of
the response value. It does not include the response OID.
- offset

- The starting position in berValue of the bytes to use.
- length

- The number of bytes in berValue to use.

**Returns:**
- A non-null object.

**Throws:**
- NamingException

- if cannot create extended response
due to an error.

**See Also:**
- ExtendedResponse

---

### Additional Sections

#### Interface ExtendedRequest

**All Superinterfaces:** Serializable

**All Known Implementing Classes:** StartTlsRequest

```java
public interface
ExtendedRequest

extends
Serializable
```

This interface represents an LDAPv3 extended operation request as defined in

RFC 2251

.

```java
ExtendedRequest ::= [APPLICATION 23] SEQUENCE {
requestName [0] LDAPOID,
requestValue [1] OCTET STRING OPTIONAL }
```

It comprises an object identifier string and an optional ASN.1 BER
encoded value.

The methods in this class are used by the service provider to construct
the bits to send to the LDAP server. Applications typically only deal with
the classes that implement this interface, supplying them with
any information required for a particular extended operation request.
It would then pass such a class as an argument to the

LdapContext.extendedOperation()

method for performing the
LDAPv3 extended operation.

For example, suppose the LDAP server supported a 'get time' extended operation.
It would supply GetTimeRequest and GetTimeResponse classes:

```java
public class GetTimeRequest implements ExtendedRequest {
public GetTimeRequest() {... };
public ExtendedResponse createExtendedResponse(String id,
byte[] berValue, int offset, int length)
throws NamingException {
return new GetTimeResponse(id, berValue, offset, length);
}
...
}
public class GetTimeResponse implements ExtendedResponse {
long time;
public GetTimeResponse(String id, byte[] berValue, int offset,
int length) throws NamingException {
time = ... // decode berValue to get time
}
public java.util.Date getDate() { return new java.util.Date(time) };
public long getTime() { return time };
...
}
```

A program would use then these classes as follows:

```java
GetTimeResponse resp =
(GetTimeResponse) ectx.extendedOperation(new GetTimeRequest());
long time = resp.getTime();
```

**Since:** 1.3
**See Also:** ExtendedResponse

,

LdapContext.extendedOperation(javax.naming.ldap.ExtendedRequest)

public interface

ExtendedRequest

extends

Serializable

This interface represents an LDAPv3 extended operation request as defined in

RFC 2251

.

```java
ExtendedRequest ::= [APPLICATION 23] SEQUENCE {
requestName [0] LDAPOID,
requestValue [1] OCTET STRING OPTIONAL }
```

It comprises an object identifier string and an optional ASN.1 BER
encoded value.

The methods in this class are used by the service provider to construct
the bits to send to the LDAP server. Applications typically only deal with
the classes that implement this interface, supplying them with
any information required for a particular extended operation request.
It would then pass such a class as an argument to the

LdapContext.extendedOperation()

method for performing the
LDAPv3 extended operation.

For example, suppose the LDAP server supported a 'get time' extended operation.
It would supply GetTimeRequest and GetTimeResponse classes:

```java
public class GetTimeRequest implements ExtendedRequest {
public GetTimeRequest() {... };
public ExtendedResponse createExtendedResponse(String id,
byte[] berValue, int offset, int length)
throws NamingException {
return new GetTimeResponse(id, berValue, offset, length);
}
...
}
public class GetTimeResponse implements ExtendedResponse {
long time;
public GetTimeResponse(String id, byte[] berValue, int offset,
int length) throws NamingException {
time = ... // decode berValue to get time
}
public java.util.Date getDate() { return new java.util.Date(time) };
public long getTime() { return time };
...
}
```

A program would use then these classes as follows:

```java
GetTimeResponse resp =
(GetTimeResponse) ectx.extendedOperation(new GetTimeRequest());
long time = resp.getTime();
```

ExtendedRequest ::= [APPLICATION 23] SEQUENCE {
requestName [0] LDAPOID,
requestValue [1] OCTET STRING OPTIONAL }

The methods in this class are used by the service provider to construct
the bits to send to the LDAP server. Applications typically only deal with
the classes that implement this interface, supplying them with
any information required for a particular extended operation request.
It would then pass such a class as an argument to the

LdapContext.extendedOperation()

method for performing the
LDAPv3 extended operation.

For example, suppose the LDAP server supported a 'get time' extended operation.
It would supply GetTimeRequest and GetTimeResponse classes:

```java
public class GetTimeRequest implements ExtendedRequest {
public GetTimeRequest() {... };
public ExtendedResponse createExtendedResponse(String id,
byte[] berValue, int offset, int length)
throws NamingException {
return new GetTimeResponse(id, berValue, offset, length);
}
...
}
public class GetTimeResponse implements ExtendedResponse {
long time;
public GetTimeResponse(String id, byte[] berValue, int offset,
int length) throws NamingException {
time = ... // decode berValue to get time
}
public java.util.Date getDate() { return new java.util.Date(time) };
public long getTime() { return time };
...
}
```

A program would use then these classes as follows:

```java
GetTimeResponse resp =
(GetTimeResponse) ectx.extendedOperation(new GetTimeRequest());
long time = resp.getTime();
```

For example, suppose the LDAP server supported a 'get time' extended operation.
It would supply GetTimeRequest and GetTimeResponse classes:

```java
public class GetTimeRequest implements ExtendedRequest {
public GetTimeRequest() {... };
public ExtendedResponse createExtendedResponse(String id,
byte[] berValue, int offset, int length)
throws NamingException {
return new GetTimeResponse(id, berValue, offset, length);
}
...
}
public class GetTimeResponse implements ExtendedResponse {
long time;
public GetTimeResponse(String id, byte[] berValue, int offset,
int length) throws NamingException {
time = ... // decode berValue to get time
}
public java.util.Date getDate() { return new java.util.Date(time) };
public long getTime() { return time };
...
}
```

A program would use then these classes as follows:

```java
GetTimeResponse resp =
(GetTimeResponse) ectx.extendedOperation(new GetTimeRequest());
long time = resp.getTime();
```

public class GetTimeRequest implements ExtendedRequest {
public GetTimeRequest() {... };
public ExtendedResponse createExtendedResponse(String id,
byte[] berValue, int offset, int length)
throws NamingException {
return new GetTimeResponse(id, berValue, offset, length);
}
...
}
public class GetTimeResponse implements ExtendedResponse {
long time;
public GetTimeResponse(String id, byte[] berValue, int offset,
int length) throws NamingException {
time = ... // decode berValue to get time
}
public java.util.Date getDate() { return new java.util.Date(time) };
public long getTime() { return time };
...
}

GetTimeResponse resp =
(GetTimeResponse) ectx.extendedOperation(new GetTimeRequest());
long time = resp.getTime();

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ExtendedResponse

createExtendedResponse

​(

String

id,
byte[] berValue,
int offset,
int length)

Creates the response object that corresponds to this request.

byte[]

getEncodedValue

()

Retrieves the ASN.1 BER encoded value of the LDAP extended operation
request.

String

getID

()

Retrieves the object identifier of the request.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ExtendedResponse

createExtendedResponse

​(

String

id,
byte[] berValue,
int offset,
int length)

Creates the response object that corresponds to this request.

byte[]

getEncodedValue

()

Retrieves the ASN.1 BER encoded value of the LDAP extended operation
request.

String

getID

()

Retrieves the object identifier of the request.

---

#### Method Summary

Creates the response object that corresponds to this request.

Retrieves the ASN.1 BER encoded value of the LDAP extended operation
request.

Retrieves the object identifier of the request.

============ METHOD DETAIL ==========

- Method Detail

- getID

```java
String
getID()
```

Retrieves the object identifier of the request.

**Returns:** The non-null object identifier string representing the LDAP

ExtendedRequest.requestName

component.

- getEncodedValue

```java
byte[] getEncodedValue()
```

Retrieves the ASN.1 BER encoded value of the LDAP extended operation
request. Null is returned if the value is absent.

The result is the raw BER bytes including the tag and length of
the request value. It does not include the request OID.
This method is called by the service provider to get the bits to
put into the extended operation to be sent to the LDAP server.

**Returns:** A possibly null byte array representing the ASN.1 BER encoded
contents of the LDAP

ExtendedRequest.requestValue

component.
**Throws:** IllegalStateException

- If the encoded value cannot be retrieved
because the request contains insufficient or invalid data/state.

- createExtendedResponse

```java
ExtendedResponse
createExtendedResponse​(
String
id,
byte[] berValue,
int offset,
int length)
throws
NamingException
```

Creates the response object that corresponds to this request.

After the service provider has sent the extended operation request
to the LDAP server, it will receive a response from the server.
If the operation failed, the provider will throw a NamingException.
If the operation succeeded, the provider will invoke this method
using the data that it got back in the response.
It is the job of this method to return a class that implements
the ExtendedResponse interface that is appropriate for the
extended operation request.

For example, a Start TLS extended request class would need to know
how to process a Start TLS extended response. It does this by creating
a class that implements ExtendedResponse.

**Parameters:** id

- The possibly null object identifier of the response
control.
**Parameters:** berValue

- The possibly null ASN.1 BER encoded value of the
response control.
This is the raw BER bytes including the tag and length of
the response value. It does not include the response OID.
**Parameters:** offset

- The starting position in berValue of the bytes to use.
**Parameters:** length

- The number of bytes in berValue to use.
**Returns:** A non-null object.
**Throws:** NamingException

- if cannot create extended response
due to an error.
**See Also:** ExtendedResponse

Method Detail

- getID

```java
String
getID()
```

Retrieves the object identifier of the request.

**Returns:** The non-null object identifier string representing the LDAP

ExtendedRequest.requestName

component.

- getEncodedValue

```java
byte[] getEncodedValue()
```

Retrieves the ASN.1 BER encoded value of the LDAP extended operation
request. Null is returned if the value is absent.

The result is the raw BER bytes including the tag and length of
the request value. It does not include the request OID.
This method is called by the service provider to get the bits to
put into the extended operation to be sent to the LDAP server.

**Returns:** A possibly null byte array representing the ASN.1 BER encoded
contents of the LDAP

ExtendedRequest.requestValue

component.
**Throws:** IllegalStateException

- If the encoded value cannot be retrieved
because the request contains insufficient or invalid data/state.

- createExtendedResponse

```java
ExtendedResponse
createExtendedResponse​(
String
id,
byte[] berValue,
int offset,
int length)
throws
NamingException
```

Creates the response object that corresponds to this request.

After the service provider has sent the extended operation request
to the LDAP server, it will receive a response from the server.
If the operation failed, the provider will throw a NamingException.
If the operation succeeded, the provider will invoke this method
using the data that it got back in the response.
It is the job of this method to return a class that implements
the ExtendedResponse interface that is appropriate for the
extended operation request.

For example, a Start TLS extended request class would need to know
how to process a Start TLS extended response. It does this by creating
a class that implements ExtendedResponse.

**Parameters:** id

- The possibly null object identifier of the response
control.
**Parameters:** berValue

- The possibly null ASN.1 BER encoded value of the
response control.
This is the raw BER bytes including the tag and length of
the response value. It does not include the response OID.
**Parameters:** offset

- The starting position in berValue of the bytes to use.
**Parameters:** length

- The number of bytes in berValue to use.
**Returns:** A non-null object.
**Throws:** NamingException

- if cannot create extended response
due to an error.
**See Also:** ExtendedResponse

---

#### Method Detail

getID

```java
String
getID()
```

Retrieves the object identifier of the request.

**Returns:** The non-null object identifier string representing the LDAP

ExtendedRequest.requestName

component.

---

#### getID

String

getID()

Retrieves the object identifier of the request.

getEncodedValue

```java
byte[] getEncodedValue()
```

Retrieves the ASN.1 BER encoded value of the LDAP extended operation
request. Null is returned if the value is absent.

The result is the raw BER bytes including the tag and length of
the request value. It does not include the request OID.
This method is called by the service provider to get the bits to
put into the extended operation to be sent to the LDAP server.

**Returns:** A possibly null byte array representing the ASN.1 BER encoded
contents of the LDAP

ExtendedRequest.requestValue

component.
**Throws:** IllegalStateException

- If the encoded value cannot be retrieved
because the request contains insufficient or invalid data/state.

---

#### getEncodedValue

byte[] getEncodedValue()

Retrieves the ASN.1 BER encoded value of the LDAP extended operation
request. Null is returned if the value is absent.

The result is the raw BER bytes including the tag and length of
the request value. It does not include the request OID.
This method is called by the service provider to get the bits to
put into the extended operation to be sent to the LDAP server.

createExtendedResponse

```java
ExtendedResponse
createExtendedResponse​(
String
id,
byte[] berValue,
int offset,
int length)
throws
NamingException
```

Creates the response object that corresponds to this request.

After the service provider has sent the extended operation request
to the LDAP server, it will receive a response from the server.
If the operation failed, the provider will throw a NamingException.
If the operation succeeded, the provider will invoke this method
using the data that it got back in the response.
It is the job of this method to return a class that implements
the ExtendedResponse interface that is appropriate for the
extended operation request.

For example, a Start TLS extended request class would need to know
how to process a Start TLS extended response. It does this by creating
a class that implements ExtendedResponse.

**Parameters:** id

- The possibly null object identifier of the response
control.
**Parameters:** berValue

- The possibly null ASN.1 BER encoded value of the
response control.
This is the raw BER bytes including the tag and length of
the response value. It does not include the response OID.
**Parameters:** offset

- The starting position in berValue of the bytes to use.
**Parameters:** length

- The number of bytes in berValue to use.
**Returns:** A non-null object.
**Throws:** NamingException

- if cannot create extended response
due to an error.
**See Also:** ExtendedResponse

---

#### createExtendedResponse

ExtendedResponse

createExtendedResponse​(

String

id,
byte[] berValue,
int offset,
int length)
throws

NamingException

Creates the response object that corresponds to this request.

After the service provider has sent the extended operation request
to the LDAP server, it will receive a response from the server.
If the operation failed, the provider will throw a NamingException.
If the operation succeeded, the provider will invoke this method
using the data that it got back in the response.
It is the job of this method to return a class that implements
the ExtendedResponse interface that is appropriate for the
extended operation request.

For example, a Start TLS extended request class would need to know
how to process a Start TLS extended response. It does this by creating
a class that implements ExtendedResponse.

After the service provider has sent the extended operation request
to the LDAP server, it will receive a response from the server.
If the operation failed, the provider will throw a NamingException.
If the operation succeeded, the provider will invoke this method
using the data that it got back in the response.
It is the job of this method to return a class that implements
the ExtendedResponse interface that is appropriate for the
extended operation request.

For example, a Start TLS extended request class would need to know
how to process a Start TLS extended response. It does this by creating
a class that implements ExtendedResponse.

For example, a Start TLS extended request class would need to know
how to process a Start TLS extended response. It does this by creating
a class that implements ExtendedResponse.

---

