# Class SortResponseControl

**Source:** `java.naming\javax\naming\ldap\SortResponseControl.html`

### Class Description

```java
public final class
SortResponseControl

extends
BasicControl
```

Indicates whether the requested sort of search results was successful or not.
When the result code indicates success then the results have been sorted as
requested. Otherwise the sort was unsuccessful and additional details
regarding the cause of the error may have been provided by the server.

The code sample in

SortControl

shows how this class may be used.

This class implements the LDAPv3 Response Control for server-side sorting
as defined in

RFC 2891

.

The control's value has the following ASN.1 definition:

```java
SortResult ::= SEQUENCE {
sortResult ENUMERATED {
success (0), -- results are sorted
operationsError (1), -- server internal failure
timeLimitExceeded (3), -- timelimit reached before
-- sorting was completed
strongAuthRequired (8), -- refused to return sorted
-- results via insecure
-- protocol
adminLimitExceeded (11), -- too many matching entries
-- for the server to sort
noSuchAttribute (16), -- unrecognized attribute
-- type in sort key
inappropriateMatching (18), -- unrecognized or inappro-
-- priate matching rule in
-- sort key
insufficientAccessRights (50), -- refused to return sorted
-- results to this client
busy (51), -- too busy to process
unwillingToPerform (53), -- unable to sort
other (80)
},
attributeType [0] AttributeType OPTIONAL }
```

**All Implemented Interfaces:** Serializable

,

Control

---

### Field Details

#### public static final
String
OID

The server-side sort response control's assigned object identifier
is 1.2.840.113556.1.4.474.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public SortResponseControl​(
String
id,
boolean criticality,
byte[] value)
throws
IOException

Constructs a control to indicate the outcome of a sort request.

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

- if an error is encountered
while decoding the control's value.

---

### Method Details

#### public boolean isSorted()

Determines if the search results have been successfully sorted.
If an error occurred during sorting a NamingException is thrown.

**Returns:**
- true if the search results have been sorted.

---

#### public int getResultCode()

Retrieves the LDAP result code of the sort operation.

**Returns:**
- The result code. A zero value indicates success.

---

#### public
String
getAttributeID()

Retrieves the ID of the attribute that caused the sort to fail.
Returns null if no ID was returned by the server.

**Returns:**
- The possibly null ID of the bad attribute.

---

#### public
NamingException
getException()

Retrieves the NamingException appropriate for the result code.

**Returns:**
- A NamingException or null if the result code indicates
success.

---

### Additional Sections

#### Class SortResponseControl

java.lang.Object

- javax.naming.ldap.BasicControl
- - javax.naming.ldap.SortResponseControl

javax.naming.ldap.BasicControl

- javax.naming.ldap.SortResponseControl

javax.naming.ldap.SortResponseControl

**All Implemented Interfaces:** Serializable

,

Control

```java
public final class
SortResponseControl

extends
BasicControl
```

Indicates whether the requested sort of search results was successful or not.
When the result code indicates success then the results have been sorted as
requested. Otherwise the sort was unsuccessful and additional details
regarding the cause of the error may have been provided by the server.

The code sample in

SortControl

shows how this class may be used.

This class implements the LDAPv3 Response Control for server-side sorting
as defined in

RFC 2891

.

The control's value has the following ASN.1 definition:

```java
SortResult ::= SEQUENCE {
sortResult ENUMERATED {
success (0), -- results are sorted
operationsError (1), -- server internal failure
timeLimitExceeded (3), -- timelimit reached before
-- sorting was completed
strongAuthRequired (8), -- refused to return sorted
-- results via insecure
-- protocol
adminLimitExceeded (11), -- too many matching entries
-- for the server to sort
noSuchAttribute (16), -- unrecognized attribute
-- type in sort key
inappropriateMatching (18), -- unrecognized or inappro-
-- priate matching rule in
-- sort key
insufficientAccessRights (50), -- refused to return sorted
-- results to this client
busy (51), -- too busy to process
unwillingToPerform (53), -- unable to sort
other (80)
},
attributeType [0] AttributeType OPTIONAL }
```

**Since:** 1.5
**See Also:** SortControl

,

Serialized Form

public final class

SortResponseControl

extends

BasicControl

Indicates whether the requested sort of search results was successful or not.
When the result code indicates success then the results have been sorted as
requested. Otherwise the sort was unsuccessful and additional details
regarding the cause of the error may have been provided by the server.

The code sample in

SortControl

shows how this class may be used.

This class implements the LDAPv3 Response Control for server-side sorting
as defined in

RFC 2891

.

The control's value has the following ASN.1 definition:

