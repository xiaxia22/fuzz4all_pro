# Enum PKIXRevocationChecker.Option

**Source:** `java.base\java\security\cert\PKIXRevocationChecker.Option.html`

### Class Description

```java
public static enum
PKIXRevocationChecker.Option

extends
Enum
<
PKIXRevocationChecker.Option
>
```

Various revocation options that can be specified for the revocation
checking mechanism.

**All Implemented Interfaces:** Serializable

,

Comparable

<

PKIXRevocationChecker.Option

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
PKIXRevocationChecker.Option
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PKIXRevocationChecker.Option c : PKIXRevocationChecker.Option.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
PKIXRevocationChecker.Option
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

#### Enum PKIXRevocationChecker.Option

java.lang.Object

- java.lang.Enum

<

PKIXRevocationChecker.Option

>
- - java.security.cert.PKIXRevocationChecker.Option

java.lang.Enum

<

PKIXRevocationChecker.Option

>

- java.security.cert.PKIXRevocationChecker.Option

java.security.cert.PKIXRevocationChecker.Option

**All Implemented Interfaces:** Serializable

,

Comparable

<

PKIXRevocationChecker.Option

>

**Enclosing class:** PKIXRevocationChecker

```java
public static enum
PKIXRevocationChecker.Option

extends
Enum
<
PKIXRevocationChecker.Option
>
```

Various revocation options that can be specified for the revocation
checking mechanism.

public static enum

PKIXRevocationChecker.Option

extends

Enum

<

PKIXRevocationChecker.Option

>

Various revocation options that can be specified for the revocation
checking mechanism.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

NO_FALLBACK

Disable the fallback mechanism.

ONLY_END_ENTITY

Only check the revocation status of end-entity certificates.

PREFER_CRLS

Prefer CRLs to OSCP.

SOFT_FAIL

Allow revocation check to succeed if the revocation status cannot be
determined for one of the following reasons:

The CRL or OCSP response cannot be obtained because of a
network error.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

PKIXRevocationChecker.Option

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

PKIXRevocationChecker.Option

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

NO_FALLBACK

Disable the fallback mechanism.

ONLY_END_ENTITY

Only check the revocation status of end-entity certificates.

PREFER_CRLS

Prefer CRLs to OSCP.

SOFT_FAIL

Allow revocation check to succeed if the revocation status cannot be
determined for one of the following reasons:

The CRL or OCSP response cannot be obtained because of a
network error.

---

#### Enum Constant Summary

Disable the fallback mechanism.

Only check the revocation status of end-entity certificates.

Prefer CRLs to OSCP.

Allow revocation check to succeed if the revocation status cannot be
determined for one of the following reasons:

The CRL or OCSP response cannot be obtained because of a
network error.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

PKIXRevocationChecker.Option

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

PKIXRevocationChecker.Option

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

- ONLY_END_ENTITY

```java
public static final
PKIXRevocationChecker.Option
ONLY_END_ENTITY
```

Only check the revocation status of end-entity certificates.

- PREFER_CRLS

```java
public static final
PKIXRevocationChecker.Option
PREFER_CRLS
```

Prefer CRLs to OSCP. The default behavior is to prefer OCSP. Each
PKIX implementation should document further details of their
specific preference rules and fallback policies.

- NO_FALLBACK

```java
public static final
PKIXRevocationChecker.Option
NO_FALLBACK
```

Disable the fallback mechanism.

- SOFT_FAIL

```java
public static final
PKIXRevocationChecker.Option
SOFT_FAIL
```

Allow revocation check to succeed if the revocation status cannot be
determined for one of the following reasons:

- The CRL or OCSP response cannot be obtained because of a
network error.

The OCSP responder returns one of the following errors
specified in section 2.3 of RFC 2560: internalError or tryLater.

Note that these conditions apply to both OCSP and CRLs, and unless
the

NO_FALLBACK

option is set, the revocation check is
allowed to succeed only if both mechanisms fail under one of the
conditions as stated above.
Exceptions that cause the network errors are ignored but can be
later retrieved by calling the

getSoftFailExceptions

method.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
PKIXRevocationChecker.Option
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PKIXRevocationChecker.Option c : PKIXRevocationChecker.Option.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
PKIXRevocationChecker.Option
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

- ONLY_END_ENTITY

```java
public static final
PKIXRevocationChecker.Option
ONLY_END_ENTITY
```

Only check the revocation status of end-entity certificates.

- PREFER_CRLS

