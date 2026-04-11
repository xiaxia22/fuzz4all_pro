# Interface ExtendedResponse

**Source:** `java.naming\javax\naming\ldap\ExtendedResponse.html`

### Class Description

```java
public interface
ExtendedResponse

extends
Serializable
```

This interface represents an LDAP extended operation response as defined in

RFC 2251

.

```java
ExtendedResponse ::= [APPLICATION 24] SEQUENCE {
COMPONENTS OF LDAPResult,
responseName [10] LDAPOID OPTIONAL,
response [11] OCTET STRING OPTIONAL }
```

It comprises an optional object identifier and an optional ASN.1 BER
encoded value.

The methods in this class can be used by the application to get low
level information about the extended operation response. However, typically,
the application will be using methods specific to the class that
implements this interface. Such a class should have decoded the BER buffer
in the response and should provide methods that allow the user to
access that data in the response in a type-safe and friendly manner.

For example, suppose the LDAP server supported a 'get time' extended operation.
It would supply GetTimeRequest and GetTimeResponse classes.
The GetTimeResponse class might look like:

```java
public class GetTimeResponse implements ExtendedResponse {
public java.util.Date getDate() {...};
public long getTime() {...};
....
}
```

A program would use then these classes as follows:

```java
GetTimeResponse resp =
(GetTimeResponse) ectx.extendedOperation(new GetTimeRequest());
java.util.Date now = resp.getDate();
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

Retrieves the object identifier of the response.
The LDAP protocol specifies that the response object identifier is optional.
If the server does not send it, the response will contain no ID (i.e. null).

**Returns:**
- A possibly null object identifier string representing the LDAP

ExtendedResponse.responseName

component.

---

#### byte[] getEncodedValue()

Retrieves the ASN.1 BER encoded value of the LDAP extended operation
response. Null is returned if the value is absent from the response
sent by the LDAP server.
The result is the raw BER bytes including the tag and length of
the response value. It does not include the response OID.

**Returns:**
- A possibly null byte array representing the ASN.1 BER encoded
contents of the LDAP

ExtendedResponse.response

component.

---

### Additional Sections

#### Interface ExtendedResponse

**All Superinterfaces:** Serializable

**All Known Subinterfaces:** UnsolicitedNotification

**All Known Implementing Classes:** StartTlsResponse

```java
public interface
ExtendedResponse

