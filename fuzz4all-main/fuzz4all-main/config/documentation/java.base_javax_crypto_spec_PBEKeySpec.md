# Class PBEKeySpec

**Source:** `java.base\javax\crypto\spec\PBEKeySpec.html`

### Class Description

```java
public class
PBEKeySpec

extends
Object

implements
KeySpec
```

A user-chosen password that can be used with password-based encryption
(

PBE

).

The password can be viewed as some kind of raw key material, from which
the encryption mechanism that uses it derives a cryptographic key.

Different PBE mechanisms may consume different bits of each password
character. For example, the PBE mechanism defined in

PKCS #5

looks at only the low order 8 bits of each character, whereas
PKCS #12 looks at all 16 bits of each character.

You convert the password characters to a PBE key by creating an
instance of the appropriate secret-key factory. For example, a secret-key
factory for PKCS #5 will construct a PBE key from only the low order 8 bits
of each password character, whereas a secret-key factory for PKCS #12 will
take all 16 bits of each character.

Also note that this class stores passwords as char arrays instead of

String

objects (which would seem more logical), because the
String class is immutable and there is no way to overwrite its
internal value when the password stored in it is no longer needed. Hence,
this class requests the password as a char array, so it can be overwritten
when done.

**All Implemented Interfaces:** KeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public PBEKeySpec​(char[] password)

Constructor that takes a password. An empty char[] is used if
null is specified.

Note:

password

is cloned before it is stored in
the new

PBEKeySpec

object.

**Parameters:**
- password

- the password.

---

#### public PBEKeySpec​(char[] password,
byte[] salt,
int iterationCount,
int keyLength)

Constructor that takes a password, salt, iteration count, and
to-be-derived key length for generating PBEKey of variable-key-size
PBE ciphers. An empty char[] is used if null is specified for

password

.

Note: the

password

and

salt

are cloned before they are stored in
the new

PBEKeySpec

object.

**Parameters:**
- password

- the password.
- salt

- the salt.
- iterationCount

- the iteration count.
- keyLength

- the to-be-derived key length.

**Throws:**
- NullPointerException

- if

salt

is null.
- IllegalArgumentException

- if

salt

is empty,
i.e. 0-length,

iterationCount

or

keyLength

is not positive.

---

#### public PBEKeySpec​(char[] password,
byte[] salt,
int iterationCount)

Constructor that takes a password, salt, iteration count for
generating PBEKey of fixed-key-size PBE ciphers. An empty
char[] is used if null is specified for

password

.

Note: the

password

and

salt

are cloned before they are stored in the new

PBEKeySpec

object.

**Parameters:**
- password

- the password.
- salt

- the salt.
- iterationCount

- the iteration count.

**Throws:**
- NullPointerException

- if

salt

is null.
- IllegalArgumentException

- if

salt

is empty,
i.e. 0-length, or

iterationCount

is not positive.

---

### Method Details

#### public final void clearPassword()

Clears the internal copy of the password.

---

#### public final char[] getPassword()

Returns a copy of the password.

Note: this method returns a copy of the password. It is
the caller's responsibility to zero out the password information after
it is no longer needed.

**Returns:**
- the password.

**Throws:**
- IllegalStateException

- if password has been cleared by
calling

clearPassword

method.

---

#### public final byte[] getSalt()

Returns a copy of the salt or null if not specified.

Note: this method should return a copy of the salt. It is
the caller's responsibility to zero out the salt information after
it is no longer needed.

**Returns:**
- the salt.

---

#### public final int getIterationCount()

Returns the iteration count or 0 if not specified.

**Returns:**
- the iteration count.

---

#### public final int getKeyLength()

Returns the to-be-derived key length or 0 if not specified.

Note: this is used to indicate the preference on key length
for variable-key-size ciphers. The actual key size depends on
each provider's implementation.

**Returns:**
- the to-be-derived key length.

---

### Additional Sections

#### Class PBEKeySpec

java.lang.Object

- javax.crypto.spec.PBEKeySpec

javax.crypto.spec.PBEKeySpec

**All Implemented Interfaces:** KeySpec

```java
public class
PBEKeySpec

extends
Object

implements
KeySpec
```

A user-chosen password that can be used with password-based encryption
(

PBE

).

The password can be viewed as some kind of raw key material, from which
the encryption mechanism that uses it derives a cryptographic key.

