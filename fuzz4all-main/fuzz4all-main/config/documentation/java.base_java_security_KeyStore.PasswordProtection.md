# Class KeyStore.PasswordProtection

**Source:** `java.base\java\security\KeyStore.PasswordProtection.html`

### Class Description

```java
public static class
KeyStore.PasswordProtection

extends
Object

implements
KeyStore.ProtectionParameter
,
Destroyable
```

A password-based implementation of

ProtectionParameter

.

**All Implemented Interfaces:** KeyStore.ProtectionParameter

,

Destroyable

---

### Field Details

*No entries found.*

### Constructor Details

#### public PasswordProtection​(char[] password)

Creates a password parameter.

The specified

password

is cloned before it is stored
in the new

PasswordProtection

object.

**Parameters:**
- password

- the password, which may be

null

---

#### public PasswordProtection​(char[] password,

String
protectionAlgorithm,

AlgorithmParameterSpec
protectionParameters)

Creates a password parameter and specifies the protection algorithm
and associated parameters to use when encrypting a keystore entry.

The specified

password

is cloned before it is stored in the
new

PasswordProtection

object.

**Parameters:**
- password

- the password, which may be

null
- protectionAlgorithm

- the encryption algorithm name, for
example,

PBEWithHmacSHA256AndAES_256

.
See the Cipher section in the

Java Security Standard Algorithm Names Specification

for information about standard encryption algorithm names.
- protectionParameters

- the encryption algorithm parameter
specification, which may be

null

**Throws:**
- NullPointerException

- if

protectionAlgorithm

is

null

**Since:**
- 1.8

---

### Method Details

#### public
String
getProtectionAlgorithm()

Gets the name of the protection algorithm.
If none was set then the keystore provider will use its default
protection algorithm. The name of the default protection algorithm
for a given keystore type is set using the

'keystore.<type>.keyProtectionAlgorithm'

security property.
For example, the

keystore.PKCS12.keyProtectionAlgorithm

property stores the
name of the default key protection algorithm used for PKCS12
keystores. If the security property is not set, an
implementation-specific algorithm will be used.

**Returns:**
- the algorithm name, or

null

if none was set

**Since:**
- 1.8

---

#### public
AlgorithmParameterSpec
getProtectionParameters()

Gets the parameters supplied for the protection algorithm.

**Returns:**
- the algorithm parameter specification, or

null

,
if none was set

**Since:**
- 1.8

---

#### public char[] getPassword()

Gets the password.

Note that this method returns a reference to the password.
If a clone of the array is created it is the caller's
responsibility to zero out the password information
after it is no longer needed.

**Returns:**
- the password, which may be

null

**Throws:**
- IllegalStateException

- if the password has
been cleared (destroyed)

**See Also:**
- destroy()

---

#### public void destroy()
throws
DestroyFailedException

Clears the password.

**Specified by:**
- destroy

in interface

Destroyable

**Throws:**
- DestroyFailedException

- if this method was unable
to clear the password

---

#### public boolean isDestroyed()

Determines if password has been cleared.

**Specified by:**
- isDestroyed

in interface

Destroyable

**Returns:**
- true if the password has been cleared, false otherwise

---

### Additional Sections

#### Class KeyStore.PasswordProtection

java.lang.Object

- java.security.KeyStore.PasswordProtection

java.security.KeyStore.PasswordProtection

**All Implemented Interfaces:** KeyStore.ProtectionParameter

,

Destroyable

**Enclosing class:** KeyStore

```java
public static class
KeyStore.PasswordProtection

extends
Object

implements
KeyStore.ProtectionParameter
,
Destroyable
```

A password-based implementation of

ProtectionParameter

.

**Since:** 1.5

public static class

KeyStore.PasswordProtection

extends

Object

implements

KeyStore.ProtectionParameter

,

Destroyable

A password-based implementation of

ProtectionParameter

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PasswordProtection

​(char[] password)

Creates a password parameter.

PasswordProtection

​(char[] password,

String

protectionAlgorithm,

AlgorithmParameterSpec

protectionParameters)

Creates a password parameter and specifies the protection algorithm
and associated parameters to use when encrypting a keystore entry.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

destroy

()

Clears the password.

char[]

getPassword

()

Gets the password.

String

getProtectionAlgorithm

()

Gets the name of the protection algorithm.

AlgorithmParameterSpec

getProtectionParameters

()

Gets the parameters supplied for the protection algorithm.

boolean

isDestroyed

()

Determines if password has been cleared.

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

PasswordProtection

​(char[] password)

Creates a password parameter.

PasswordProtection

​(char[] password,

String

protectionAlgorithm,

AlgorithmParameterSpec

protectionParameters)

Creates a password parameter and specifies the protection algorithm
and associated parameters to use when encrypting a keystore entry.

---

#### Constructor Summary

Creates a password parameter.

Creates a password parameter and specifies the protection algorithm
and associated parameters to use when encrypting a keystore entry.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

destroy

()

Clears the password.

char[]

getPassword

()

Gets the password.

String

getProtectionAlgorithm

()

Gets the name of the protection algorithm.

AlgorithmParameterSpec