extends
Serializable
```

This interface represents an LDAP extended operation response as defined in

RFC 2251

.

```java
ExtendedResponse ::= [APPLICATION 24] SEQUENCE {
COMPONENTS OF LDAPResult,
responseName [10] LDAPOID OPTIONAL,
response [11] OCTET STRING OPTIONAL }
```

It comprises an optional object identifier and an optional ASN.1 BER
encoded value.

The methods in this class can be used by the application to get low
level information about the extended operation response. However, typically,
the application will be using methods specific to the class that
implements this interface. Such a class should have decoded the BER buffer
in the response and should provide methods that allow the user to
access that data in the response in a type-safe and friendly manner.

For example, suppose the LDAP server supported a 'get time' extended operation.
It would supply GetTimeRequest and GetTimeResponse classes.
The GetTimeResponse class might look like:

```java
public class GetTimeResponse implements ExtendedResponse {
public java.util.Date getDate() {...};
public long getTime() {...};
....
}
```

A program would use then these classes as follows:

```java
GetTimeResponse resp =
(GetTimeResponse) ectx.extendedOperation(new GetTimeRequest());
java.util.Date now = resp.getDate();
```

**Since:** 1.3
**See Also:** ExtendedRequest

public interface

ExtendedResponse

extends

Serializable

This interface represents an LDAP extended operation response as defined in

RFC 2251

.

```java
ExtendedResponse ::= [APPLICATION 24] SEQUENCE {
COMPONENTS OF LDAPResult,
responseName [10] LDAPOID OPTIONAL,
response [11] OCTET STRING OPTIONAL }
```

It comprises an optional object identifier and an optional ASN.1 BER
encoded value.

The methods in this class can be used by the application to get low
level information about the extended operation response. However, typically,
the application will be using methods specific to the class that
implements this interface. Such a class should have decoded the BER buffer
in the response and should provide methods that allow the user to
access that data in the response in a type-safe and friendly manner.

For example, suppose the LDAP server supported a 'get time' extended operation.
It would supply GetTimeRequest and GetTimeResponse classes.
The GetTimeResponse class might look like:

```java
public class GetTimeResponse implements ExtendedResponse {
public java.util.Date getDate() {...};
public long getTime() {...};
....
}
```

A program would use then these classes as follows:

```java
GetTimeResponse resp =
(GetTimeResponse) ectx.extendedOperation(new GetTimeRequest());
java.util.Date now = resp.getDate();
```

ExtendedResponse ::= [APPLICATION 24] SEQUENCE {
COMPONENTS OF LDAPResult,
responseName [10] LDAPOID OPTIONAL,
response [11] OCTET STRING OPTIONAL }

The methods in this class can be used by the application to get low
level information about the extended operation response. However, typically,
the application will be using methods specific to the class that
implements this interface. Such a class should have decoded the BER buffer
in the response and should provide methods that allow the user to
access that data in the response in a type-safe and friendly manner.

For example, suppose the LDAP server supported a 'get time' extended operation.
It would supply GetTimeRequest and GetTimeResponse classes.
The GetTimeResponse class might look like:

```java
public class GetTimeResponse implements ExtendedResponse {
public java.util.Date getDate() {...};
public long getTime() {...};
....
}
```

A program would use then these classes as follows:

```java
GetTimeResponse resp =
(GetTimeResponse) ectx.extendedOperation(new GetTimeRequest());
java.util.Date now = resp.getDate();
```

For example, suppose the LDAP server supported a 'get time' extended operation.
It would supply GetTimeRequest and GetTimeResponse classes.
The GetTimeResponse class might look like:

```java
public class GetTimeResponse implements ExtendedResponse {
public java.util.Date getDate() {...};
public long getTime() {...};
....
}
```

A program would use then these classes as follows:

```java
GetTimeResponse resp =
(GetTimeResponse) ectx.extendedOperation(new GetTimeRequest());
java.util.Date now = resp.getDate();
```

public class GetTimeResponse implements ExtendedResponse {
public java.util.Date getDate() {...};
public long getTime() {...};
....
}

GetTimeResponse resp =
(GetTimeResponse) ectx.extendedOperation(new GetTimeRequest());
java.util.Date now = resp.getDate();

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

byte[]

getEncodedValue

()

Retrieves the ASN.1 BER encoded value of the LDAP extended operation
response.

String

getID

()

Retrieves the object identifier of the response.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

byte[]

getEncodedValue

()

Retrieves the ASN.1 BER encoded value of the LDAP extended operation
response.

String

getID

()

Retrieves the object identifier of the response.

---

#### Method Summary

Retrieves the ASN.1 BER encoded value of the LDAP extended operation
response.

Retrieves the object identifier of the response.

============ METHOD DETAIL ==========

- Method Detail

- getID

```java
String
getID()
```

Retrieves the object identifier of the response.
The LDAP protocol specifies that the response object identifier is optional.
If the server does not send it, the response will contain no ID (i.e. null).

**Returns:** A possibly null object identifier string representing the LDAP

ExtendedResponse.responseName

component.

- getEncodedValue

```java
byte[] getEncodedValue()
```

Retrieves the ASN.1 BER encoded value of the LDAP extended operation
response. Null is returned if the value is absent from the response
sent by the LDAP server.
The result is the raw BER bytes including the tag and length of
the response value. It does not include the response OID.

**Returns:** A possibly null byte array representing the ASN.1 BER encoded
contents of the LDAP

ExtendedResponse.response

component.

Method Detail

- getID

```java
String
getID()
```

Retrieves the object identifier of the response.
The LDAP protocol specifies that the response object identifier is optional.
If the server does not send it, the response will contain no ID (i.e. null).

**Returns:** A possibly null object identifier string representing the LDAP

ExtendedResponse.responseName

component.

- getEncodedValue

```java
byte[] getEncodedValue()
```

Retrieves the ASN.1 BER encoded value of the LDAP extended operation
response. Null is returned if the value is absent from the response
sent by the LDAP server.
The result is the raw BER bytes including the tag and length of
the response value. It does not include the response OID.

**Returns:** A possibly null byte array representing the ASN.1 BER encoded
contents of the LDAP

ExtendedResponse.response

component.

---

#### Method Detail

getID

```java
String
getID()
```

Retrieves the object identifier of the response.
The LDAP protocol specifies that the response object identifier is optional.
If the server does not send it, the response will contain no ID (i.e. null).

**Returns:** A possibly null object identifier string representing the LDAP

ExtendedResponse.responseName

component.

---

#### getID

String

getID()

Retrieves the object identifier of the response.
The LDAP protocol specifies that the response object identifier is optional.
If the server does not send it, the response will contain no ID (i.e. null).

getEncodedValue

```java
byte[] getEncodedValue()
```

Retrieves the ASN.1 BER encoded value of the LDAP extended operation
response. Null is returned if the value is absent from the response
sent by the LDAP server.
The result is the raw BER bytes including the tag and length of
the response value. It does not include the response OID.

**Returns:** A possibly null byte array representing the ASN.1 BER encoded
contents of the LDAP

ExtendedResponse.response

component.

---

#### getEncodedValue

byte[] getEncodedValue()

Retrieves the ASN.1 BER encoded value of the LDAP extended operation
response. Null is returned if the value is absent from the response
sent by the LDAP server.
The result is the raw BER bytes including the tag and length of
the response value. It does not include the response OID.

---

