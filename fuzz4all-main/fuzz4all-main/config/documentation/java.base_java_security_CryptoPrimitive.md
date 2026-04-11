# Enum CryptoPrimitive

**Source:** `java.base\java\security\CryptoPrimitive.html`

### Class Description

```java
public enum
CryptoPrimitive

extends
Enum
<
CryptoPrimitive
>
```

An enumeration of cryptographic primitives.

**All Implemented Interfaces:** Serializable

,

Comparable

<

CryptoPrimitive

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
CryptoPrimitive
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CryptoPrimitive c : CryptoPrimitive.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
CryptoPrimitive
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

#### Enum CryptoPrimitive

java.lang.Object

- java.lang.Enum

<

CryptoPrimitive

>
- - java.security.CryptoPrimitive

java.lang.Enum

<

CryptoPrimitive

>

- java.security.CryptoPrimitive

java.security.CryptoPrimitive

**All Implemented Interfaces:** Serializable

,

Comparable

<

CryptoPrimitive

>

```java
public enum
CryptoPrimitive

extends
Enum
<
CryptoPrimitive
>
```

An enumeration of cryptographic primitives.

**Since:** 1.7

public enum

CryptoPrimitive

extends

Enum

<

CryptoPrimitive

>

An enumeration of cryptographic primitives.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

BLOCK_CIPHER

Symmetric primitive: block cipher

KEY_AGREEMENT

Asymmetric primitive: key agreement and key distribution

KEY_ENCAPSULATION

Asymmetric primitive: key encapsulation mechanism

KEY_WRAP

Symmetric primitive: key wrap

MAC

Symmetric primitive: message authentication code

MESSAGE_DIGEST

Hash function

PUBLIC_KEY_ENCRYPTION

Asymmetric primitive: public key encryption

SECURE_RANDOM

Cryptographic random number generator

SIGNATURE

Asymmetric primitive: signature scheme

STREAM_CIPHER

Symmetric primitive: stream cipher

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

CryptoPrimitive

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

CryptoPrimitive

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

BLOCK_CIPHER

Symmetric primitive: block cipher

KEY_AGREEMENT

Asymmetric primitive: key agreement and key distribution

KEY_ENCAPSULATION

Asymmetric primitive: key encapsulation mechanism

KEY_WRAP

Symmetric primitive: key wrap

MAC

Symmetric primitive: message authentication code

MESSAGE_DIGEST

Hash function

PUBLIC_KEY_ENCRYPTION

Asymmetric primitive: public key encryption

SECURE_RANDOM

Cryptographic random number generator

SIGNATURE

Asymmetric primitive: signature scheme

STREAM_CIPHER

Symmetric primitive: stream cipher

---

#### Enum Constant Summary

Symmetric primitive: block cipher

Asymmetric primitive: key agreement and key distribution

Asymmetric primitive: key encapsulation mechanism

Symmetric primitive: key wrap

Symmetric primitive: message authentication code

Hash function

Asymmetric primitive: public key encryption

Cryptographic random number generator

Asymmetric primitive: signature scheme

Symmetric primitive: stream cipher

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

CryptoPrimitive

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

CryptoPrimitive

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

- MESSAGE_DIGEST

```java
public static final
CryptoPrimitive
MESSAGE_DIGEST
```

Hash function

- SECURE_RANDOM

```java
public static final
CryptoPrimitive
SECURE_RANDOM
```

Cryptographic random number generator

- BLOCK_CIPHER

```java
public static final
CryptoPrimitive
BLOCK_CIPHER
```

Symmetric primitive: block cipher

- STREAM_CIPHER

```java
public static final
CryptoPrimitive
STREAM_CIPHER
```

Symmetric primitive: stream cipher

- MAC

```java
public static final
CryptoPrimitive
MAC
```

Symmetric primitive: message authentication code

- KEY_WRAP

```java
public static final
CryptoPrimitive
KEY_WRAP
```

Symmetric primitive: key wrap

- PUBLIC_KEY_ENCRYPTION

```java
public static final
CryptoPrimitive
PUBLIC_KEY_ENCRYPTION
```

Asymmetric primitive: public key encryption

- SIGNATURE

```java
public static final
CryptoPrimitive
SIGNATURE
```

Asymmetric primitive: signature scheme

- KEY_ENCAPSULATION

```java
public static final
CryptoPrimitive
KEY_ENCAPSULATION
```

Asymmetric primitive: key encapsulation mechanism

- KEY_AGREEMENT

```java
public static final
CryptoPrimitive
KEY_AGREEMENT
```

Asymmetric primitive: key agreement and key distribution

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
CryptoPrimitive
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CryptoPrimitive c : CryptoPrimitive.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
CryptoPrimitive
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

- MESSAGE_DIGEST