Different PBE mechanisms may consume different bits of each password
character. For example, the PBE mechanism defined in

PKCS #5

looks at only the low order 8 bits of each character, whereas
PKCS #12 looks at all 16 bits of each character.

You convert the password characters to a PBE key by creating an
instance of the appropriate secret-key factory. For example, a secret-key
factory for PKCS #5 will construct a PBE key from only the low order 8 bits
of each password character, whereas a secret-key factory for PKCS #12 will
take all 16 bits of each character.

Also note that this class stores passwords as char arrays instead of

String

objects (which would seem more logical), because the
String class is immutable and there is no way to overwrite its
internal value when the password stored in it is no longer needed. Hence,
this class requests the password as a char array, so it can be overwritten
when done.

**Since:** 1.4
**See Also:** SecretKeyFactory

,

PBEParameterSpec

public class

PBEKeySpec

extends

Object

implements

KeySpec

A user-chosen password that can be used with password-based encryption
(

PBE

).

The password can be viewed as some kind of raw key material, from which
the encryption mechanism that uses it derives a cryptographic key.

Different PBE mechanisms may consume different bits of each password
character. For example, the PBE mechanism defined in

PKCS #5

looks at only the low order 8 bits of each character, whereas
PKCS #12 looks at all 16 bits of each character.

You convert the password characters to a PBE key by creating an
instance of the appropriate secret-key factory. For example, a secret-key
factory for PKCS #5 will construct a PBE key from only the low order 8 bits
of each password character, whereas a secret-key factory for PKCS #12 will
take all 16 bits of each character.

Also note that this class stores passwords as char arrays instead of

String

objects (which would seem more logical), because the
String class is immutable and there is no way to overwrite its
internal value when the password stored in it is no longer needed. Hence,
this class requests the password as a char array, so it can be overwritten
when done.

The password can be viewed as some kind of raw key material, from which
the encryption mechanism that uses it derives a cryptographic key.

Different PBE mechanisms may consume different bits of each password
character. For example, the PBE mechanism defined in

PKCS #5

looks at only the low order 8 bits of each character, whereas
PKCS #12 looks at all 16 bits of each character.

You convert the password characters to a PBE key by creating an
instance of the appropriate secret-key factory. For example, a secret-key
factory for PKCS #5 will construct a PBE key from only the low order 8 bits
of each password character, whereas a secret-key factory for PKCS #12 will
take all 16 bits of each character.

Also note that this class stores passwords as char arrays instead of

String

objects (which would seem more logical), because the
String class is immutable and there is no way to overwrite its
internal value when the password stored in it is no longer needed. Hence,
this class requests the password as a char array, so it can be overwritten
when done.

Different PBE mechanisms may consume different bits of each password
character. For example, the PBE mechanism defined in

PKCS #5

looks at only the low order 8 bits of each character, whereas
PKCS #12 looks at all 16 bits of each character.

You convert the password characters to a PBE key by creating an
instance of the appropriate secret-key factory. For example, a secret-key
factory for PKCS #5 will construct a PBE key from only the low order 8 bits
of each password character, whereas a secret-key factory for PKCS #12 will
take all 16 bits of each character.

Also note that this class stores passwords as char arrays instead of

String

objects (which would seem more logical), because the
String class is immutable and there is no way to overwrite its
internal value when the password stored in it is no longer needed. Hence,
this class requests the password as a char array, so it can be overwritten
when done.

You convert the password characters to a PBE key by creating an
instance of the appropriate secret-key factory. For example, a secret-key
factory for PKCS #5 will construct a PBE key from only the low order 8 bits
of each password character, whereas a secret-key factory for PKCS #12 will
take all 16 bits of each character.

Also note that this class stores passwords as char arrays instead of

String

objects (which would seem more logical), because the
String class is immutable and there is no way to overwrite its
internal value when the password stored in it is no longer needed. Hence,
this class requests the password as a char array, so it can be overwritten
when done.

Also note that this class stores passwords as char arrays instead of

String

objects (which would seem more logical), because the
String class is immutable and there is no way to overwrite its
internal value when the password stored in it is no longer needed. Hence,
this class requests the password as a char array, so it can be overwritten
when done.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PBEKeySpec

​(char[] password)

Constructor that takes a password.

PBEKeySpec

​(char[] password,
byte[] salt,
int iterationCount)

