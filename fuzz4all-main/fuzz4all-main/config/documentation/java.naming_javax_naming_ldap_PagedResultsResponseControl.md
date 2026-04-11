# Class PagedResultsResponseControl

**Source:** `java.naming\javax\naming\ldap\PagedResultsResponseControl.html`

### Class Description

```java
public final class
PagedResultsResponseControl

extends
BasicControl
```

Indicates the end of a batch of search results.
Contains an estimate of the total number of entries in the result set
and an opaque cookie. The cookie must be supplied to the next search
operation in order to get the next batch of results.

The code sample in

PagedResultsControl

shows how this class may
be used.

This class implements the LDAPv3 Response Control for
paged-results as defined in

RFC 2696

.

The control's value has the following ASN.1 definition:

```java
realSearchControlValue ::= SEQUENCE {
size INTEGER (0..maxInt),
-- requested page size from client
-- result set size estimate from server
cookie OCTET STRING
}
```

**All Implemented Interfaces:** Serializable

,

Control

---

### Field Details

#### public static final
String
OID

The paged-results response control's assigned object identifier
is 1.2.840.113556.1.4.319.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public PagedResultsResponseControl​(
String
id,
boolean criticality,
byte[] value)
throws
IOException

Constructs a paged-results response control.

**Parameters:**
- id

- The control's object identifier string.
- criticality

- The control's criticality.
- value

- The control's ASN.1 BER encoded value.
It is not cloned - any changes to value
will affect the contents of the control.

**Throws:**
- IOException

- If an error was encountered while decoding
the control's value.

---

### Method Details

#### public int getResultSize()

Retrieves (an estimate of) the number of entries in the search result.

**Returns:**
- The number of entries in the search result, or zero if unknown.

---

#### public byte[] getCookie()

Retrieves the server-generated cookie. Null is returned when there are
no more entries for the server to return.

**Returns:**
- A possibly null server-generated cookie. It is not cloned - any
changes to the cookie will update the control's state and thus
are not recommended.

---

### Additional Sections

#### Class PagedResultsResponseControl

java.lang.Object

- javax.naming.ldap.BasicControl
- - javax.naming.ldap.PagedResultsResponseControl

javax.naming.ldap.BasicControl

- javax.naming.ldap.PagedResultsResponseControl

javax.naming.ldap.PagedResultsResponseControl

**All Implemented Interfaces:** Serializable

,

Control

```java
public final class
PagedResultsResponseControl

extends
BasicControl
```

Indicates the end of a batch of search results.
Contains an estimate of the total number of entries in the result set
and an opaque cookie. The cookie must be supplied to the next search
operation in order to get the next batch of results.

The code sample in

PagedResultsControl

shows how this class may
be used.

This class implements the LDAPv3 Response Control for
paged-results as defined in

RFC 2696

.

The control's value has the following ASN.1 definition:

```java
realSearchControlValue ::= SEQUENCE {
size INTEGER (0..maxInt),
-- requested page size from client
-- result set size estimate from server
cookie OCTET STRING
}
```

**Since:** 1.5
**See Also:** PagedResultsControl

,

Serialized Form

public final class

PagedResultsResponseControl

extends

BasicControl

Indicates the end of a batch of search results.
Contains an estimate of the total number of entries in the result set
and an opaque cookie. The cookie must be supplied to the next search
operation in order to get the next batch of results.

The code sample in

PagedResultsControl

shows how this class may
be used.

This class implements the LDAPv3 Response Control for
paged-results as defined in

RFC 2696

.

The control's value has the following ASN.1 definition:

```java
realSearchControlValue ::= SEQUENCE {
size INTEGER (0..maxInt),
-- requested page size from client
-- result set size estimate from server
cookie OCTET STRING
}
```

The code sample in

PagedResultsControl

shows how this class may
be used.

This class implements the LDAPv3 Response Control for
paged-results as defined in

RFC 2696

.

The control's value has the following ASN.1 definition:

```java
realSearchControlValue ::= SEQUENCE {
size INTEGER (0..maxInt),
-- requested page size from client
-- result set size estimate from server
cookie OCTET STRING
}
```

This class implements the LDAPv3 Response Control for
paged-results as defined in

RFC 2696

.

The control's value has the following ASN.1 definition:

```java
realSearchControlValue ::= SEQUENCE {
size INTEGER (0..maxInt),
-- requested page size from client
-- result set size estimate from server
cookie OCTET STRING
}
```

realSearchControlValue ::= SEQUENCE {
size INTEGER (0..maxInt),
-- requested page size from client
-- result set size estimate from server
cookie OCTET STRING
}

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

OID

The paged-results response control's assigned object identifier
is 1.2.840.113556.1.4.319.

- Fields declared in class javax.naming.ldap.

BasicControl

criticality

,

id

,

value

- Fields declared in interface javax.naming.ldap.

Control

CRITICAL

,

NONCRITICAL

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PagedResultsResponseControl

​(

String

id,
boolean criticality,
byte[] value)

Constructs a paged-results response control.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

getCookie

()

Retrieves the server-generated cookie.

int

getResultSize

()

Retrieves (an estimate of) the number of entries in the search result.

- Methods declared in class javax.naming.ldap.

BasicControl

getEncodedValue

,

getID

,

isCritical

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

static

String

OID

The paged-results response control's assigned object identifier
is 1.2.840.113556.1.4.319.