```java
public static final
PKIXRevocationChecker.Option
PREFER_CRLS
```

Prefer CRLs to OSCP. The default behavior is to prefer OCSP. Each
PKIX implementation should document further details of their
specific preference rules and fallback policies.

- NO_FALLBACK

```java
public static final
PKIXRevocationChecker.Option
NO_FALLBACK
```

Disable the fallback mechanism.

- SOFT_FAIL

```java
public static final
PKIXRevocationChecker.Option
SOFT_FAIL
```

Allow revocation check to succeed if the revocation status cannot be
determined for one of the following reasons:

- The CRL or OCSP response cannot be obtained because of a
network error.

The OCSP responder returns one of the following errors
specified in section 2.3 of RFC 2560: internalError or tryLater.

Note that these conditions apply to both OCSP and CRLs, and unless
the

NO_FALLBACK

option is set, the revocation check is
allowed to succeed only if both mechanisms fail under one of the
conditions as stated above.
Exceptions that cause the network errors are ignored but can be
later retrieved by calling the

getSoftFailExceptions

method.

---

#### Enum Constant Detail

ONLY_END_ENTITY

```java
public static final
PKIXRevocationChecker.Option
ONLY_END_ENTITY
```

Only check the revocation status of end-entity certificates.

---

#### ONLY_END_ENTITY

public static final

PKIXRevocationChecker.Option

ONLY_END_ENTITY

Only check the revocation status of end-entity certificates.

PREFER_CRLS

```java
public static final
PKIXRevocationChecker.Option
PREFER_CRLS
```

Prefer CRLs to OSCP. The default behavior is to prefer OCSP. Each
PKIX implementation should document further details of their
specific preference rules and fallback policies.

---

#### PREFER_CRLS

public static final

PKIXRevocationChecker.Option

PREFER_CRLS

Prefer CRLs to OSCP. The default behavior is to prefer OCSP. Each
PKIX implementation should document further details of their
specific preference rules and fallback policies.

NO_FALLBACK

```java
public static final
PKIXRevocationChecker.Option
NO_FALLBACK
```

Disable the fallback mechanism.

---

#### NO_FALLBACK

public static final

PKIXRevocationChecker.Option

NO_FALLBACK

Disable the fallback mechanism.

SOFT_FAIL

```java
public static final
PKIXRevocationChecker.Option
SOFT_FAIL
```

Allow revocation check to succeed if the revocation status cannot be
determined for one of the following reasons:

- The CRL or OCSP response cannot be obtained because of a
network error.

The OCSP responder returns one of the following errors
specified in section 2.3 of RFC 2560: internalError or tryLater.

Note that these conditions apply to both OCSP and CRLs, and unless
the

NO_FALLBACK

option is set, the revocation check is
allowed to succeed only if both mechanisms fail under one of the
conditions as stated above.
Exceptions that cause the network errors are ignored but can be
later retrieved by calling the

getSoftFailExceptions

method.

---

#### SOFT_FAIL

public static final

PKIXRevocationChecker.Option

SOFT_FAIL

Allow revocation check to succeed if the revocation status cannot be
determined for one of the following reasons:

- The CRL or OCSP response cannot be obtained because of a
network error.

The OCSP responder returns one of the following errors
specified in section 2.3 of RFC 2560: internalError or tryLater.

Note that these conditions apply to both OCSP and CRLs, and unless
the

NO_FALLBACK

option is set, the revocation check is
allowed to succeed only if both mechanisms fail under one of the
conditions as stated above.
Exceptions that cause the network errors are ignored but can be
later retrieved by calling the

getSoftFailExceptions

method.

The CRL or OCSP response cannot be obtained because of a
network error.

The OCSP responder returns one of the following errors
specified in section 2.3 of RFC 2560: internalError or tryLater.

Method Detail

- values

```java
public static
PKIXRevocationChecker.Option
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PKIXRevocationChecker.Option c : PKIXRevocationChecker.Option.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
PKIXRevocationChecker.Option
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
PKIXRevocationChecker.Option
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PKIXRevocationChecker.Option c : PKIXRevocationChecker.Option.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

PKIXRevocationChecker.Option

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PKIXRevocationChecker.Option c : PKIXRevocationChecker.Option.values())
System.out.println(c);
```

for (PKIXRevocationChecker.Option c : PKIXRevocationChecker.Option.values())
System.out.println(c);

valueOf

```java
public static
PKIXRevocationChecker.Option
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

PKIXRevocationChecker.Option

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

