# Enum CRLReason

**Source:** `java.base\java\security\cert\CRLReason.html`

### Class Description

```java
public enum
CRLReason

extends
Enum
<
CRLReason
>
```

The CRLReason enumeration specifies the reason that a certificate
is revoked, as defined in

RFC 5280: Internet X.509 Public Key Infrastructure Certificate and CRL
Profile

.

**All Implemented Interfaces:** Serializable

,

Comparable

<

CRLReason

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
CRLReason
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CRLReason c : CRLReason.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
CRLReason
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

### Additional Sections

#### Enum CRLReason

java.lang.Object

- java.lang.Enum

<

CRLReason

>
- - java.security.cert.CRLReason

java.lang.Enum

<

CRLReason

>

- java.security.cert.CRLReason

java.security.cert.CRLReason

**All Implemented Interfaces:** Serializable

,

Comparable

<

CRLReason

>

```java
public enum
CRLReason

extends
Enum
<
CRLReason
>
```

The CRLReason enumeration specifies the reason that a certificate
is revoked, as defined in

RFC 5280: Internet X.509 Public Key Infrastructure Certificate and CRL
Profile

.

**Since:** 1.7
**See Also:** X509CRLEntry.getRevocationReason()

,

CertificateRevokedException.getRevocationReason()

public enum

CRLReason

extends

Enum

<

CRLReason

>

The CRLReason enumeration specifies the reason that a certificate
is revoked, as defined in

RFC 5280: Internet X.509 Public Key Infrastructure Certificate and CRL
Profile

.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

AA_COMPROMISE

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised.

AFFILIATION_CHANGED

This reason indicates that the subject's name or other information
has changed.

CA_COMPROMISE

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised.

CERTIFICATE_HOLD

This reason indicates that the certificate has been put on hold.

CESSATION_OF_OPERATION

This reason indicates that the certificate is no longer needed.

KEY_COMPROMISE

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised.

PRIVILEGE_WITHDRAWN

This reason indicates that the privileges granted to the subject of
the certificate have been withdrawn.

REMOVE_FROM_CRL

This reason indicates that the certificate was previously on hold
and should be removed from the CRL.

SUPERSEDED

This reason indicates that the certificate has been superseded.

UNSPECIFIED

This reason indicates that it is unspecified as to why the
certificate has been revoked.

UNUSED

Unused reason.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

CRLReason

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

CRLReason

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Enum Constant Summary

Enum Constants

Enum Constant

Description

AA_COMPROMISE

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised.

AFFILIATION_CHANGED

This reason indicates that the subject's name or other information
has changed.

CA_COMPROMISE

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised.

CERTIFICATE_HOLD

This reason indicates that the certificate has been put on hold.

CESSATION_OF_OPERATION

This reason indicates that the certificate is no longer needed.

KEY_COMPROMISE

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised.

PRIVILEGE_WITHDRAWN

This reason indicates that the privileges granted to the subject of
the certificate have been withdrawn.

REMOVE_FROM_CRL

This reason indicates that the certificate was previously on hold
and should be removed from the CRL.

SUPERSEDED

This reason indicates that the certificate has been superseded.

UNSPECIFIED

This reason indicates that it is unspecified as to why the
certificate has been revoked.

UNUSED

Unused reason.

---

#### Enum Constant Summary

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised.

This reason indicates that the subject's name or other information
has changed.

This reason indicates that the certificate has been put on hold.

This reason indicates that the certificate is no longer needed.

This reason indicates that the privileges granted to the subject of
the certificate have been withdrawn.

This reason indicates that the certificate was previously on hold
and should be removed from the CRL.

This reason indicates that the certificate has been superseded.

This reason indicates that it is unspecified as to why the
certificate has been revoked.

Unused reason.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

CRLReason

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

CRLReason

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- UNSPECIFIED

```java
public static final
CRLReason
UNSPECIFIED
```

This reason indicates that it is unspecified as to why the
certificate has been revoked.

- KEY_COMPROMISE

```java
public static final
CRLReason
KEY_COMPROMISE
```

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised. It applies
to end-entity certificates only.

- CA_COMPROMISE

```java
public static final
CRLReason
CA_COMPROMISE
```

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised. It applies
to certificate authority (CA) certificates only.

- AFFILIATION_CHANGED

```java
public static final
CRLReason
AFFILIATION_CHANGED
```

This reason indicates that the subject's name or other information
has changed.

- SUPERSEDED

```java
public static final
CRLReason
SUPERSEDED
```

This reason indicates that the certificate has been superseded.

- CESSATION_OF_OPERATION

```java
public static final
CRLReason
CESSATION_OF_OPERATION
```

This reason indicates that the certificate is no longer needed.

- CERTIFICATE_HOLD

```java
public static final
CRLReason
CERTIFICATE_HOLD
```

This reason indicates that the certificate has been put on hold.

- UNUSED

```java
public static final
CRLReason
UNUSED
```

Unused reason.

- REMOVE_FROM_CRL

```java
public static final
CRLReason
REMOVE_FROM_CRL
```

This reason indicates that the certificate was previously on hold
and should be removed from the CRL. It is for use with delta CRLs.

- PRIVILEGE_WITHDRAWN

```java
public static final
CRLReason
PRIVILEGE_WITHDRAWN
```

This reason indicates that the privileges granted to the subject of
the certificate have been withdrawn.

- AA_COMPROMISE

```java
public static final
CRLReason
AA_COMPROMISE
```

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised. It applies
to authority attribute (AA) certificates only.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
CRLReason
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CRLReason c : CRLReason.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
CRLReason
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

Enum Constant Detail

- UNSPECIFIED