```java
SortResult ::= SEQUENCE {
sortResult ENUMERATED {
success (0), -- results are sorted
operationsError (1), -- server internal failure
timeLimitExceeded (3), -- timelimit reached before
-- sorting was completed
strongAuthRequired (8), -- refused to return sorted
-- results via insecure
-- protocol
adminLimitExceeded (11), -- too many matching entries
-- for the server to sort
noSuchAttribute (16), -- unrecognized attribute
-- type in sort key
inappropriateMatching (18), -- unrecognized or inappro-
-- priate matching rule in
-- sort key
insufficientAccessRights (50), -- refused to return sorted
-- results to this client
busy (51), -- too busy to process
unwillingToPerform (53), -- unable to sort
other (80)
},
attributeType [0] AttributeType OPTIONAL }
```

The code sample in

SortControl

shows how this class may be used.

This class implements the LDAPv3 Response Control for server-side sorting
as defined in

RFC 2891

.

The control's value has the following ASN.1 definition:

```java
SortResult ::= SEQUENCE {
sortResult ENUMERATED {
success (0), -- results are sorted
operationsError (1), -- server internal failure
timeLimitExceeded (3), -- timelimit reached before
-- sorting was completed
strongAuthRequired (8), -- refused to return sorted
-- results via insecure
-- protocol
adminLimitExceeded (11), -- too many matching entries
-- for the server to sort
noSuchAttribute (16), -- unrecognized attribute
-- type in sort key
inappropriateMatching (18), -- unrecognized or inappro-
-- priate matching rule in
-- sort key
insufficientAccessRights (50), -- refused to return sorted
-- results to this client
busy (51), -- too busy to process
unwillingToPerform (53), -- unable to sort
other (80)
},
attributeType [0] AttributeType OPTIONAL }
```

This class implements the LDAPv3 Response Control for server-side sorting
as defined in

RFC 2891

.

The control's value has the following ASN.1 definition:

```java
SortResult ::= SEQUENCE {
sortResult ENUMERATED {
success (0), -- results are sorted
operationsError (1), -- server internal failure
timeLimitExceeded (3), -- timelimit reached before
-- sorting was completed
strongAuthRequired (8), -- refused to return sorted
-- results via insecure
-- protocol
adminLimitExceeded (11), -- too many matching entries
-- for the server to sort
noSuchAttribute (16), -- unrecognized attribute
-- type in sort key
inappropriateMatching (18), -- unrecognized or inappro-
-- priate matching rule in
-- sort key
insufficientAccessRights (50), -- refused to return sorted
-- results to this client
busy (51), -- too busy to process
unwillingToPerform (53), -- unable to sort
other (80)
},
attributeType [0] AttributeType OPTIONAL }
```

SortResult ::= SEQUENCE {
sortResult ENUMERATED {
success (0), -- results are sorted
operationsError (1), -- server internal failure
timeLimitExceeded (3), -- timelimit reached before
-- sorting was completed
strongAuthRequired (8), -- refused to return sorted
-- results via insecure
-- protocol
adminLimitExceeded (11), -- too many matching entries
-- for the server to sort
noSuchAttribute (16), -- unrecognized attribute
-- type in sort key
inappropriateMatching (18), -- unrecognized or inappro-
-- priate matching rule in
-- sort key
insufficientAccessRights (50), -- refused to return sorted
-- results to this client
busy (51), -- too busy to process
unwillingToPerform (53), -- unable to sort
other (80)
},
attributeType [0] AttributeType OPTIONAL }

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

OID

The server-side sort response control's assigned object identifier
is 1.2.840.113556.1.4.474.

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

SortResponseControl

​(

String

id,
boolean criticality,
byte[] value)

Constructs a control to indicate the outcome of a sort request.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAttributeID

()

Retrieves the ID of the attribute that caused the sort to fail.

NamingException

getException

()

Retrieves the NamingException appropriate for the result code.

int

getResultCode

()

Retrieves the LDAP result code of the sort operation.

boolean

isSorted

()

Determines if the search results have been successfully sorted.

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

The server-side sort response control's assigned object identifier
is 1.2.840.113556.1.4.474.

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

The server-side sort response control's assigned object identifier
is 1.2.840.113556.1.4.474.

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

SortResponseControl

​(

String

id,
boolean criticality,
byte[] value)

Constructs a control to indicate the outcome of a sort request.

---

#### Constructor Summary

Constructs a control to indicate the outcome of a sort request.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAttributeID

()

Retrieves the ID of the attribute that caused the sort to fail.

NamingException

getException

()

Retrieves the NamingException appropriate for the result code.

int

getResultCode

()

Retrieves the LDAP result code of the sort operation.

boolean

isSorted

()

Determines if the search results have been successfully sorted.

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

Retrieves the ID of the attribute that caused the sort to fail.

Retrieves the NamingException appropriate for the result code.

Retrieves the LDAP result code of the sort operation.

Determines if the search results have been successfully sorted.

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

The server-side sort response control's assigned object identifier
is 1.2.840.113556.1.4.474.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SortResponseControl

```java
public SortResponseControl​(
String
id,
boolean criticality,
byte[] value)
throws
IOException
```

