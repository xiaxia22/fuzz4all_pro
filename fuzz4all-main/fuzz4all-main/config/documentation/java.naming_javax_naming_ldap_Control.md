# Interface Control

**Source:** `java.naming\javax\naming\ldap\Control.html`

### Class Description

```java
public interface
Control

extends
Serializable
```

This interface represents an LDAPv3 control as defined in

RFC 2251

.

The LDAPv3 protocol uses controls to send and receive additional data
to affect the behavior of predefined operations.
Controls can be sent along with any LDAP operation to the server.
These are referred to as

request controls

. For example, a
"sort" control can be sent with an LDAP search operation to
request that the results be returned in a particular order.
Solicited and unsolicited controls can also be returned with
responses from the server. Such controls are referred to as

response controls

. For example, an LDAP server might
define a special control to return change notifications.

This interface is used to represent both request and response controls.

**All Superinterfaces:** Serializable

---

### Field Details

#### static final boolean CRITICAL

Indicates a critical control.
The value of this constant is

true

.

**See Also:**
- Constant Field Values

---

#### static final boolean NONCRITICAL

Indicates a non-critical control.
The value of this constant is

false

.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### String
getID()

Retrieves the object identifier assigned for the LDAP control.

**Returns:**
- The non-null object identifier string.

---

#### boolean isCritical()

Determines the criticality of the LDAP control.
A critical control must not be ignored by the server.
In other words, if the server receives a critical control
that it does not support, regardless of whether the control
makes sense for the operation, the operation will not be performed
and an

OperationNotSupportedException

will be thrown.

**Returns:**
- true if this control is critical; false otherwise.

---

#### byte[] getEncodedValue()

Retrieves the ASN.1 BER encoded value of the LDAP control.
The result is the raw BER bytes including the tag and length of
the control's value. It does not include the controls OID or criticality.

Null is returned if the value is absent.

**Returns:**
- A possibly null byte array representing the ASN.1 BER encoded
value of the LDAP control.

---

### Additional Sections

#### Interface Control

**All Superinterfaces:** Serializable

**All Known Implementing Classes:** BasicControl

,

ManageReferralControl

,

PagedResultsControl

,

PagedResultsResponseControl

,

SortControl

,

SortResponseControl

```java
public interface
Control

extends
Serializable
```

This interface represents an LDAPv3 control as defined in

RFC 2251

.

The LDAPv3 protocol uses controls to send and receive additional data
to affect the behavior of predefined operations.
Controls can be sent along with any LDAP operation to the server.
These are referred to as

request controls

. For example, a
"sort" control can be sent with an LDAP search operation to
request that the results be returned in a particular order.
Solicited and unsolicited controls can also be returned with
responses from the server. Such controls are referred to as

response controls

. For example, an LDAP server might
define a special control to return change notifications.

This interface is used to represent both request and response controls.

**Since:** 1.3
**See Also:** ControlFactory

public interface

Control

extends

Serializable

This interface represents an LDAPv3 control as defined in

RFC 2251

.

The LDAPv3 protocol uses controls to send and receive additional data
to affect the behavior of predefined operations.
Controls can be sent along with any LDAP operation to the server.
These are referred to as

request controls

. For example, a
"sort" control can be sent with an LDAP search operation to
request that the results be returned in a particular order.
Solicited and unsolicited controls can also be returned with
responses from the server. Such controls are referred to as

response controls

. For example, an LDAP server might
define a special control to return change notifications.

This interface is used to represent both request and response controls.

The LDAPv3 protocol uses controls to send and receive additional data
to affect the behavior of predefined operations.
Controls can be sent along with any LDAP operation to the server.
These are referred to as

request controls

. For example, a
"sort" control can be sent with an LDAP search operation to
request that the results be returned in a particular order.
Solicited and unsolicited controls can also be returned with
responses from the server. Such controls are referred to as

response controls

. For example, an LDAP server might
define a special control to return change notifications.

This interface is used to represent both request and response controls.

This interface is used to represent both request and response controls.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static boolean

CRITICAL

Indicates a critical control.

static boolean

NONCRITICAL

Indicates a non-critical control.

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

Retrieves the ASN.1 BER encoded value of the LDAP control.

String

getID

()

Retrieves the object identifier assigned for the LDAP control.

boolean

isCritical

()

Determines the criticality of the LDAP control.

Field Summary

Fields

Modifier and Type

Field

Description

static boolean

CRITICAL

Indicates a critical control.

static boolean

NONCRITICAL

Indicates a non-critical control.

---

#### Field Summary

Indicates a critical control.

Indicates a non-critical control.

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

Retrieves the ASN.1 BER encoded value of the LDAP control.

String

getID

()

Retrieves the object identifier assigned for the LDAP control.

boolean