getProtectionParameters

()

Gets the parameters supplied for the protection algorithm.

boolean

isDestroyed

()

Determines if password has been cleared.

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

Clears the password.

Gets the password.

Gets the name of the protection algorithm.

Gets the parameters supplied for the protection algorithm.

Determines if password has been cleared.

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

- PasswordProtection

```java
public PasswordProtection​(char[] password)
```

Creates a password parameter.

The specified

password

is cloned before it is stored
in the new

PasswordProtection

object.

**Parameters:** password

- the password, which may be

null

- PasswordProtection

```java
public PasswordProtection​(char[] password,

String
protectionAlgorithm,

AlgorithmParameterSpec
protectionParameters)
```

Creates a password parameter and specifies the protection algorithm
and associated parameters to use when encrypting a keystore entry.

The specified

password

is cloned before it is stored in the
new

PasswordProtection

object.

**Parameters:** password

- the password, which may be

null
**Parameters:** protectionAlgorithm

- the encryption algorithm name, for
example,

PBEWithHmacSHA256AndAES_256

.
See the Cipher section in the

Java Security Standard Algorithm Names Specification

for information about standard encryption algorithm names.
**Parameters:** protectionParameters

- the encryption algorithm parameter
specification, which may be

null
**Throws:** NullPointerException

- if

protectionAlgorithm

is

null
**Since:** 1.8

============ METHOD DETAIL ==========

- Method Detail

- getProtectionAlgorithm

```java
public
String
getProtectionAlgorithm()
```

Gets the name of the protection algorithm.
If none was set then the keystore provider will use its default
protection algorithm. The name of the default protection algorithm
for a given keystore type is set using the

'keystore.<type>.keyProtectionAlgorithm'

security property.
For example, the

keystore.PKCS12.keyProtectionAlgorithm

property stores the
name of the default key protection algorithm used for PKCS12
keystores. If the security property is not set, an
implementation-specific algorithm will be used.

**Returns:** the algorithm name, or

null

if none was set
**Since:** 1.8

- getProtectionParameters

```java
public
AlgorithmParameterSpec
getProtectionParameters()
```

Gets the parameters supplied for the protection algorithm.

**Returns:** the algorithm parameter specification, or

null

,
if none was set
**Since:** 1.8

- getPassword

```java
public char[] getPassword()
```

Gets the password.

Note that this method returns a reference to the password.
If a clone of the array is created it is the caller's
responsibility to zero out the password information
after it is no longer needed.

**Returns:** the password, which may be

null
**Throws:** IllegalStateException

- if the password has
been cleared (destroyed)
**See Also:** destroy()

- destroy

```java
public void destroy()
throws
DestroyFailedException
```

Clears the password.

**Specified by:** destroy

in interface

Destroyable
**Throws:** DestroyFailedException

- if this method was unable
to clear the password

- isDestroyed

```java
public boolean isDestroyed()
```

Determines if password has been cleared.

**Specified by:** isDestroyed

in interface

Destroyable
**Returns:** true if the password has been cleared, false otherwise

Constructor Detail

- PasswordProtection

```java
public PasswordProtection​(char[] password)
```

Creates a password parameter.

The specified

password

is cloned before it is stored
in the new

PasswordProtection

object.

**Parameters:** password

- the password, which may be

null

- PasswordProtection

```java
public PasswordProtection​(char[] password,

String
protectionAlgorithm,

AlgorithmParameterSpec
protectionParameters)
```

Creates a password parameter and specifies the protection algorithm
and associated parameters to use when encrypting a keystore entry.

The specified

password

is cloned before it is stored in the
new

PasswordProtection

object.

**Parameters:** password

- the password, which may be

null
**Parameters:** protectionAlgorithm

- the encryption algorithm name, for
example,

PBEWithHmacSHA256AndAES_256

.
See the Cipher section in the

Java Security Standard Algorithm Names Specification

for information about standard encryption algorithm names.
**Parameters:** protectionParameters

- the encryption algorithm parameter
specification, which may be

null
**Throws:** NullPointerException

- if

protectionAlgorithm

is

null
**Since:** 1.8

---

#### Constructor Detail

PasswordProtection

```java
public PasswordProtection​(char[] password)
```

Creates a password parameter.

The specified

password

is cloned before it is stored
in the new

PasswordProtection

object.

**Parameters:** password

- the password, which may be

null

---

#### PasswordProtection

public PasswordProtection​(char[] password)

Creates a password parameter.

The specified

password

is cloned before it is stored
in the new

PasswordProtection

object.

The specified

password

is cloned before it is stored
in the new

PasswordProtection

object.

PasswordProtection

```java
public PasswordProtection​(char[] password,

String
protectionAlgorithm,

AlgorithmParameterSpec
protectionParameters)
```

Creates a password parameter and specifies the protection algorithm
and associated parameters to use when encrypting a keystore entry.

The specified

password

is cloned before it is stored in the
new

PasswordProtection

object.

**Parameters:** password

- the password, which may be

null
**Parameters:** protectionAlgorithm

- the encryption algorithm name, for
example,

PBEWithHmacSHA256AndAES_256

