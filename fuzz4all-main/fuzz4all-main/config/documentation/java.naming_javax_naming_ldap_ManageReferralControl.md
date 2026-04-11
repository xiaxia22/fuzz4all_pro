# Class ManageReferralControl

**Source:** `java.naming\javax\naming\ldap\ManageReferralControl.html`

### Class Description

```java
public final class
ManageReferralControl

extends
BasicControl
```

Requests that referral and other special LDAP objects be manipulated
as normal LDAP objects. It enables the requestor to interrogate or
update such objects.

This class implements the LDAPv3 Request Control for ManageDsaIT
as defined in

RFC 3296

.

The control has no control value.

**All Implemented Interfaces:** Serializable

,

Control

---

### Field Details

#### public static final
String
OID

The ManageReferral control's assigned object identifier
is 2.16.840.1.113730.3.4.2.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public ManageReferralControl()

Constructs a critical ManageReferral control.

---

#### public ManageReferralControl​(boolean criticality)

Constructs a ManageReferral control.

**Parameters:**
- criticality

- The control's criticality setting.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class ManageReferralControl

java.lang.Object

- javax.naming.ldap.BasicControl
- - javax.naming.ldap.ManageReferralControl

javax.naming.ldap.BasicControl

- javax.naming.ldap.ManageReferralControl

javax.naming.ldap.ManageReferralControl

**All Implemented Interfaces:** Serializable

,

Control

```java
public final class
ManageReferralControl

extends
BasicControl
```

Requests that referral and other special LDAP objects be manipulated
as normal LDAP objects. It enables the requestor to interrogate or
update such objects.

This class implements the LDAPv3 Request Control for ManageDsaIT
as defined in

RFC 3296

.

The control has no control value.

**Since:** 1.5
**See Also:** Serialized Form

public final class

ManageReferralControl

extends

BasicControl

Requests that referral and other special LDAP objects be manipulated
as normal LDAP objects. It enables the requestor to interrogate or
update such objects.

This class implements the LDAPv3 Request Control for ManageDsaIT
as defined in

RFC 3296

.

The control has no control value.

This class implements the LDAPv3 Request Control for ManageDsaIT
as defined in

RFC 3296

.

The control has no control value.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

OID

The ManageReferral control's assigned object identifier
is 2.16.840.1.113730.3.4.2.

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

ManageReferralControl

()

Constructs a critical ManageReferral control.

ManageReferralControl

​(boolean criticality)

Constructs a ManageReferral control.

========== METHOD SUMMARY ===========

- Method Summary

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

The ManageReferral control's assigned object identifier
is 2.16.840.1.113730.3.4.2.

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

The ManageReferral control's assigned object identifier
is 2.16.840.1.113730.3.4.2.

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

ManageReferralControl

()

Constructs a critical ManageReferral control.

ManageReferralControl

​(boolean criticality)

Constructs a ManageReferral control.

---

#### Constructor Summary

Constructs a critical ManageReferral control.

Constructs a ManageReferral control.

Method Summary

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

The ManageReferral control's assigned object identifier
is 2.16.840.1.113730.3.4.2.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ManageReferralControl

```java
public ManageReferralControl()
```

Constructs a critical ManageReferral control.

- ManageReferralControl

```java
public ManageReferralControl​(boolean criticality)
```

Constructs a ManageReferral control.

**Parameters:** criticality

- The control's criticality setting.

Field Detail

- OID

```java
public static final
String
OID
```

The ManageReferral control's assigned object identifier
is 2.16.840.1.113730.3.4.2.

**See Also:** Constant Field Values

---

#### Field Detail

OID

```java
public static final
String
OID
```

The ManageReferral control's assigned object identifier
is 2.16.840.1.113730.3.4.2.

**See Also:** Constant Field Values

---

#### OID

public static final

String

OID

The ManageReferral control's assigned object identifier
is 2.16.840.1.113730.3.4.2.

Constructor Detail

- ManageReferralControl

```java
public ManageReferralControl()
```

Constructs a critical ManageReferral control.

- ManageReferralControl

```java
public ManageReferralControl​(boolean criticality)
```

Constructs a ManageReferral control.

**Parameters:** criticality

- The control's criticality setting.

---

#### Constructor Detail

ManageReferralControl

```java
public ManageReferralControl()
```

Constructs a critical ManageReferral control.

---

#### ManageReferralControl

public ManageReferralControl()

Constructs a critical ManageReferral control.

ManageReferralControl

```java
public ManageReferralControl​(boolean criticality)
```

Constructs a ManageReferral control.

**Parameters:** criticality

- The control's criticality setting.

---

#### ManageReferralControl

public ManageReferralControl​(boolean criticality)

Constructs a ManageReferral control.

---

