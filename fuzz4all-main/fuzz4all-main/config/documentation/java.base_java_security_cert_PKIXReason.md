# Enum PKIXReason

**Source:** `java.base\java\security\cert\PKIXReason.html`

### Class Description

```java
public enum
PKIXReason

extends
Enum
<
PKIXReason
>
implements
CertPathValidatorException.Reason
```

The

PKIXReason

enumerates the potential PKIX-specific reasons
that an X.509 certification path may be invalid according to the PKIX
(RFC 5280) standard. These reasons are in addition to those of the

CertPathValidatorException.BasicReason

enumeration.

**All Implemented Interfaces:** Serializable

,

Comparable

<

PKIXReason

>

,

CertPathValidatorException.Reason

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
PKIXReason
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PKIXReason c : PKIXReason.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
PKIXReason
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

#### Enum PKIXReason

java.lang.Object

- java.lang.Enum

<

PKIXReason

>
- - java.security.cert.PKIXReason

java.lang.Enum

<

PKIXReason

>

- java.security.cert.PKIXReason

java.security.cert.PKIXReason

**All Implemented Interfaces:** Serializable

,

Comparable

<

PKIXReason

>

,

CertPathValidatorException.Reason

```java
public enum
PKIXReason

extends
Enum
<
PKIXReason
>
implements
CertPathValidatorException.Reason
```

The

PKIXReason

enumerates the potential PKIX-specific reasons
that an X.509 certification path may be invalid according to the PKIX
(RFC 5280) standard. These reasons are in addition to those of the

CertPathValidatorException.BasicReason

enumeration.

**Since:** 1.7

public enum

PKIXReason

extends

Enum

<

PKIXReason

>
implements

CertPathValidatorException.Reason

The

PKIXReason

enumerates the potential PKIX-specific reasons
that an X.509 certification path may be invalid according to the PKIX
(RFC 5280) standard. These reasons are in addition to those of the

CertPathValidatorException.BasicReason

enumeration.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

INVALID_KEY_USAGE

The certificate's key usage is invalid.

INVALID_NAME

The name constraints have been violated.

INVALID_POLICY

The policy constraints have been violated.

NAME_CHAINING

The certificate does not chain correctly.

NO_TRUST_ANCHOR

No acceptable trust anchor found.

NOT_CA_CERT

The certificate is not a CA certificate.

PATH_TOO_LONG

The path length constraint has been violated.

UNRECOGNIZED_CRIT_EXT

The certificate contains one or more unrecognized critical
extensions.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

PKIXReason

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

PKIXReason

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

INVALID_KEY_USAGE

The certificate's key usage is invalid.

INVALID_NAME

The name constraints have been violated.

INVALID_POLICY

The policy constraints have been violated.

NAME_CHAINING

The certificate does not chain correctly.

NO_TRUST_ANCHOR

No acceptable trust anchor found.

NOT_CA_CERT

The certificate is not a CA certificate.

PATH_TOO_LONG

The path length constraint has been violated.

UNRECOGNIZED_CRIT_EXT

The certificate contains one or more unrecognized critical
extensions.

---

#### Enum Constant Summary

The certificate's key usage is invalid.

The name constraints have been violated.

The policy constraints have been violated.

The certificate does not chain correctly.

No acceptable trust anchor found.

The certificate is not a CA certificate.

The path length constraint has been violated.

The certificate contains one or more unrecognized critical
extensions.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

PKIXReason

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

PKIXReason

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

- NAME_CHAINING

```java
public static final
PKIXReason
NAME_CHAINING
```

The certificate does not chain correctly.

- INVALID_KEY_USAGE

```java
public static final
PKIXReason
INVALID_KEY_USAGE
```

The certificate's key usage is invalid.

- INVALID_POLICY

```java
public static final
PKIXReason
INVALID_POLICY
```

The policy constraints have been violated.

- NO_TRUST_ANCHOR

```java
public static final
PKIXReason
NO_TRUST_ANCHOR
```

No acceptable trust anchor found.

- UNRECOGNIZED_CRIT_EXT

```java
public static final
PKIXReason
UNRECOGNIZED_CRIT_EXT
```

The certificate contains one or more unrecognized critical
extensions.

- NOT_CA_CERT

