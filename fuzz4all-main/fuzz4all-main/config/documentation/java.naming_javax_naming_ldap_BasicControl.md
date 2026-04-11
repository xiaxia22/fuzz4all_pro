# Class BasicControl

**Source:** `java.naming\javax\naming\ldap\BasicControl.html`

### Class Description

```java
public class
BasicControl

extends
Object

implements
Control
```

This class provides a basic implementation of the

Control

interface. It represents an LDAPv3 Control as defined in

RFC 2251

.

**All Implemented Interfaces:** Serializable

,

Control

---

### Field Details

#### protected
String
id

The control's object identifier string.

---

#### protected boolean criticality

The control's criticality.

---

#### protected byte[] value

The control's ASN.1 BER encoded value.

---

### Constructor Details

#### public BasicControl​(
String
id)

Constructs a non-critical control.

**Parameters:**
- id

- The control's object identifier string.

---

#### public BasicControl​(
String
id,
boolean criticality,
byte[] value)

Constructs a control using the supplied arguments.

**Parameters:**
- id

- The control's object identifier string.
- criticality

- The control's criticality.
- value

- The control's ASN.1 BER encoded value.
It is not cloned - any changes to value
will affect the contents of the control.
It may be null.

---

### Method Details

#### public
String
getID()

Retrieves the control's object identifier string.

**Specified by:**
- getID

in interface

Control

**Returns:**
- The non-null object identifier string.

---

#### public boolean isCritical()

Determines the control's criticality.

**Specified by:**
- isCritical

in interface

Control

**Returns:**
- true if the control is critical; false otherwise.

---

#### public byte[] getEncodedValue()

Retrieves the control's ASN.1 BER encoded value.
The result includes the BER tag and length for the control's value but
does not include the control's object identifier and criticality setting.

**Specified by:**
- getEncodedValue

in interface

Control

**Returns:**
- A possibly null byte array representing the control's
ASN.1 BER encoded value. It is not cloned - any changes to the
returned value will affect the contents of the control.

---

### Additional Sections

#### Class BasicControl

java.lang.Object

- javax.naming.ldap.BasicControl

javax.naming.ldap.BasicControl

**All Implemented Interfaces:** Serializable

,

Control

**Direct Known Subclasses:** ManageReferralControl

,

PagedResultsControl

,

PagedResultsResponseControl

,

SortControl

,

SortResponseControl

```java
public class
BasicControl

extends
Object

implements
Control
```

This class provides a basic implementation of the

Control

interface. It represents an LDAPv3 Control as defined in

RFC 2251

.

**Since:** 1.5
**See Also:** Serialized Form

public class

BasicControl

extends

Object

implements

Control

This class provides a basic implementation of the

Control

interface. It represents an LDAPv3 Control as defined in

RFC 2251

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected boolean

criticality

The control's criticality.

protected

String

id

The control's object identifier string.

protected byte[]

value

The control's ASN.1 BER encoded value.

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

BasicControl

​(

String

id)

Constructs a non-critical control.

BasicControl

​(

String

id,
boolean criticality,
byte[] value)

Constructs a control using the supplied arguments.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

getEncodedValue

()

Retrieves the control's ASN.1 BER encoded value.

String

getID

()

Retrieves the control's object identifier string.

boolean

isCritical

()

Determines the control's criticality.

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

protected boolean

criticality

The control's criticality.

protected

String

id

The control's object identifier string.

protected byte[]

value

The control's ASN.1 BER encoded value.

- Fields declared in interface javax.naming.ldap.

Control

CRITICAL

,

NONCRITICAL

---

#### Field Summary

The control's criticality.

The control's object identifier string.

The control's ASN.1 BER encoded value.

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

BasicControl

​(

String

id)

Constructs a non-critical control.

BasicControl

​(

String

id,
boolean criticality,
byte[] value)

Constructs a control using the supplied arguments.

---

#### Constructor Summary

Constructs a non-critical control.

Constructs a control using the supplied arguments.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

getEncodedValue

()

Retrieves the control's ASN.1 BER encoded value.

String

getID

()

Retrieves the control's object identifier string.

boolean

isCritical

()

Determines the control's criticality.

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

Retrieves the control's ASN.1 BER encoded value.

Retrieves the control's object identifier string.

Determines the control's criticality.

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

- id

```java
protected
String
id
```

The control's object identifier string.

- criticality

```java
protected boolean criticality
```

The control's criticality.

- value

```java
protected byte[] value
```

The control's ASN.1 BER encoded value.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicControl

```java
public BasicControl​(
String
id)
```

Constructs a non-critical control.

**Parameters:** id

- The control's object identifier string.

- BasicControl

```java
public BasicControl​(
String
id,
boolean criticality,
byte[] value)
```

Constructs a control using the supplied arguments.

**Parameters:** id

- The control's object identifier string.
**Parameters:** criticality

- The control's criticality.
**Parameters:** value