Constructor that takes a password, salt, iteration count for
generating PBEKey of fixed-key-size PBE ciphers.

PBEKeySpec

​(char[] password,
byte[] salt,
int iterationCount,
int keyLength)

Constructor that takes a password, salt, iteration count, and
to-be-derived key length for generating PBEKey of variable-key-size
PBE ciphers.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

clearPassword

()

Clears the internal copy of the password.

int

getIterationCount

()

Returns the iteration count or 0 if not specified.

int

getKeyLength

()

Returns the to-be-derived key length or 0 if not specified.

char[]

getPassword

()

Returns a copy of the password.

byte[]

getSalt

()

Returns a copy of the salt or null if not specified.

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

Constructor Summary

Constructors

Constructor

Description

PBEKeySpec

​(char[] password)

Constructor that takes a password.

PBEKeySpec

​(char[] password,
byte[] salt,
int iterationCount)

Constructor that takes a password, salt, iteration count for
generating PBEKey of fixed-key-size PBE ciphers.

PBEKeySpec

​(char[] password,
byte[] salt,
int iterationCount,
int keyLength)

Constructor that takes a password, salt, iteration count, and
to-be-derived key length for generating PBEKey of variable-key-size
PBE ciphers.

---

#### Constructor Summary

Constructor that takes a password.

Constructor that takes a password, salt, iteration count for
generating PBEKey of fixed-key-size PBE ciphers.

Constructor that takes a password, salt, iteration count, and
to-be-derived key length for generating PBEKey of variable-key-size
PBE ciphers.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

clearPassword

()

Clears the internal copy of the password.

int

getIterationCount

()

Returns the iteration count or 0 if not specified.

int

getKeyLength

()

Returns the to-be-derived key length or 0 if not specified.

char[]

getPassword

()

Returns a copy of the password.

byte[]

getSalt

()

Returns a copy of the salt or null if not specified.

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

Clears the internal copy of the password.

Returns the iteration count or 0 if not specified.

Returns the to-be-derived key length or 0 if not specified.

Returns a copy of the password.

Returns a copy of the salt or null if not specified.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PBEKeySpec

```java
public PBEKeySpec​(char[] password)
```

Constructor that takes a password. An empty char[] is used if
null is specified.

Note:

password

is cloned before it is stored in
the new

PBEKeySpec

object.

**Parameters:** password

- the password.

- PBEKeySpec

```java
public PBEKeySpec​(char[] password,
byte[] salt,
int iterationCount,
int keyLength)
```

Constructor that takes a password, salt, iteration count, and
to-be-derived key length for generating PBEKey of variable-key-size
PBE ciphers. An empty char[] is used if null is specified for

password

.

Note: the

password

and

salt

are cloned before they are stored in
the new

PBEKeySpec

object.

**Parameters:** password

- the password.
**Parameters:** salt

- the salt.
**Parameters:** iterationCount

- the iteration count.
**Parameters:** keyLength

- the to-be-derived key length.
**Throws:** NullPointerException

- if

salt

is null.
**Throws:** IllegalArgumentException

- if

salt

is empty,
i.e. 0-length,

iterationCount

or

keyLength

is not positive.

- PBEKeySpec

```java
public PBEKeySpec​(char[] password,
byte[] salt,
int iterationCount)
```

Constructor that takes a password, salt, iteration count for
generating PBEKey of fixed-key-size PBE ciphers. An empty
char[] is used if null is specified for

password

.

Note: the

password

and

salt

are cloned before they are stored in the new

PBEKeySpec

object.

**Parameters:** password

- the password.
**Parameters:** salt

- the salt.
**Parameters:** iterationCount

- the iteration count.
**Throws:** NullPointerException

- if

salt

is null.
**Throws:** IllegalArgumentException

- if

salt

is empty,
i.e. 0-length, or

iterationCount

is not positive.

============ METHOD DETAIL ==========

- Method Detail

- clearPassword

```java
public final void clearPassword()
```

Clears the internal copy of the password.

- getPassword

```java
public final char[] getPassword()
```

Returns a copy of the password.

Note: this method returns a copy of the password. It is
the caller's responsibility to zero out the password information after
it is no longer needed.

**Returns:** the password.
**Throws:** IllegalStateException

- if password has been cleared by
calling

clearPassword

method.

- getSalt

```java
public final byte[] getSalt()
```