```java
public static final
PKIXReason
NOT_CA_CERT
```

The certificate is not a CA certificate.

- PATH_TOO_LONG

```java
public static final
PKIXReason
PATH_TOO_LONG
```

The path length constraint has been violated.

- INVALID_NAME

```java
public static final
PKIXReason
INVALID_NAME
```

The name constraints have been violated.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
PKIXReason
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PKIXReason c : PKIXReason.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
PKIXReason
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

- NAME_CHAINING

```java
public static final
PKIXReason
NAME_CHAINING
```

The certificate does not chain correctly.

- INVALID_KEY_USAGE

```java
public static final
PKIXReason
INVALID_KEY_USAGE
```

The certificate's key usage is invalid.

- INVALID_POLICY

```java
public static final
PKIXReason
INVALID_POLICY
```

The policy constraints have been violated.

- NO_TRUST_ANCHOR

```java
public static final
PKIXReason
NO_TRUST_ANCHOR
```

No acceptable trust anchor found.

- UNRECOGNIZED_CRIT_EXT

```java
public static final
PKIXReason
UNRECOGNIZED_CRIT_EXT
```

The certificate contains one or more unrecognized critical
extensions.

- NOT_CA_CERT

```java
public static final
PKIXReason
NOT_CA_CERT
```

The certificate is not a CA certificate.

- PATH_TOO_LONG

```java
public static final
PKIXReason
PATH_TOO_LONG
```

The path length constraint has been violated.

- INVALID_NAME

```java
public static final
PKIXReason
INVALID_NAME
```

The name constraints have been violated.

---

#### Enum Constant Detail

NAME_CHAINING

```java
public static final
PKIXReason
NAME_CHAINING
```

The certificate does not chain correctly.

---

#### NAME_CHAINING

public static final

PKIXReason

NAME_CHAINING

The certificate does not chain correctly.

INVALID_KEY_USAGE

```java
public static final
PKIXReason
INVALID_KEY_USAGE
```

The certificate's key usage is invalid.

---

#### INVALID_KEY_USAGE

public static final

PKIXReason

INVALID_KEY_USAGE

The certificate's key usage is invalid.

INVALID_POLICY

```java
public static final
PKIXReason
INVALID_POLICY
```

The policy constraints have been violated.

---

#### INVALID_POLICY

public static final

PKIXReason

INVALID_POLICY

The policy constraints have been violated.

NO_TRUST_ANCHOR

```java
public static final
PKIXReason
NO_TRUST_ANCHOR
```

No acceptable trust anchor found.

---

#### NO_TRUST_ANCHOR

public static final

PKIXReason

NO_TRUST_ANCHOR

No acceptable trust anchor found.

UNRECOGNIZED_CRIT_EXT

```java
public static final
PKIXReason
UNRECOGNIZED_CRIT_EXT
```

The certificate contains one or more unrecognized critical
extensions.

---

#### UNRECOGNIZED_CRIT_EXT

public static final

PKIXReason

UNRECOGNIZED_CRIT_EXT

The certificate contains one or more unrecognized critical
extensions.

NOT_CA_CERT

```java
public static final
PKIXReason
NOT_CA_CERT
```

The certificate is not a CA certificate.

---

#### NOT_CA_CERT

public static final

PKIXReason

NOT_CA_CERT

The certificate is not a CA certificate.

PATH_TOO_LONG

```java
public static final
PKIXReason
PATH_TOO_LONG
```

The path length constraint has been violated.

---

#### PATH_TOO_LONG

public static final

PKIXReason

PATH_TOO_LONG

The path length constraint has been violated.

INVALID_NAME

```java
public static final
PKIXReason
INVALID_NAME
```

The name constraints have been violated.

---

#### INVALID_NAME

public static final

PKIXReason

INVALID_NAME

The name constraints have been violated.

Method Detail

- values

```java
public static
PKIXReason
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PKIXReason c : PKIXReason.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
PKIXReason
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
PKIXReason
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PKIXReason c : PKIXReason.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

PKIXReason

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PKIXReason c : PKIXReason.values())
System.out.println(c);
```

for (PKIXReason c : PKIXReason.values())
System.out.println(c);

valueOf

```java
public static
PKIXReason
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

PKIXReason

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