- Fields declared in class javax.naming.ldap.

BasicControl

criticality

,

id

,

value

- Fields declared in interface javax.naming.ldap.

Control

CRITICAL

,

NONCRITICAL

---

#### Field Summary

The paged-results response control's assigned object identifier
is 1.2.840.113556.1.4.319.

Fields declared in class javax.naming.ldap.

BasicControl

criticality

,

id

,

value

---

#### Fields declared in class javax.naming.ldap. BasicControl

Fields declared in interface javax.naming.ldap.

Control

CRITICAL

,

NONCRITICAL

---

#### Fields declared in interface javax.naming.ldap. Control

Constructor Summary

Constructors

Constructor

Description

PagedResultsResponseControl

​(

String

id,
boolean criticality,
byte[] value)

Constructs a paged-results response control.

---

#### Constructor Summary

Constructs a paged-results response control.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

getCookie

()

Retrieves the server-generated cookie.

int

getResultSize

()

Retrieves (an estimate of) the number of entries in the search result.

- Methods declared in class javax.naming.ldap.

BasicControl

getEncodedValue

,

getID

,

isCritical

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Retrieves the server-generated cookie.

Retrieves (an estimate of) the number of entries in the search result.

Methods declared in class javax.naming.ldap.

BasicControl

getEncodedValue

,

getID

,

isCritical

---

#### Methods declared in class javax.naming.ldap. BasicControl

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- OID

```java
public static final
String
OID
```

The paged-results response control's assigned object identifier
is 1.2.840.113556.1.4.319.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PagedResultsResponseControl

```java
public PagedResultsResponseControl​(
String
id,
boolean criticality,
byte[] value)
throws
IOException
```

Constructs a paged-results response control.

**Parameters:** id

- The control's object identifier string.
**Parameters:** criticality

- The control's criticality.
**Parameters:** value

- The control's ASN.1 BER encoded value.
It is not cloned - any changes to value
will affect the contents of the control.
**Throws:** IOException

- If an error was encountered while decoding
the control's value.

============ METHOD DETAIL ==========

- Method Detail

- getResultSize

```java
public int getResultSize()
```

Retrieves (an estimate of) the number of entries in the search result.

**Returns:** The number of entries in the search result, or zero if unknown.

- getCookie

```java
public byte[] getCookie()
```

Retrieves the server-generated cookie. Null is returned when there are
no more entries for the server to return.

**Returns:** A possibly null server-generated cookie. It is not cloned - any
changes to the cookie will update the control's state and thus
are not recommended.

Field Detail

- OID

```java
public static final
String
OID
```

The paged-results response control's assigned object identifier
is 1.2.840.113556.1.4.319.

**See Also:** Constant Field Values

---

#### Field Detail

OID

```java
public static final
String
OID
```

The paged-results response control's assigned object identifier
is 1.2.840.113556.1.4.319.

**See Also:** Constant Field Values

---

#### OID

public static final

String

OID

The paged-results response control's assigned object identifier
is 1.2.840.113556.1.4.319.

Constructor Detail

- PagedResultsResponseControl

```java
public PagedResultsResponseControl​(
String
id,
boolean criticality,
byte[] value)
throws
IOException
```

Constructs a paged-results response control.

**Parameters:** id

- The control's object identifier string.
**Parameters:** criticality

- The control's criticality.
**Parameters:** value

- The control's ASN.1 BER encoded value.
It is not cloned - any changes to value
will affect the contents of the control.
**Throws:** IOException

- If an error was encountered while decoding
the control's value.

---

#### Constructor Detail

PagedResultsResponseControl

```java
public PagedResultsResponseControl​(
String
id,
boolean criticality,
byte[] value)
throws
IOException
```

Constructs a paged-results response control.

**Parameters:** id

- The control's object identifier string.
**Parameters:** criticality

- The control's criticality.
**Parameters:** value

- The control's ASN.1 BER encoded value.
It is not cloned - any changes to value
will affect the contents of the control.
**Throws:** IOException

- If an error was encountered while decoding
the control's value.

---

#### PagedResultsResponseControl

public PagedResultsResponseControl​(

String

id,
boolean criticality,
byte[] value)
throws

IOException

Constructs a paged-results response control.

Method Detail

- getResultSize

```java
public int getResultSize()
```

Retrieves (an estimate of) the number of entries in the search result.

**Returns:** The number of entries in the search result, or zero if unknown.

- getCookie

```java
public byte[] getCookie()
```

Retrieves the server-generated cookie. Null is returned when there are
no more entries for the server to return.

**Returns:** A possibly null server-generated cookie. It is not cloned - any
changes to the cookie will update the control's state and thus
are not recommended.

---

#### Method Detail

getResultSize

```java
public int getResultSize()
```

Retrieves (an estimate of) the number of entries in the search result.

**Returns:** The number of entries in the search result, or zero if unknown.

---

#### getResultSize

public int getResultSize()

Retrieves (an estimate of) the number of entries in the search result.

getCookie

```java
public byte[] getCookie()
```

Retrieves the server-generated cookie. Null is returned when there are
no more entries for the server to return.

**Returns:** A possibly null server-generated cookie. It is not cloned - any
changes to the cookie will update the control's state and thus
are not recommended.

---

#### getCookie

public byte[] getCookie()

Retrieves the server-generated cookie. Null is returned when there are
no more entries for the server to return.

---