.
See the Cipher section in the

Java Security Standard Algorithm Names Specification

for information about standard encryption algorithm names.
**Parameters:** protectionParameters

- the encryption algorithm parameter
specification, which may be

null
**Throws:** NullPointerException

- if

protectionAlgorithm

is

null
**Since:** 1.8

---

#### PasswordProtection

public PasswordProtection​(char[] password,

String

protectionAlgorithm,

AlgorithmParameterSpec

protectionParameters)

Creates a password parameter and specifies the protection algorithm
and associated parameters to use when encrypting a keystore entry.

The specified

password

is cloned before it is stored in the
new

PasswordProtection

object.

The specified

password

is cloned before it is stored in the
new

PasswordProtection

object.

Method Detail

- getProtectionAlgorithm

```java
public
String
getProtectionAlgorithm()
```

Gets the name of the protection algorithm.
If none was set then the keystore provider will use its default
protection algorithm. The name of the default protection algorithm
for a given keystore type is set using the

'keystore.<type>.keyProtectionAlgorithm'

security property.
For example, the

keystore.PKCS12.keyProtectionAlgorithm

property stores the
name of the default key protection algorithm used for PKCS12
keystores. If the security property is not set, an
implementation-specific algorithm will be used.

**Returns:** the algorithm name, or

null

if none was set
**Since:** 1.8

- getProtectionParameters

```java
public
AlgorithmParameterSpec
getProtectionParameters()
```

Gets the parameters supplied for the protection algorithm.

**Returns:** the algorithm parameter specification, or

null

,
if none was set
**Since:** 1.8

- getPassword

```java
public char[] getPassword()
```

Gets the password.

Note that this method returns a reference to the password.
If a clone of the array is created it is the caller's
responsibility to zero out the password information
after it is no longer needed.

**Returns:** the password, which may be

null
**Throws:** IllegalStateException

- if the password has
been cleared (destroyed)
**See Also:** destroy()

- destroy

```java
public void destroy()
throws
DestroyFailedException
```

Clears the password.

**Specified by:** destroy

in interface

Destroyable
**Throws:** DestroyFailedException

- if this method was unable
to clear the password

- isDestroyed

```java
public boolean isDestroyed()
```

Determines if password has been cleared.

**Specified by:** isDestroyed

in interface

Destroyable
**Returns:** true if the password has been cleared, false otherwise

---

#### Method Detail

getProtectionAlgorithm

```java
public
String
getProtectionAlgorithm()
```

Gets the name of the protection algorithm.
If none was set then the keystore provider will use its default
protection algorithm. The name of the default protection algorithm
for a given keystore type is set using the

'keystore.<type>.keyProtectionAlgorithm'

security property.
For example, the

keystore.PKCS12.keyProtectionAlgorithm

property stores the
name of the default key protection algorithm used for PKCS12
keystores. If the security property is not set, an
implementation-specific algorithm will be used.

**Returns:** the algorithm name, or

null

if none was set
**Since:** 1.8

---

#### getProtectionAlgorithm

public

String

getProtectionAlgorithm()

Gets the name of the protection algorithm.
If none was set then the keystore provider will use its default
protection algorithm. The name of the default protection algorithm
for a given keystore type is set using the

'keystore.<type>.keyProtectionAlgorithm'

security property.
For example, the

keystore.PKCS12.keyProtectionAlgorithm

property stores the
name of the default key protection algorithm used for PKCS12
keystores. If the security property is not set, an
implementation-specific algorithm will be used.

getProtectionParameters

```java
public
AlgorithmParameterSpec
getProtectionParameters()
```

Gets the parameters supplied for the protection algorithm.

**Returns:** the algorithm parameter specification, or

null

,
if none was set
**Since:** 1.8

---

#### getProtectionParameters

public

AlgorithmParameterSpec

getProtectionParameters()

Gets the parameters supplied for the protection algorithm.

getPassword

```java
public char[] getPassword()
```

Gets the password.

Note that this method returns a reference to the password.
If a clone of the array is created it is the caller's
responsibility to zero out the password information
after it is no longer needed.

**Returns:** the password, which may be

null
**Throws:** IllegalStateException

- if the password has
been cleared (destroyed)
**See Also:** destroy()

---

#### getPassword

public char[] getPassword()

Gets the password.

Note that this method returns a reference to the password.
If a clone of the array is created it is the caller's
responsibility to zero out the password information
after it is no longer needed.

Note that this method returns a reference to the password.
If a clone of the array is created it is the caller's
responsibility to zero out the password information
after it is no longer needed.

destroy

```java
public void destroy()
throws
DestroyFailedException
```

Clears the password.

**Specified by:** destroy

in interface

Destroyable
**Throws:** DestroyFailedException

- if this method was unable
to clear the password

---

#### destroy

public void destroy()
throws

DestroyFailedException

Clears the password.

isDestroyed

```java
public boolean isDestroyed()
```

Determines if password has been cleared.

**Specified by:** isDestroyed

in interface

Destroyable
**Returns:** true if the password has been cleared, false otherwise

---

#### isDestroyed

public boolean isDestroyed()

Determines if password has been cleared.

---