Constructs a control to indicate the outcome of a sort request.

**Parameters:** id

- The control's object identifier string.
**Parameters:** criticality

- The control's criticality.
**Parameters:** value

- The control's ASN.1 BER encoded value.
It is not cloned - any changes to value
will affect the contents of the control.
**Throws:** IOException

- if an error is encountered
while decoding the control's value.

============ METHOD DETAIL ==========

- Method Detail

- isSorted

```java
public boolean isSorted()
```

Determines if the search results have been successfully sorted.
If an error occurred during sorting a NamingException is thrown.

**Returns:** true if the search results have been sorted.

- getResultCode

```java
public int getResultCode()
```

Retrieves the LDAP result code of the sort operation.

**Returns:** The result code. A zero value indicates success.

- getAttributeID

```java
public
String
getAttributeID()
```

Retrieves the ID of the attribute that caused the sort to fail.
Returns null if no ID was returned by the server.

**Returns:** The possibly null ID of the bad attribute.

- getException

```java
public
NamingException
getException()
```

Retrieves the NamingException appropriate for the result code.

**Returns:** A NamingException or null if the result code indicates
success.

Field Detail

- OID

```java
public static final
String
OID
```

The server-side sort response control's assigned object identifier
is 1.2.840.113556.1.4.474.

**See Also:** Constant Field Values

---

#### Field Detail

OID

```java
public static final
String
OID
```

The server-side sort response control's assigned object identifier
is 1.2.840.113556.1.4.474.

**See Also:** Constant Field Values

---

#### OID

public static final

String

OID

The server-side sort response control's assigned object identifier
is 1.2.840.113556.1.4.474.

Constructor Detail

- SortResponseControl

```java
public SortResponseControl​(
String
id,
boolean criticality,
byte[] value)
throws
IOException
```

Constructs a control to indicate the outcome of a sort request.

**Parameters:** id

- The control's object identifier string.
**Parameters:** criticality

- The control's criticality.
**Parameters:** value

- The control's ASN.1 BER encoded value.
It is not cloned - any changes to value
will affect the contents of the control.
**Throws:** IOException

- if an error is encountered
while decoding the control's value.

---

#### Constructor Detail

SortResponseControl

```java
public SortResponseControl​(
String
id,
boolean criticality,
byte[] value)
throws
IOException
```

Constructs a control to indicate the outcome of a sort request.

**Parameters:** id

- The control's object identifier string.
**Parameters:** criticality

- The control's criticality.
**Parameters:** value

- The control's ASN.1 BER encoded value.
It is not cloned - any changes to value
will affect the contents of the control.
**Throws:** IOException

- if an error is encountered
while decoding the control's value.

---

#### SortResponseControl

public SortResponseControl​(

String

id,
boolean criticality,
byte[] value)
throws

IOException

Constructs a control to indicate the outcome of a sort request.

Method Detail

- isSorted

```java
public boolean isSorted()
```

Determines if the search results have been successfully sorted.
If an error occurred during sorting a NamingException is thrown.

**Returns:** true if the search results have been sorted.

- getResultCode

```java
public int getResultCode()
```

Retrieves the LDAP result code of the sort operation.

**Returns:** The result code. A zero value indicates success.

- getAttributeID

```java
public
String
getAttributeID()
```

Retrieves the ID of the attribute that caused the sort to fail.
Returns null if no ID was returned by the server.

**Returns:** The possibly null ID of the bad attribute.

- getException

```java
public
NamingException
getException()
```

Retrieves the NamingException appropriate for the result code.

**Returns:** A NamingException or null if the result code indicates
success.

---

#### Method Detail

isSorted

```java
public boolean isSorted()
```

Determines if the search results have been successfully sorted.
If an error occurred during sorting a NamingException is thrown.

**Returns:** true if the search results have been sorted.

---

#### isSorted

public boolean isSorted()

Determines if the search results have been successfully sorted.
If an error occurred during sorting a NamingException is thrown.

getResultCode

```java
public int getResultCode()
```

Retrieves the LDAP result code of the sort operation.

**Returns:** The result code. A zero value indicates success.

---

#### getResultCode

public int getResultCode()

Retrieves the LDAP result code of the sort operation.

getAttributeID

```java
public
String
getAttributeID()
```

Retrieves the ID of the attribute that caused the sort to fail.
Returns null if no ID was returned by the server.

**Returns:** The possibly null ID of the bad attribute.

---

#### getAttributeID

public

String

getAttributeID()

Retrieves the ID of the attribute that caused the sort to fail.
Returns null if no ID was returned by the server.

getException

```java
public
NamingException
getException()
```

Retrieves the NamingException appropriate for the result code.

**Returns:** A NamingException or null if the result code indicates
success.

---

#### getException

public

NamingException

getException()

Retrieves the NamingException appropriate for the result code.

---