isCritical

()

Determines the criticality of the LDAP control.

---

#### Method Summary

Retrieves the ASN.1 BER encoded value of the LDAP control.

Retrieves the object identifier assigned for the LDAP control.

Determines the criticality of the LDAP control.

============ FIELD DETAIL ===========

- Field Detail

- CRITICAL

```java
static final boolean CRITICAL
```

Indicates a critical control.
The value of this constant is

true

.

**See Also:** Constant Field Values

- NONCRITICAL

```java
static final boolean NONCRITICAL
```

Indicates a non-critical control.
The value of this constant is

false

.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getID

```java
String
getID()
```

Retrieves the object identifier assigned for the LDAP control.

**Returns:** The non-null object identifier string.

- isCritical

```java
boolean isCritical()
```

Determines the criticality of the LDAP control.
A critical control must not be ignored by the server.
In other words, if the server receives a critical control
that it does not support, regardless of whether the control
makes sense for the operation, the operation will not be performed
and an

OperationNotSupportedException

will be thrown.

**Returns:** true if this control is critical; false otherwise.

- getEncodedValue

```java
byte[] getEncodedValue()
```

Retrieves the ASN.1 BER encoded value of the LDAP control.
The result is the raw BER bytes including the tag and length of
the control's value. It does not include the controls OID or criticality.

Null is returned if the value is absent.

**Returns:** A possibly null byte array representing the ASN.1 BER encoded
value of the LDAP control.

Field Detail

- CRITICAL

```java
static final boolean CRITICAL
```

Indicates a critical control.
The value of this constant is

true

.

**See Also:** Constant Field Values

- NONCRITICAL

```java
static final boolean NONCRITICAL
```

Indicates a non-critical control.
The value of this constant is

false

.

**See Also:** Constant Field Values

---

#### Field Detail

CRITICAL

```java
static final boolean CRITICAL
```

Indicates a critical control.
The value of this constant is

true

.

**See Also:** Constant Field Values

---

#### CRITICAL

static final boolean CRITICAL

Indicates a critical control.
The value of this constant is

true

.

NONCRITICAL

```java
static final boolean NONCRITICAL
```

Indicates a non-critical control.
The value of this constant is

false

.

**See Also:** Constant Field Values

---

#### NONCRITICAL

static final boolean NONCRITICAL

Indicates a non-critical control.
The value of this constant is

false

.

Method Detail

- getID

```java
String
getID()
```

Retrieves the object identifier assigned for the LDAP control.

**Returns:** The non-null object identifier string.

- isCritical

```java
boolean isCritical()
```

Determines the criticality of the LDAP control.
A critical control must not be ignored by the server.
In other words, if the server receives a critical control
that it does not support, regardless of whether the control
makes sense for the operation, the operation will not be performed
and an

OperationNotSupportedException

will be thrown.

**Returns:** true if this control is critical; false otherwise.

- getEncodedValue

```java
byte[] getEncodedValue()
```

Retrieves the ASN.1 BER encoded value of the LDAP control.
The result is the raw BER bytes including the tag and length of
the control's value. It does not include the controls OID or criticality.

Null is returned if the value is absent.

**Returns:** A possibly null byte array representing the ASN.1 BER encoded
value of the LDAP control.

---

#### Method Detail

getID

```java
String
getID()
```

Retrieves the object identifier assigned for the LDAP control.

**Returns:** The non-null object identifier string.

---

#### getID

String

getID()

Retrieves the object identifier assigned for the LDAP control.

isCritical

```java
boolean isCritical()
```

Determines the criticality of the LDAP control.
A critical control must not be ignored by the server.
In other words, if the server receives a critical control
that it does not support, regardless of whether the control
makes sense for the operation, the operation will not be performed
and an

OperationNotSupportedException

will be thrown.

**Returns:** true if this control is critical; false otherwise.

---

#### isCritical

boolean isCritical()

Determines the criticality of the LDAP control.
A critical control must not be ignored by the server.
In other words, if the server receives a critical control
that it does not support, regardless of whether the control
makes sense for the operation, the operation will not be performed
and an

OperationNotSupportedException

will be thrown.

getEncodedValue

```java
byte[] getEncodedValue()
```

Retrieves the ASN.1 BER encoded value of the LDAP control.
The result is the raw BER bytes including the tag and length of
the control's value. It does not include the controls OID or criticality.

Null is returned if the value is absent.

**Returns:** A possibly null byte array representing the ASN.1 BER encoded
value of the LDAP control.

---

#### getEncodedValue

byte[] getEncodedValue()

Retrieves the ASN.1 BER encoded value of the LDAP control.
The result is the raw BER bytes including the tag and length of
the control's value. It does not include the controls OID or criticality.

Null is returned if the value is absent.

---

