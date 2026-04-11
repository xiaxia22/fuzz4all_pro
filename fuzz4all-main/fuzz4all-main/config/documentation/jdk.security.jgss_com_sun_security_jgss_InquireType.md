# Enum InquireType

**Source:** `jdk.security.jgss\com\sun\security\jgss\InquireType.html`

### Class Description

```java
public enum
InquireType

extends
Enum
<
InquireType
>
```

Attribute types that can be specified as an argument of

ExtendedGSSContext.inquireSecContext(com.sun.security.jgss.InquireType)

**All Implemented Interfaces:** Serializable

,

Comparable

<

InquireType

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
InquireType
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (InquireType c : InquireType.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
InquireType
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

#### Enum InquireType

java.lang.Object

- java.lang.Enum

<

InquireType

>
- - com.sun.security.jgss.InquireType

java.lang.Enum

<

InquireType

>

- com.sun.security.jgss.InquireType

com.sun.security.jgss.InquireType

**All Implemented Interfaces:** Serializable

,

Comparable

<

InquireType

>

```java
public enum
InquireType

extends
Enum
<
InquireType
>
```

Attribute types that can be specified as an argument of

ExtendedGSSContext.inquireSecContext(com.sun.security.jgss.InquireType)

public enum

InquireType

extends

Enum

<

InquireType

>

Attribute types that can be specified as an argument of

ExtendedGSSContext.inquireSecContext(com.sun.security.jgss.InquireType)

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

KRB5_GET_AUTHTIME

Attribute type for retrieving the authtime in the service ticket
of an established Kerberos 5 security context.

KRB5_GET_AUTHZ_DATA

Attribute type for retrieving the authorization data in the
service ticket of an established Kerberos 5 security context.

KRB5_GET_KRB_CRED

Attribute type for retrieving the KRB_CRED message that an initiator
is about to send to an acceptor.

KRB5_GET_SESSION_KEY

Deprecated.

as of 9, replaced by

KRB5_GET_SESSION_KEY_EX

which returns an instance of

EncryptionKey

that implements the

SecretKey

interface and
has similar methods with

KerberosKey

.

KRB5_GET_SESSION_KEY_EX

Attribute type for retrieving the session key of an
established Kerberos 5 security context.

KRB5_GET_TKT_FLAGS

Attribute type for retrieving the service ticket flags of an
established Kerberos 5 security context.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

InquireType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

InquireType

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

KRB5_GET_AUTHTIME

Attribute type for retrieving the authtime in the service ticket
of an established Kerberos 5 security context.

KRB5_GET_AUTHZ_DATA

Attribute type for retrieving the authorization data in the
service ticket of an established Kerberos 5 security context.

KRB5_GET_KRB_CRED

Attribute type for retrieving the KRB_CRED message that an initiator
is about to send to an acceptor.

KRB5_GET_SESSION_KEY

Deprecated.

as of 9, replaced by

KRB5_GET_SESSION_KEY_EX

which returns an instance of

EncryptionKey

that implements the

SecretKey

interface and
has similar methods with

KerberosKey

.

KRB5_GET_SESSION_KEY_EX

Attribute type for retrieving the session key of an
established Kerberos 5 security context.

KRB5_GET_TKT_FLAGS

Attribute type for retrieving the service ticket flags of an
established Kerberos 5 security context.

---

#### Enum Constant Summary

Attribute type for retrieving the authtime in the service ticket
of an established Kerberos 5 security context.

Attribute type for retrieving the authorization data in the
service ticket of an established Kerberos 5 security context.

Attribute type for retrieving the KRB_CRED message that an initiator
is about to send to an acceptor.

Deprecated.

as of 9, replaced by

KRB5_GET_SESSION_KEY_EX

which returns an instance of

EncryptionKey

that implements the

SecretKey

interface and
has similar methods with

KerberosKey

.

Attribute type for retrieving the session key of an
established Kerberos 5 security context.

Attribute type for retrieving the service ticket flags of an
established Kerberos 5 security context.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

InquireType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

InquireType

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

- KRB5_GET_SESSION_KEY

```java
@Deprecated

public static final
InquireType
KRB5_GET_SESSION_KEY
```

Deprecated.

as of 9, replaced by

KRB5_GET_SESSION_KEY_EX

which returns an instance of

EncryptionKey

that implements the

SecretKey

interface and
has similar methods with

KerberosKey

.

Attribute type for retrieving the session key of an established
Kerberos 5 security context. The returned object is an instance of

Key

, which has the following properties:

- Algorithm: enctype as a string, where
enctype is defined in RFC 3961, section 8.

Format: "RAW"

Encoded form: the raw key bytes, not in any ASN.1 encoding

- KRB5_GET_SESSION_KEY_EX

```java
public static final
InquireType
KRB5_GET_SESSION_KEY_EX
```

Attribute type for retrieving the session key of an
established Kerberos 5 security context. The return value is an
instance of

EncryptionKey

.

**Since:** 9

- KRB5_GET_TKT_FLAGS

```java
public static final
InquireType
KRB5_GET_TKT_FLAGS
```

Attribute type for retrieving the service ticket flags of an
established Kerberos 5 security context. The returned object is
a boolean array for the service ticket flags, which is long enough
to contain all true bits. This means if the user wants to get the

n

'th bit but the length of the returned array is less than

n

, it is regarded as false.

- KRB5_GET_AUTHZ_DATA

```java
public static final
InquireType
KRB5_GET_AUTHZ_DATA
```

Attribute type for retrieving the authorization data in the
service ticket of an established Kerberos 5 security context.
Only supported on the acceptor side.

- KRB5_GET_AUTHTIME

```java
public static final
InquireType
KRB5_GET_AUTHTIME
```

Attribute type for retrieving the authtime in the service ticket
of an established Kerberos 5 security context. The returned object
is a String object in the standard KerberosTime format defined in
RFC 4120 Section 5.2.3.

- KRB5_GET_KRB_CRED

```java
public static final
InquireType
KRB5_GET_KRB_CRED
```

Attribute type for retrieving the KRB_CRED message that an initiator
is about to send to an acceptor. The return type is an instance of

KerberosCredMessage

.

**Since:** 9

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
InquireType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (InquireType c : InquireType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
InquireType
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

- KRB5_GET_SESSION_KEY

```java
@Deprecated

public static final
InquireType
KRB5_GET_SESSION_KEY
```

Deprecated.

as of 9, replaced by

KRB5_GET_SESSION_KEY_EX

which returns an instance of

EncryptionKey

that implements the

SecretKey

interface and
has similar methods with

KerberosKey

.

Attribute type for retrieving the session key of an established
Kerberos 5 security context. The returned object is an instance of

Key

, which has the following properties:

- Algorithm: enctype as a string, where
enctype is defined in RFC 3961, section 8.

Format: "RAW"

Encoded form: the raw key bytes, not in any ASN.1 encoding

- KRB5_GET_SESSION_KEY_EX

```java
public static final
InquireType
KRB5_GET_SESSION_KEY_EX
```

Attribute type for retrieving the session key of an
established Kerberos 5 security context. The return value is an
instance of

EncryptionKey

.

**Since:** 9

- KRB5_GET_TKT_FLAGS

```java
public static final
InquireType
KRB5_GET_TKT_FLAGS
```

Attribute type for retrieving the service ticket flags of an
established Kerberos 5 security context. The returned object is
a boolean array for the service ticket flags, which is long enough
to contain all true bits. This means if the user wants to get the

n

'th bit but the length of the returned array is less than

n

, it is regarded as false.

- KRB5_GET_AUTHZ_DATA

```java
public static final
InquireType
KRB5_GET_AUTHZ_DATA
```

Attribute type for retrieving the authorization data in the
service ticket of an established Kerberos 5 security context.
Only supported on the acceptor side.

- KRB5_GET_AUTHTIME

```java
public static final
InquireType
KRB5_GET_AUTHTIME
```

Attribute type for retrieving the authtime in the service ticket
of an established Kerberos 5 security context. The returned object
is a String object in the standard KerberosTime format defined in
RFC 4120 Section 5.2.3.

- KRB5_GET_KRB_CRED

```java
public static final
InquireType
KRB5_GET_KRB_CRED
```

Attribute type for retrieving the KRB_CRED message that an initiator
is about to send to an acceptor. The return type is an instance of

KerberosCredMessage

.

**Since:** 9

---

#### Enum Constant Detail

KRB5_GET_SESSION_KEY

```java
@Deprecated

public static final
InquireType
KRB5_GET_SESSION_KEY
```

Deprecated.

as of 9, replaced by

KRB5_GET_SESSION_KEY_EX

which returns an instance of

EncryptionKey

that implements the

SecretKey

interface and
has similar methods with

KerberosKey

.

Attribute type for retrieving the session key of an established
Kerberos 5 security context. The returned object is an instance of

Key

, which has the following properties:

- Algorithm: enctype as a string, where
enctype is defined in RFC 3961, section 8.

Format: "RAW"

Encoded form: the raw key bytes, not in any ASN.1 encoding

---

#### KRB5_GET_SESSION_KEY

@Deprecated

public static final

InquireType

KRB5_GET_SESSION_KEY

Attribute type for retrieving the session key of an established
Kerberos 5 security context. The returned object is an instance of

Key

, which has the following properties:

- Algorithm: enctype as a string, where
enctype is defined in RFC 3961, section 8.

Format: "RAW"

Encoded form: the raw key bytes, not in any ASN.1 encoding

Algorithm: enctype as a string, where
enctype is defined in RFC 3961, section 8.

Format: "RAW"

Encoded form: the raw key bytes, not in any ASN.1 encoding

KRB5_GET_SESSION_KEY_EX

```java
public static final
InquireType
KRB5_GET_SESSION_KEY_EX
```

Attribute type for retrieving the session key of an
established Kerberos 5 security context. The return value is an
instance of

EncryptionKey

.

**Since:** 9

---

#### KRB5_GET_SESSION_KEY_EX

public static final

InquireType

KRB5_GET_SESSION_KEY_EX

Attribute type for retrieving the session key of an
established Kerberos 5 security context. The return value is an
instance of

EncryptionKey

.

KRB5_GET_TKT_FLAGS

```java
public static final
InquireType
KRB5_GET_TKT_FLAGS
```

Attribute type for retrieving the service ticket flags of an
established Kerberos 5 security context. The returned object is
a boolean array for the service ticket flags, which is long enough
to contain all true bits. This means if the user wants to get the

n

'th bit but the length of the returned array is less than

n

, it is regarded as false.

---

#### KRB5_GET_TKT_FLAGS

public static final

InquireType

KRB5_GET_TKT_FLAGS

Attribute type for retrieving the service ticket flags of an
established Kerberos 5 security context. The returned object is
a boolean array for the service ticket flags, which is long enough
to contain all true bits. This means if the user wants to get the

n

'th bit but the length of the returned array is less than

n

, it is regarded as false.

KRB5_GET_AUTHZ_DATA

```java
public static final
InquireType
KRB5_GET_AUTHZ_DATA
```

Attribute type for retrieving the authorization data in the
service ticket of an established Kerberos 5 security context.
Only supported on the acceptor side.

---

#### KRB5_GET_AUTHZ_DATA

public static final

InquireType

KRB5_GET_AUTHZ_DATA

Attribute type for retrieving the authorization data in the
service ticket of an established Kerberos 5 security context.
Only supported on the acceptor side.

KRB5_GET_AUTHTIME

```java
public static final
InquireType
KRB5_GET_AUTHTIME
```

Attribute type for retrieving the authtime in the service ticket
of an established Kerberos 5 security context. The returned object
is a String object in the standard KerberosTime format defined in
RFC 4120 Section 5.2.3.

---

#### KRB5_GET_AUTHTIME

public static final

InquireType

KRB5_GET_AUTHTIME

Attribute type for retrieving the authtime in the service ticket
of an established Kerberos 5 security context. The returned object
is a String object in the standard KerberosTime format defined in
RFC 4120 Section 5.2.3.

KRB5_GET_KRB_CRED

```java
public static final
InquireType
KRB5_GET_KRB_CRED
```

Attribute type for retrieving the KRB_CRED message that an initiator
is about to send to an acceptor. The return type is an instance of

KerberosCredMessage

.

**Since:** 9

---

#### KRB5_GET_KRB_CRED

public static final

InquireType

KRB5_GET_KRB_CRED

Attribute type for retrieving the KRB_CRED message that an initiator
is about to send to an acceptor. The return type is an instance of

KerberosCredMessage

.

Method Detail

- values

```java
public static
InquireType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (InquireType c : InquireType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
InquireType
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
InquireType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (InquireType c : InquireType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

InquireType

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (InquireType c : InquireType.values())
System.out.println(c);
```

for (InquireType c : InquireType.values())
System.out.println(c);

valueOf

```java
public static
InquireType
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

InquireType

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