```java
public static final
CRLReason
UNSPECIFIED
```

This reason indicates that it is unspecified as to why the
certificate has been revoked.

- KEY_COMPROMISE

```java
public static final
CRLReason
KEY_COMPROMISE
```

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised. It applies
to end-entity certificates only.

- CA_COMPROMISE

```java
public static final
CRLReason
CA_COMPROMISE
```

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised. It applies
to certificate authority (CA) certificates only.

- AFFILIATION_CHANGED

```java
public static final
CRLReason
AFFILIATION_CHANGED
```

This reason indicates that the subject's name or other information
has changed.

- SUPERSEDED

```java
public static final
CRLReason
SUPERSEDED
```

This reason indicates that the certificate has been superseded.

- CESSATION_OF_OPERATION

```java
public static final
CRLReason
CESSATION_OF_OPERATION
```

This reason indicates that the certificate is no longer needed.

- CERTIFICATE_HOLD

```java
public static final
CRLReason
CERTIFICATE_HOLD
```

This reason indicates that the certificate has been put on hold.

- UNUSED

```java
public static final
CRLReason
UNUSED
```

Unused reason.

- REMOVE_FROM_CRL

```java
public static final
CRLReason
REMOVE_FROM_CRL
```

This reason indicates that the certificate was previously on hold
and should be removed from the CRL. It is for use with delta CRLs.

- PRIVILEGE_WITHDRAWN

```java
public static final
CRLReason
PRIVILEGE_WITHDRAWN
```

This reason indicates that the privileges granted to the subject of
the certificate have been withdrawn.

- AA_COMPROMISE

```java
public static final
CRLReason
AA_COMPROMISE
```

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised. It applies
to authority attribute (AA) certificates only.

---

#### Enum Constant Detail

UNSPECIFIED

```java
public static final
CRLReason
UNSPECIFIED
```

This reason indicates that it is unspecified as to why the
certificate has been revoked.

---

#### UNSPECIFIED

public static final

CRLReason

UNSPECIFIED

This reason indicates that it is unspecified as to why the
certificate has been revoked.

KEY_COMPROMISE

```java
public static final
CRLReason
KEY_COMPROMISE
```

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised. It applies
to end-entity certificates only.

---

#### KEY_COMPROMISE

public static final

CRLReason

KEY_COMPROMISE

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised. It applies
to end-entity certificates only.

CA_COMPROMISE

```java
public static final
CRLReason
CA_COMPROMISE
```

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised. It applies
to certificate authority (CA) certificates only.

---

#### CA_COMPROMISE

public static final

CRLReason

CA_COMPROMISE

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised. It applies
to certificate authority (CA) certificates only.

AFFILIATION_CHANGED

```java
public static final
CRLReason
AFFILIATION_CHANGED
```

This reason indicates that the subject's name or other information
has changed.

---

#### AFFILIATION_CHANGED

public static final

CRLReason

AFFILIATION_CHANGED

This reason indicates that the subject's name or other information
has changed.

SUPERSEDED

```java
public static final
CRLReason
SUPERSEDED
```

This reason indicates that the certificate has been superseded.

---

#### SUPERSEDED

public static final

CRLReason

SUPERSEDED

This reason indicates that the certificate has been superseded.

CESSATION_OF_OPERATION

```java
public static final
CRLReason
CESSATION_OF_OPERATION
```

This reason indicates that the certificate is no longer needed.

---

#### CESSATION_OF_OPERATION

public static final

CRLReason

CESSATION_OF_OPERATION

This reason indicates that the certificate is no longer needed.

CERTIFICATE_HOLD

```java
public static final
CRLReason
CERTIFICATE_HOLD
```

This reason indicates that the certificate has been put on hold.

---

#### CERTIFICATE_HOLD

public static final

CRLReason

CERTIFICATE_HOLD

This reason indicates that the certificate has been put on hold.

UNUSED

```java
public static final
CRLReason
UNUSED
```

Unused reason.

---

#### UNUSED

public static final

CRLReason

UNUSED

Unused reason.

REMOVE_FROM_CRL

```java
public static final
CRLReason
REMOVE_FROM_CRL
```

This reason indicates that the certificate was previously on hold
and should be removed from the CRL. It is for use with delta CRLs.

---

#### REMOVE_FROM_CRL

public static final

CRLReason

REMOVE_FROM_CRL

This reason indicates that the certificate was previously on hold
and should be removed from the CRL. It is for use with delta CRLs.

PRIVILEGE_WITHDRAWN

```java
public static final
CRLReason
PRIVILEGE_WITHDRAWN
```

This reason indicates that the privileges granted to the subject of
the certificate have been withdrawn.

---

#### PRIVILEGE_WITHDRAWN

public static final

CRLReason

PRIVILEGE_WITHDRAWN

This reason indicates that the privileges granted to the subject of
the certificate have been withdrawn.

AA_COMPROMISE

```java
public static final
CRLReason
AA_COMPROMISE
```

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised. It applies
to authority attribute (AA) certificates only.

---

#### AA_COMPROMISE

public static final

CRLReason

AA_COMPROMISE

This reason indicates that it is known or suspected that the
certificate subject's private key has been compromised. It applies
to authority attribute (AA) certificates only.

Method Detail

- values

```java
public static
CRLReason
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CRLReason c : CRLReason.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
CRLReason
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### Method Detail

values

```java
public static
CRLReason
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CRLReason c : CRLReason.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

CRLReason

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CRLReason c : CRLReason.values())
System.out.println(c);
```

for (CRLReason c : CRLReason.values())
System.out.println(c);

valueOf

```java
public static
CRLReason
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

CRLReason

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

---