- The control's ASN.1 BER encoded value.
It is not cloned - any changes to value
will affect the contents of the control.
It may be null.

============ METHOD DETAIL ==========

- Method Detail

- getID

```java
public
String
getID()
```

Retrieves the control's object identifier string.

**Specified by:** getID

in interface

Control
**Returns:** The non-null object identifier string.

- isCritical

```java
public boolean isCritical()
```

Determines the control's criticality.

**Specified by:** isCritical

in interface

Control
**Returns:** true if the control is critical; false otherwise.

- getEncodedValue

```java
public byte[] getEncodedValue()
```

Retrieves the control's ASN.1 BER encoded value.
The result includes the BER tag and length for the control's value but
does not include the control's object identifier and criticality setting.

**Specified by:** getEncodedValue

in interface

Control
**Returns:** A possibly null byte array representing the control's
ASN.1 BER encoded value. It is not cloned - any changes to the
returned value will affect the contents of the control.

Field Detail

- id

```java
protected
String
id
```

The control's object identifier string.

- criticality

```java
protected boolean criticality
```

The control's criticality.

- value

```java
protected byte[] value
```

The control's ASN.1 BER encoded value.

---

#### Field Detail

id

```java
protected
String
id
```

The control's object identifier string.

---

#### id

protected

String

id

The control's object identifier string.

criticality

```java
protected boolean criticality
```

The control's criticality.

---

#### criticality

protected boolean criticality

The control's criticality.

value

```java
protected byte[] value
```

The control's ASN.1 BER encoded value.

---

#### value

protected byte[] value

The control's ASN.1 BER encoded value.

Constructor Detail

- BasicControl

```java
public BasicControl​(
String
id)
```

Constructs a non-critical control.

**Parameters:** id

- The control's object identifier string.

- BasicControl

```java
public BasicControl​(
String
id,
boolean criticality,
byte[] value)
```

Constructs a control using the supplied arguments.

**Parameters:** id

- The control's object identifier string.
**Parameters:** criticality

- The control's criticality.
**Parameters:** value

- The control's ASN.1 BER encoded value.
It is not cloned - any changes to value
will affect the contents of the control.
It may be null.

---

#### Constructor Detail

BasicControl

```java
public BasicControl​(
String
id)
```

Constructs a non-critical control.

**Parameters:** id

- The control's object identifier string.

---

#### BasicControl

public BasicControl​(

String

id)

Constructs a non-critical control.

BasicControl

```java
public BasicControl​(
String
id,
boolean criticality,
byte[] value)
```

Constructs a control using the supplied arguments.

**Parameters:** id

- The control's object identifier string.
**Parameters:** criticality

- The control's criticality.
**Parameters:** value

- The control's ASN.1 BER encoded value.
It is not cloned - any changes to value
will affect the contents of the control.
It may be null.

---

#### BasicControl

public BasicControl​(

String

id,
boolean criticality,
byte[] value)

Constructs a control using the supplied arguments.

Method Detail

- getID

```java
public
String
getID()
```

Retrieves the control's object identifier string.

**Specified by:** getID

in interface

Control
**Returns:** The non-null object identifier string.

- isCritical

```java
public boolean isCritical()
```

Determines the control's criticality.

**Specified by:** isCritical

in interface

Control
**Returns:** true if the control is critical; false otherwise.

- getEncodedValue

```java
public byte[] getEncodedValue()
```

Retrieves the control's ASN.1 BER encoded value.
The result includes the BER tag and length for the control's value but
does not include the control's object identifier and criticality setting.

**Specified by:** getEncodedValue

in interface

Control
**Returns:** A possibly null byte array representing the control's
ASN.1 BER encoded value. It is not cloned - any changes to the
returned value will affect the contents of the control.

---

#### Method Detail

getID

```java
public
String
getID()
```

Retrieves the control's object identifier string.

**Specified by:** getID

in interface

Control
**Returns:** The non-null object identifier string.

---

#### getID

public

String

getID()

Retrieves the control's object identifier string.

isCritical

```java
public boolean isCritical()
```

Determines the control's criticality.

**Specified by:** isCritical

in interface

Control
**Returns:** true if the control is critical; false otherwise.

---

#### isCritical

public boolean isCritical()

Determines the control's criticality.

getEncodedValue

```java
public byte[] getEncodedValue()
```

Retrieves the control's ASN.1 BER encoded value.
The result includes the BER tag and length for the control's value but
does not include the control's object identifier and criticality setting.

**Specified by:** getEncodedValue

in interface

Control
**Returns:** A possibly null byte array representing the control's
ASN.1 BER encoded value. It is not cloned - any changes to the
returned value will affect the contents of the control.

---

#### getEncodedValue

public byte[] getEncodedValue()

Retrieves the control's ASN.1 BER encoded value.
The result includes the BER tag and length for the control's value but
does not include the control's object identifier and criticality setting.

---