Returns a copy of the salt or null if not specified.

Note: this method should return a copy of the salt. It is
the caller's responsibility to zero out the salt information after
it is no longer needed.

**Returns:** the salt.

- getIterationCount

```java
public final int getIterationCount()
```

Returns the iteration count or 0 if not specified.

**Returns:** the iteration count.

- getKeyLength

```java
public final int getKeyLength()
```

Returns the to-be-derived key length or 0 if not specified.

Note: this is used to indicate the preference on key length
for variable-key-size ciphers. The actual key size depends on
each provider's implementation.

**Returns:** the to-be-derived key length.

Constructor Detail

- PBEKeySpec

```java
public PBEKeySpec​(char[] password)
```

Constructor that takes a password. An empty char[] is used if
null is specified.

Note:

password

is cloned before it is stored in
the new

PBEKeySpec

object.

**Parameters:** password

- the password.

- PBEKeySpec

```java
public PBEKeySpec​(char[] password,
byte[] salt,
int iterationCount,
int keyLength)
```

Constructor that takes a password, salt, iteration count, and
to-be-derived key length for generating PBEKey of variable-key-size
PBE ciphers. An empty char[] is used if null is specified for

password

.

Note: the

password

and

salt

are cloned before they are stored in
the new

PBEKeySpec

object.

**Parameters:** password

- the password.
**Parameters:** salt

- the salt.
**Parameters:** iterationCount

- the iteration count.
**Parameters:** keyLength

- the to-be-derived key length.
**Throws:** NullPointerException

- if

salt

is null.
**Throws:** IllegalArgumentException

- if

salt

is empty,
i.e. 0-length,

iterationCount

or

keyLength

is not positive.

- PBEKeySpec

```java
public PBEKeySpec​(char[] password,
byte[] salt,
int iterationCount)
```

Constructor that takes a password, salt, iteration count for
generating PBEKey of fixed-key-size PBE ciphers. An empty
char[] is used if null is specified for

password

.

Note: the

password

and

salt

are cloned before they are stored in the new

PBEKeySpec

object.

**Parameters:** password

- the password.
**Parameters:** salt

- the salt.
**Parameters:** iterationCount

- the iteration count.
**Throws:** NullPointerException

- if

salt

is null.
**Throws:** IllegalArgumentException

- if

salt

is empty,
i.e. 0-length, or

iterationCount

is not positive.

---

#### Constructor Detail

PBEKeySpec

```java
public PBEKeySpec​(char[] password)
```

Constructor that takes a password. An empty char[] is used if
null is specified.

Note:

password

is cloned before it is stored in
the new

PBEKeySpec

object.

**Parameters:** password

- the password.

---

#### PBEKeySpec

public PBEKeySpec​(char[] password)

Constructor that takes a password. An empty char[] is used if
null is specified.

Note:

password

is cloned before it is stored in
the new

PBEKeySpec

object.

Note:

password

is cloned before it is stored in
the new

PBEKeySpec

object.

PBEKeySpec

```java
public PBEKeySpec​(char[] password,
byte[] salt,
int iterationCount,
int keyLength)
```

Constructor that takes a password, salt, iteration count, and
to-be-derived key length for generating PBEKey of variable-key-size
PBE ciphers. An empty char[] is used if null is specified for

password

.

Note: the

password

and

salt

are cloned before they are stored in
the new

PBEKeySpec

object.

**Parameters:** password

- the password.
**Parameters:** salt

- the salt.
**Parameters:** iterationCount

- the iteration count.
**Parameters:** keyLength

- the to-be-derived key length.
**Throws:** NullPointerException

- if

salt

is null.
**Throws:** IllegalArgumentException

- if

salt

is empty,
i.e. 0-length,

iterationCount

or

keyLength

is not positive.

---

#### PBEKeySpec

public PBEKeySpec​(char[] password,
byte[] salt,
int iterationCount,
int keyLength)

Constructor that takes a password, salt, iteration count, and
to-be-derived key length for generating PBEKey of variable-key-size
PBE ciphers. An empty char[] is used if null is specified for

password

.

Note: the

password

and

salt

are cloned before they are stored in
the new

PBEKeySpec

object.

Note: the

password

and

salt

are cloned before they are stored in
the new

PBEKeySpec

object.

PBEKeySpec

```java
public PBEKeySpec​(char[] password,
byte[] salt,
int iterationCount)
```

