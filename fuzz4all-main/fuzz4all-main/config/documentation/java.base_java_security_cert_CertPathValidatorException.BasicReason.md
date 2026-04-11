# Enum CertPathValidatorException.BasicReason

**Source:** `java.base\java\security\cert\CertPathValidatorException.BasicReason.html`

### Class Description

```java
public static enum
CertPathValidatorException.BasicReason

extends
Enum
<
CertPathValidatorException.BasicReason
>
implements
CertPathValidatorException.Reason
```

The BasicReason enumerates the potential reasons that a certification
path of any type may be invalid.

**All Implemented Interfaces:** Serializable

,

Comparable

<

CertPathValidatorException.BasicReason

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
CertPathValidatorException.BasicReason
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CertPathValidatorException.BasicReason c : CertPathValidatorException.BasicReason.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
CertPathValidatorException.BasicReason
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

#### Enum CertPathValidatorException.BasicReason

java.lang.Object

- java.lang.Enum

<

CertPathValidatorException.BasicReason

>
- - java.security.cert.CertPathValidatorException.BasicReason

java.lang.Enum

<

CertPathValidatorException.BasicReason

>

- java.security.cert.CertPathValidatorException.BasicReason

java.security.cert.CertPathValidatorException.BasicReason

**All Implemented Interfaces:** Serializable

,

Comparable

<

CertPathValidatorException.BasicReason

>

,

CertPathValidatorException.Reason

**Enclosing class:** CertPathValidatorException

```java
public static enum
CertPathValidatorException.BasicReason

extends
Enum
<
CertPathValidatorException.BasicReason
>
implements
CertPathValidatorException.Reason
```

The BasicReason enumerates the potential reasons that a certification
path of any type may be invalid.

**Since:** 1.7

public static enum

CertPathValidatorException.BasicReason

extends

Enum

<

CertPathValidatorException.BasicReason

>
implements

CertPathValidatorException.Reason

The BasicReason enumerates the potential reasons that a certification
path of any type may be invalid.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ALGORITHM_CONSTRAINED

The public key or the signature algorithm has been constrained.

EXPIRED

The certificate is expired.

INVALID_SIGNATURE

The signature is invalid.

NOT_YET_VALID

The certificate is not yet valid.

REVOKED

The certificate is revoked.

UNDETERMINED_REVOCATION_STATUS

The revocation status of the certificate could not be determined.

UNSPECIFIED

Unspecified reason.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

CertPathValidatorException.BasicReason

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

CertPathValidatorException.BasicReason

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

ALGORITHM_CONSTRAINED

The public key or the signature algorithm has been constrained.

EXPIRED

The certificate is expired.

INVALID_SIGNATURE

The signature is invalid.

NOT_YET_VALID

The certificate is not yet valid.

REVOKED

The certificate is revoked.

UNDETERMINED_REVOCATION_STATUS

The revocation status of the certificate could not be determined.

UNSPECIFIED

Unspecified reason.

---

#### Enum Constant Summary

The public key or the signature algorithm has been constrained.

The certificate is expired.

The signature is invalid.

The certificate is not yet valid.

The certificate is revoked.

The revocation status of the certificate could not be determined.

Unspecified reason.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

CertPathValidatorException.BasicReason

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

CertPathValidatorException.BasicReason

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
CertPathValidatorException.BasicReason
UNSPECIFIED
```

Unspecified reason.

- EXPIRED

```java
public static final
CertPathValidatorException.BasicReason
EXPIRED
```

The certificate is expired.

- NOT_YET_VALID

```java
public static final
CertPathValidatorException.BasicReason
NOT_YET_VALID
```

The certificate is not yet valid.

- REVOKED

```java
public static final
CertPathValidatorException.BasicReason
REVOKED
```

The certificate is revoked.

- UNDETERMINED_REVOCATION_STATUS

```java
public static final
CertPathValidatorException.BasicReason
UNDETERMINED_REVOCATION_STATUS
```

The revocation status of the certificate could not be determined.

- INVALID_SIGNATURE

```java
public static final
CertPathValidatorException.BasicReason
INVALID_SIGNATURE
```

The signature is invalid.

- ALGORITHM_CONSTRAINED

```java
public static final
CertPathValidatorException.BasicReason
ALGORITHM_CONSTRAINED
```

The public key or the signature algorithm has been constrained.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
CertPathValidatorException.BasicReason
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CertPathValidatorException.BasicReason c : CertPathValidatorException.BasicReason.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
CertPathValidatorException.BasicReason
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
CertPathValidatorException.BasicReason
UNSPECIFIED
```