```java
public static final
CryptoPrimitive
MESSAGE_DIGEST
```

Hash function

- SECURE_RANDOM

```java
public static final
CryptoPrimitive
SECURE_RANDOM
```

Cryptographic random number generator

- BLOCK_CIPHER

```java
public static final
CryptoPrimitive
BLOCK_CIPHER
```

Symmetric primitive: block cipher

- STREAM_CIPHER

```java
public static final
CryptoPrimitive
STREAM_CIPHER
```

Symmetric primitive: stream cipher

- MAC

```java
public static final
CryptoPrimitive
MAC
```

Symmetric primitive: message authentication code

- KEY_WRAP

```java
public static final
CryptoPrimitive
KEY_WRAP
```

Symmetric primitive: key wrap

- PUBLIC_KEY_ENCRYPTION

```java
public static final
CryptoPrimitive
PUBLIC_KEY_ENCRYPTION
```

Asymmetric primitive: public key encryption

- SIGNATURE

```java
public static final
CryptoPrimitive
SIGNATURE
```

Asymmetric primitive: signature scheme

- KEY_ENCAPSULATION

```java
public static final
CryptoPrimitive
KEY_ENCAPSULATION
```

Asymmetric primitive: key encapsulation mechanism

- KEY_AGREEMENT

```java
public static final
CryptoPrimitive
KEY_AGREEMENT
```

Asymmetric primitive: key agreement and key distribution

---

#### Enum Constant Detail

MESSAGE_DIGEST

```java
public static final
CryptoPrimitive
MESSAGE_DIGEST
```

Hash function

---

#### MESSAGE_DIGEST

public static final

CryptoPrimitive

MESSAGE_DIGEST

Hash function

SECURE_RANDOM

```java
public static final
CryptoPrimitive
SECURE_RANDOM
```

Cryptographic random number generator

---

#### SECURE_RANDOM

public static final

CryptoPrimitive

SECURE_RANDOM

Cryptographic random number generator

BLOCK_CIPHER

```java
public static final
CryptoPrimitive
BLOCK_CIPHER
```

Symmetric primitive: block cipher

---

#### BLOCK_CIPHER

public static final

CryptoPrimitive

BLOCK_CIPHER

Symmetric primitive: block cipher

STREAM_CIPHER

```java
public static final
CryptoPrimitive
STREAM_CIPHER
```

Symmetric primitive: stream cipher

---

#### STREAM_CIPHER

public static final

CryptoPrimitive

STREAM_CIPHER

Symmetric primitive: stream cipher

MAC

```java
public static final
CryptoPrimitive
MAC
```

Symmetric primitive: message authentication code

---

#### MAC

public static final

CryptoPrimitive

MAC

Symmetric primitive: message authentication code

KEY_WRAP

```java
public static final
CryptoPrimitive
KEY_WRAP
```

Symmetric primitive: key wrap

---

#### KEY_WRAP

public static final

CryptoPrimitive

KEY_WRAP

Symmetric primitive: key wrap

PUBLIC_KEY_ENCRYPTION

```java
public static final
CryptoPrimitive
PUBLIC_KEY_ENCRYPTION
```

Asymmetric primitive: public key encryption

---

#### PUBLIC_KEY_ENCRYPTION

public static final

CryptoPrimitive

PUBLIC_KEY_ENCRYPTION

Asymmetric primitive: public key encryption

SIGNATURE

```java
public static final
CryptoPrimitive
SIGNATURE
```

Asymmetric primitive: signature scheme

---

#### SIGNATURE

public static final

CryptoPrimitive

SIGNATURE

Asymmetric primitive: signature scheme

KEY_ENCAPSULATION

```java
public static final
CryptoPrimitive
KEY_ENCAPSULATION
```

Asymmetric primitive: key encapsulation mechanism

---

#### KEY_ENCAPSULATION

public static final

CryptoPrimitive

KEY_ENCAPSULATION

Asymmetric primitive: key encapsulation mechanism

KEY_AGREEMENT

```java
public static final
CryptoPrimitive
KEY_AGREEMENT
```

Asymmetric primitive: key agreement and key distribution

---

#### KEY_AGREEMENT

public static final

CryptoPrimitive

KEY_AGREEMENT

Asymmetric primitive: key agreement and key distribution

Method Detail

- values

```java
public static
CryptoPrimitive
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CryptoPrimitive c : CryptoPrimitive.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
CryptoPrimitive
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
CryptoPrimitive
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CryptoPrimitive c : CryptoPrimitive.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

CryptoPrimitive

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CryptoPrimitive c : CryptoPrimitive.values())
System.out.println(c);
```

for (CryptoPrimitive c : CryptoPrimitive.values())
System.out.println(c);

valueOf

```java
public static
CryptoPrimitive
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

CryptoPrimitive

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