Constructor that takes a password, salt, iteration count for
generating PBEKey of fixed-key-size PBE ciphers. An empty
char[] is used if null is specified for

password

.

Note: the

password

and

salt

are cloned before they are stored in the new

PBEKeySpec

object.

**Parameters:** password

- the password.
**Parameters:** salt

- the salt.
**Parameters:** iterationCount

- the iteration count.
**Throws:** NullPointerException

- if

salt

is null.
**Throws:** IllegalArgumentException

- if

salt

is empty,
i.e. 0-length, or

iterationCount

is not positive.

---

#### PBEKeySpec

public PBEKeySpec​(char[] password,
byte[] salt,
int iterationCount)

Constructor that takes a password, salt, iteration count for
generating PBEKey of fixed-key-size PBE ciphers. An empty
char[] is used if null is specified for

password

.

Note: the

password

and

salt

are cloned before they are stored in the new

PBEKeySpec

object.

Note: the

password

and

salt

are cloned before they are stored in the new

PBEKeySpec

object.

Method Detail

- clearPassword

```java
public final void clearPassword()
```

Clears the internal copy of the password.

- getPassword

```java
public final char[] getPassword()
```

Returns a copy of the password.

Note: this method returns a copy of the password. It is
the caller's responsibility to zero out the password information after
it is no longer needed.

**Returns:** the password.
**Throws:** IllegalStateException

- if password has been cleared by
calling

clearPassword

method.

- getSalt

```java
public final byte[] getSalt()
```

Returns a copy of the salt or null if not specified.

Note: this method should return a copy of the salt. It is
the caller's responsibility to zero out the salt information after
it is no longer needed.

**Returns:** the salt.

- getIterationCount

```java
public final int getIterationCount()
```

Returns the iteration count or 0 if not specified.

**Returns:** the iteration count.

- getKeyLength

```java
public final int getKeyLength()
```

Returns the to-be-derived key length or 0 if not specified.

Note: this is used to indicate the preference on key length
for variable-key-size ciphers. The actual key size depends on
each provider's implementation.

**Returns:** the to-be-derived key length.

---

#### Method Detail

clearPassword

```java
public final void clearPassword()
```

Clears the internal copy of the password.

---

#### clearPassword

public final void clearPassword()

Clears the internal copy of the password.

getPassword

```java
public final char[] getPassword()
```

Returns a copy of the password.

Note: this method returns a copy of the password. It is
the caller's responsibility to zero out the password information after
it is no longer needed.

**Returns:** the password.
**Throws:** IllegalStateException

- if password has been cleared by
calling

clearPassword

method.

---

#### getPassword

public final char[] getPassword()

Returns a copy of the password.

Note: this method returns a copy of the password. It is
the caller's responsibility to zero out the password information after
it is no longer needed.

Note: this method returns a copy of the password. It is
the caller's responsibility to zero out the password information after
it is no longer needed.

getSalt

```java
public final byte[] getSalt()
```

Returns a copy of the salt or null if not specified.

Note: this method should return a copy of the salt. It is
the caller's responsibility to zero out the salt information after
it is no longer needed.

**Returns:** the salt.

---

#### getSalt

public final byte[] getSalt()

Returns a copy of the salt or null if not specified.

Note: this method should return a copy of the salt. It is
the caller's responsibility to zero out the salt information after
it is no longer needed.

Note: this method should return a copy of the salt. It is
the caller's responsibility to zero out the salt information after
it is no longer needed.

getIterationCount

```java
public final int getIterationCount()
```

Returns the iteration count or 0 if not specified.

**Returns:** the iteration count.

---

#### getIterationCount

public final int getIterationCount()

Returns the iteration count or 0 if not specified.

getKeyLength

```java
public final int getKeyLength()
```

Returns the to-be-derived key length or 0 if not specified.

Note: this is used to indicate the preference on key length
for variable-key-size ciphers. The actual key size depends on
each provider's implementation.

**Returns:** the to-be-derived key length.

---

#### getKeyLength

public final int getKeyLength()

Returns the to-be-derived key length or 0 if not specified.

Note: this is used to indicate the preference on key length
for variable-key-size ciphers. The actual key size depends on
each provider's implementation.

Note: this is used to indicate the preference on key length
for variable-key-size ciphers. The actual key size depends on
each provider's implementation.

---