Unspecified reason.

- EXPIRED

```java
public static final
CertPathValidatorException.BasicReason
EXPIRED
```

The certificate is expired.

- NOT_YET_VALID

```java
public static final
CertPathValidatorException.BasicReason
NOT_YET_VALID
```

The certificate is not yet valid.

- REVOKED

```java
public static final
CertPathValidatorException.BasicReason
REVOKED
```

The certificate is revoked.

- UNDETERMINED_REVOCATION_STATUS

```java
public static final
CertPathValidatorException.BasicReason
UNDETERMINED_REVOCATION_STATUS
```

The revocation status of the certificate could not be determined.

- INVALID_SIGNATURE

```java
public static final
CertPathValidatorException.BasicReason
INVALID_SIGNATURE
```

The signature is invalid.

- ALGORITHM_CONSTRAINED

```java
public static final
CertPathValidatorException.BasicReason
ALGORITHM_CONSTRAINED
```

The public key or the signature algorithm has been constrained.

---

#### Enum Constant Detail

UNSPECIFIED

```java
public static final
CertPathValidatorException.BasicReason
UNSPECIFIED
```

Unspecified reason.

---

#### UNSPECIFIED

public static final

CertPathValidatorException.BasicReason

UNSPECIFIED

Unspecified reason.

EXPIRED

```java
public static final
CertPathValidatorException.BasicReason
EXPIRED
```

The certificate is expired.

---

#### EXPIRED

public static final

CertPathValidatorException.BasicReason

EXPIRED

The certificate is expired.

NOT_YET_VALID

```java
public static final
CertPathValidatorException.BasicReason
NOT_YET_VALID
```

The certificate is not yet valid.

---

#### NOT_YET_VALID

public static final

CertPathValidatorException.BasicReason

NOT_YET_VALID

The certificate is not yet valid.

REVOKED

```java
public static final
CertPathValidatorException.BasicReason
REVOKED
```

The certificate is revoked.

---

#### REVOKED

public static final

CertPathValidatorException.BasicReason

REVOKED

The certificate is revoked.

UNDETERMINED_REVOCATION_STATUS

```java
public static final
CertPathValidatorException.BasicReason
UNDETERMINED_REVOCATION_STATUS
```

The revocation status of the certificate could not be determined.

---

#### UNDETERMINED_REVOCATION_STATUS

public static final

CertPathValidatorException.BasicReason

UNDETERMINED_REVOCATION_STATUS

The revocation status of the certificate could not be determined.

INVALID_SIGNATURE

```java
public static final
CertPathValidatorException.BasicReason
INVALID_SIGNATURE
```

The signature is invalid.

---

#### INVALID_SIGNATURE

public static final

CertPathValidatorException.BasicReason

INVALID_SIGNATURE

The signature is invalid.

ALGORITHM_CONSTRAINED

```java
public static final
CertPathValidatorException.BasicReason
ALGORITHM_CONSTRAINED
```

The public key or the signature algorithm has been constrained.

---

#### ALGORITHM_CONSTRAINED

public static final

CertPathValidatorException.BasicReason

ALGORITHM_CONSTRAINED

The public key or the signature algorithm has been constrained.

Method Detail

- values

```java
public static
CertPathValidatorException.BasicReason
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CertPathValidatorException.BasicReason c : CertPathValidatorException.BasicReason.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
CertPathValidatorException.BasicReason
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
CertPathValidatorException.BasicReason
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CertPathValidatorException.BasicReason c : CertPathValidatorException.BasicReason.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

CertPathValidatorException.BasicReason

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CertPathValidatorException.BasicReason c : CertPathValidatorException.BasicReason.values())
System.out.println(c);
```

for (CertPathValidatorException.BasicReason c : CertPathValidatorException.BasicReason.values())
System.out.println(c);

valueOf

```java
public static
CertPathValidatorException.BasicReason
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

CertPathValidatorException.BasicReason

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

