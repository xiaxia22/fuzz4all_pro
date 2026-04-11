# Class KeyStore.Builder

**Source:** `java.base\java\security\KeyStore.Builder.html`

### Class Description

```java
public abstract static class
KeyStore.Builder

extends
Object
```

A description of a to-be-instantiated KeyStore object.

An instance of this class encapsulates the information needed to
instantiate and initialize a KeyStore object. That process is
triggered when the

getKeyStore()

method is called.

This makes it possible to decouple configuration from KeyStore
object creation and e.g. delay a password prompt until it is
needed.

**Enclosing class:** KeyStore

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Builder()

Construct a new Builder.

---

### Method Details

#### public abstract
KeyStore
getKeyStore()
throws
KeyStoreException

Returns the KeyStore described by this object.

**Returns:**
- the

KeyStore

described by this object

**Throws:**
- KeyStoreException

- if an error occurred during the
operation, for example if the KeyStore could not be
instantiated or loaded

---

#### public abstract
KeyStore.ProtectionParameter
getProtectionParameter​(
String
alias)
throws
KeyStoreException

Returns the ProtectionParameters that should be used to obtain
the

Entry

with the given alias.
The

getKeyStore

method must be invoked before this
method may be called.

**Parameters:**
- alias

- the alias of the KeyStore entry

**Returns:**
- the ProtectionParameters that should be used to obtain
the

Entry

with the given alias.

**Throws:**
- NullPointerException

- if alias is null
- KeyStoreException

- if an error occurred during the
operation
- IllegalStateException

- if the getKeyStore method has
not been invoked prior to calling this method

---

#### public static
KeyStore.Builder
newInstance​(
KeyStore
keyStore,

KeyStore.ProtectionParameter
protectionParameter)

Returns a new Builder that encapsulates the given KeyStore.
The

getKeyStore()

method of the returned object
will return

keyStore

, the

getProtectionParameter()

method will
return

protectionParameters

.

This is useful if an existing KeyStore object needs to be
used with Builder-based APIs.

**Parameters:**
- keyStore

- the KeyStore to be encapsulated
- protectionParameter

- the ProtectionParameter used to
protect the KeyStore entries

**Returns:**
- a new Builder object

**Throws:**
- NullPointerException

- if keyStore or
protectionParameters is null
- IllegalArgumentException

- if the keyStore has not been
initialized

---

#### public static
KeyStore.Builder
newInstance​(
String
type,

Provider
provider,

File
file,

KeyStore.ProtectionParameter
protection)

Returns a new Builder object.

The first call to the

getKeyStore()

method on the returned
builder will create a KeyStore of type

type

and call
its

load()

method.
The

inputStream

argument is constructed from

file

.
If

protection

is a

PasswordProtection

, the password is obtained by
calling the

getPassword

method.
Otherwise, if

protection

is a

CallbackHandlerProtection

, the password is obtained
by invoking the CallbackHandler.

Subsequent calls to

getKeyStore()

return the same object
as the initial call. If the initial call failed with a
KeyStoreException, subsequent calls also throw a
KeyStoreException.

The KeyStore is instantiated from

provider

if
non-null. Otherwise, all installed providers are searched.

Calls to

getProtectionParameter()

will return a

PasswordProtection

object encapsulating the password that was used to invoke the

load

method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

**Parameters:**
- type

- the type of KeyStore to be constructed
- provider

- the provider from which the KeyStore is to
be instantiated (or null)
- file

- the File that contains the KeyStore data
- protection

- the ProtectionParameter securing the KeyStore data

**Returns:**
- a new Builder object

**Throws:**
- NullPointerException

- if type, file or protection is null
- IllegalArgumentException

- if protection is not an instance
of either PasswordProtection or CallbackHandlerProtection; or
if file does not exist or does not refer to a normal file

---

#### public static
KeyStore.Builder
newInstance​(
File
file,

KeyStore.ProtectionParameter
protection)

Returns a new Builder object.

The first call to the

getKeyStore()

method on the returned
builder will create a KeyStore using

file

to detect the
keystore type and then call its

load()

method.
It uses the same algorithm to determine the keystore type as
described in

KeyStore.getInstance(File, LoadStoreParameter)

.
The

inputStream

argument is constructed from

file

.
If

protection

is a

PasswordProtection

, the password
is obtained by calling the

getPassword

method.
Otherwise, if

protection

is a

CallbackHandlerProtection

,
the password is obtained by invoking the CallbackHandler.

Subsequent calls to

getKeyStore()

return the same object
as the initial call. If the initial call failed with a
KeyStoreException, subsequent calls also throw a KeyStoreException.

Calls to

getProtectionParameter()

will return a

PasswordProtection

object encapsulating the password that was used to invoke the

load

method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

**Parameters:**
- file

- the File that contains the KeyStore data
- protection

- the ProtectionParameter securing the KeyStore data

**Returns:**
- a new Builder object

**Throws:**
- NullPointerException

- if file or protection is null
- IllegalArgumentException

- if protection is not an instance
of either PasswordProtection or CallbackHandlerProtection; or
if file does not exist or does not refer to a normal file

**Since:**
- 9

---

#### public static
KeyStore.Builder
newInstance​(
String
type,

Provider
provider,

KeyStore.ProtectionParameter
protection)

Returns a new Builder object.

Each call to the

getKeyStore()

method on the returned
builder will return a new KeyStore object of type

type

.
Its

load()

method is invoked using a

LoadStoreParameter

that encapsulates

protection

.

The KeyStore is instantiated from

provider

if
non-null. Otherwise, all installed providers are searched.

Calls to

getProtectionParameter()

will return

protection

.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

**Parameters:**
- type

- the type of KeyStore to be constructed
- provider

- the provider from which the KeyStore is to
be instantiated (or null)
- protection

- the ProtectionParameter securing the Keystore

**Returns:**
- a new Builder object

**Throws:**
- NullPointerException

- if type or protection is null

---

### Additional Sections

#### Class KeyStore.Builder

java.lang.Object

- java.security.KeyStore.Builder

java.security.KeyStore.Builder

**Enclosing class:** KeyStore

```java
public abstract static class
KeyStore.Builder

extends
Object
```

A description of a to-be-instantiated KeyStore object.

An instance of this class encapsulates the information needed to
instantiate and initialize a KeyStore object. That process is
triggered when the

getKeyStore()

method is called.

This makes it possible to decouple configuration from KeyStore
object creation and e.g. delay a password prompt until it is
needed.

**Since:** 1.5
**See Also:** KeyStore

,

KeyStoreBuilderParameters

public abstract static class

KeyStore.Builder

extends

Object

A description of a to-be-instantiated KeyStore object.

An instance of this class encapsulates the information needed to
instantiate and initialize a KeyStore object. That process is
triggered when the

getKeyStore()

method is called.

This makes it possible to decouple configuration from KeyStore
object creation and e.g. delay a password prompt until it is
needed.

An instance of this class encapsulates the information needed to
instantiate and initialize a KeyStore object. That process is
triggered when the

getKeyStore()

method is called.

This makes it possible to decouple configuration from KeyStore
object creation and e.g. delay a password prompt until it is
needed.

This makes it possible to decouple configuration from KeyStore
object creation and e.g. delay a password prompt until it is
needed.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Builder

()

Construct a new Builder.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

KeyStore

getKeyStore

()

Returns the KeyStore described by this object.

abstract

KeyStore.ProtectionParameter

getProtectionParameter

​(

String

alias)

Returns the ProtectionParameters that should be used to obtain
the

Entry

with the given alias.

static

KeyStore.Builder

newInstance

​(

File

file,

KeyStore.ProtectionParameter

protection)

Returns a new Builder object.

static

KeyStore.Builder

newInstance

​(

String

type,

Provider

provider,

File

file,

KeyStore.ProtectionParameter

protection)

Returns a new Builder object.

static

KeyStore.Builder

newInstance

​(

String

type,

Provider

provider,

KeyStore.ProtectionParameter

protection)

Returns a new Builder object.

static

KeyStore.Builder

newInstance

​(

KeyStore

keyStore,

KeyStore.ProtectionParameter

protectionParameter)

Returns a new Builder that encapsulates the given KeyStore.

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

Modifier

Constructor

Description

protected

Builder

()

Construct a new Builder.

---

#### Constructor Summary

Construct a new Builder.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

KeyStore

getKeyStore

()

Returns the KeyStore described by this object.

abstract

KeyStore.ProtectionParameter

getProtectionParameter

​(

String

alias)

Returns the ProtectionParameters that should be used to obtain
the

Entry

with the given alias.

static

KeyStore.Builder

newInstance

​(

File

file,

KeyStore.ProtectionParameter

protection)

Returns a new Builder object.

static

KeyStore.Builder

newInstance

​(

String

type,

Provider

provider,

File

file,

KeyStore.ProtectionParameter

protection)

Returns a new Builder object.

static

KeyStore.Builder

newInstance

​(

String

type,

Provider

provider,

KeyStore.ProtectionParameter

protection)

Returns a new Builder object.

static

KeyStore.Builder

newInstance

​(

KeyStore

keyStore,

KeyStore.ProtectionParameter

protectionParameter)

Returns a new Builder that encapsulates the given KeyStore.

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

Returns the KeyStore described by this object.

Returns the ProtectionParameters that should be used to obtain
the

Entry

with the given alias.

Returns a new Builder object.

Returns a new Builder that encapsulates the given KeyStore.

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

- Builder

```java
protected Builder()
```

Construct a new Builder.

============ METHOD DETAIL ==========

- Method Detail

- getKeyStore

```java
public abstract
KeyStore
getKeyStore()
throws
KeyStoreException
```

Returns the KeyStore described by this object.

**Returns:** the

KeyStore

described by this object
**Throws:** KeyStoreException

- if an error occurred during the
operation, for example if the KeyStore could not be
instantiated or loaded

- getProtectionParameter

```java
public abstract
KeyStore.ProtectionParameter
getProtectionParameter​(
String
alias)
throws
KeyStoreException
```

Returns the ProtectionParameters that should be used to obtain
the

Entry

with the given alias.
The

getKeyStore

method must be invoked before this
method may be called.

**Parameters:** alias

- the alias of the KeyStore entry
**Returns:** the ProtectionParameters that should be used to obtain
the

Entry

with the given alias.
**Throws:** NullPointerException

- if alias is null
**Throws:** KeyStoreException

- if an error occurred during the
operation
**Throws:** IllegalStateException

- if the getKeyStore method has
not been invoked prior to calling this method

- newInstance

```java
public static
KeyStore.Builder
newInstance​(
KeyStore
keyStore,

KeyStore.ProtectionParameter
protectionParameter)
```

Returns a new Builder that encapsulates the given KeyStore.
The

getKeyStore()

method of the returned object
will return

keyStore

, the

getProtectionParameter()

method will
return

protectionParameters

.

This is useful if an existing KeyStore object needs to be
used with Builder-based APIs.

**Parameters:** keyStore

- the KeyStore to be encapsulated
**Parameters:** protectionParameter

- the ProtectionParameter used to
protect the KeyStore entries
**Returns:** a new Builder object
**Throws:** NullPointerException

- if keyStore or
protectionParameters is null
**Throws:** IllegalArgumentException

- if the keyStore has not been
initialized

- newInstance

```java
public static
KeyStore.Builder
newInstance​(
String
type,

Provider
provider,

File
file,

KeyStore.ProtectionParameter
protection)
```

Returns a new Builder object.

The first call to the

getKeyStore()

method on the returned
builder will create a KeyStore of type

type

and call
its

load()

method.
The

inputStream

argument is constructed from

file

.
If

protection

is a

PasswordProtection

, the password is obtained by
calling the

getPassword

method.
Otherwise, if

protection

is a

CallbackHandlerProtection

, the password is obtained
by invoking the CallbackHandler.

Subsequent calls to

getKeyStore()

return the same object
as the initial call. If the initial call failed with a
KeyStoreException, subsequent calls also throw a
KeyStoreException.

The KeyStore is instantiated from

provider

if
non-null. Otherwise, all installed providers are searched.

Calls to

getProtectionParameter()

will return a

PasswordProtection

object encapsulating the password that was used to invoke the

load

method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

**Parameters:** type

- the type of KeyStore to be constructed
**Parameters:** provider

- the provider from which the KeyStore is to
be instantiated (or null)
**Parameters:** file

- the File that contains the KeyStore data
**Parameters:** protection

- the ProtectionParameter securing the KeyStore data
**Returns:** a new Builder object
**Throws:** NullPointerException

- if type, file or protection is null
**Throws:** IllegalArgumentException

- if protection is not an instance
of either PasswordProtection or CallbackHandlerProtection; or
if file does not exist or does not refer to a normal file

- newInstance

```java
public static
KeyStore.Builder
newInstance​(
File
file,

KeyStore.ProtectionParameter
protection)
```

Returns a new Builder object.

The first call to the

getKeyStore()

method on the returned
builder will create a KeyStore using

file

to detect the
keystore type and then call its

load()

method.
It uses the same algorithm to determine the keystore type as
described in

KeyStore.getInstance(File, LoadStoreParameter)

.
The

inputStream

argument is constructed from

file

.
If

protection

is a

PasswordProtection

, the password
is obtained by calling the

getPassword

method.
Otherwise, if

protection

is a

CallbackHandlerProtection

,
the password is obtained by invoking the CallbackHandler.

Subsequent calls to

getKeyStore()

return the same object
as the initial call. If the initial call failed with a
KeyStoreException, subsequent calls also throw a KeyStoreException.

Calls to

getProtectionParameter()

will return a

PasswordProtection

object encapsulating the password that was used to invoke the

load

method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

**Parameters:** file

- the File that contains the KeyStore data
**Parameters:** protection

- the ProtectionParameter securing the KeyStore data
**Returns:** a new Builder object
**Throws:** NullPointerException

- if file or protection is null
**Throws:** IllegalArgumentException

- if protection is not an instance
of either PasswordProtection or CallbackHandlerProtection; or
if file does not exist or does not refer to a normal file
**Since:** 9

- newInstance

```java
public static
KeyStore.Builder
newInstance​(
String
type,

Provider
provider,

KeyStore.ProtectionParameter
protection)
```

Returns a new Builder object.

Each call to the

getKeyStore()

method on the returned
builder will return a new KeyStore object of type

type

.
Its

load()

method is invoked using a

LoadStoreParameter

that encapsulates

protection

.

The KeyStore is instantiated from

provider

if
non-null. Otherwise, all installed providers are searched.

Calls to

getProtectionParameter()

will return

protection

.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

**Parameters:** type

- the type of KeyStore to be constructed
**Parameters:** provider

- the provider from which the KeyStore is to
be instantiated (or null)
**Parameters:** protection

- the ProtectionParameter securing the Keystore
**Returns:** a new Builder object
**Throws:** NullPointerException

- if type or protection is null

Constructor Detail

- Builder

```java
protected Builder()
```

Construct a new Builder.

---

#### Constructor Detail

Builder

```java
protected Builder()
```

Construct a new Builder.

---

#### Builder

protected Builder()

Construct a new Builder.

Method Detail

- getKeyStore

```java
public abstract
KeyStore
getKeyStore()
throws
KeyStoreException
```

Returns the KeyStore described by this object.

**Returns:** the

KeyStore

described by this object
**Throws:** KeyStoreException

- if an error occurred during the
operation, for example if the KeyStore could not be
instantiated or loaded

- getProtectionParameter

```java
public abstract
KeyStore.ProtectionParameter
getProtectionParameter​(
String
alias)
throws
KeyStoreException
```

Returns the ProtectionParameters that should be used to obtain
the

Entry

with the given alias.
The

getKeyStore

method must be invoked before this
method may be called.

**Parameters:** alias

- the alias of the KeyStore entry
**Returns:** the ProtectionParameters that should be used to obtain
the

Entry

with the given alias.
**Throws:** NullPointerException

- if alias is null
**Throws:** KeyStoreException

- if an error occurred during the
operation
**Throws:** IllegalStateException

- if the getKeyStore method has
not been invoked prior to calling this method

- newInstance

```java
public static
KeyStore.Builder
newInstance​(
KeyStore
keyStore,

KeyStore.ProtectionParameter
protectionParameter)
```

Returns a new Builder that encapsulates the given KeyStore.
The

getKeyStore()

method of the returned object
will return

keyStore

, the

getProtectionParameter()

method will
return

protectionParameters

.

This is useful if an existing KeyStore object needs to be
used with Builder-based APIs.

**Parameters:** keyStore

- the KeyStore to be encapsulated
**Parameters:** protectionParameter

- the ProtectionParameter used to
protect the KeyStore entries
**Returns:** a new Builder object
**Throws:** NullPointerException

- if keyStore or
protectionParameters is null
**Throws:** IllegalArgumentException

- if the keyStore has not been
initialized

- newInstance

```java
public static
KeyStore.Builder
newInstance​(
String
type,

Provider
provider,

File
file,

KeyStore.ProtectionParameter
protection)
```

Returns a new Builder object.

The first call to the

getKeyStore()

method on the returned
builder will create a KeyStore of type

type

and call
its

load()

method.
The

inputStream

argument is constructed from

file

.
If

protection

is a

PasswordProtection

, the password is obtained by
calling the

getPassword

method.
Otherwise, if

protection

is a

CallbackHandlerProtection

, the password is obtained
by invoking the CallbackHandler.

Subsequent calls to

getKeyStore()

return the same object
as the initial call. If the initial call failed with a
KeyStoreException, subsequent calls also throw a
KeyStoreException.

The KeyStore is instantiated from

provider

if
non-null. Otherwise, all installed providers are searched.

Calls to

getProtectionParameter()

will return a

PasswordProtection

object encapsulating the password that was used to invoke the

load

method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

**Parameters:** type

- the type of KeyStore to be constructed
**Parameters:** provider

- the provider from which the KeyStore is to
be instantiated (or null)
**Parameters:** file

- the File that contains the KeyStore data
**Parameters:** protection

- the ProtectionParameter securing the KeyStore data
**Returns:** a new Builder object
**Throws:** NullPointerException

- if type, file or protection is null
**Throws:** IllegalArgumentException

- if protection is not an instance
of either PasswordProtection or CallbackHandlerProtection; or
if file does not exist or does not refer to a normal file

- newInstance

```java
public static
KeyStore.Builder
newInstance​(
File
file,

KeyStore.ProtectionParameter
protection)
```

Returns a new Builder object.

The first call to the

getKeyStore()

method on the returned
builder will create a KeyStore using

file

to detect the
keystore type and then call its

load()

method.
It uses the same algorithm to determine the keystore type as
described in

KeyStore.getInstance(File, LoadStoreParameter)

.
The

inputStream

argument is constructed from

file

.
If

protection

is a

PasswordProtection

, the password
is obtained by calling the

getPassword

method.
Otherwise, if

protection

is a

CallbackHandlerProtection

,
the password is obtained by invoking the CallbackHandler.

Subsequent calls to

getKeyStore()

return the same object
as the initial call. If the initial call failed with a
KeyStoreException, subsequent calls also throw a KeyStoreException.

Calls to

getProtectionParameter()

will return a

PasswordProtection

object encapsulating the password that was used to invoke the

load

method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

**Parameters:** file

- the File that contains the KeyStore data
**Parameters:** protection

- the ProtectionParameter securing the KeyStore data
**Returns:** a new Builder object
**Throws:** NullPointerException

- if file or protection is null
**Throws:** IllegalArgumentException

- if protection is not an instance
of either PasswordProtection or CallbackHandlerProtection; or
if file does not exist or does not refer to a normal file
**Since:** 9

- newInstance

```java
public static
KeyStore.Builder
newInstance​(
String
type,

Provider
provider,

KeyStore.ProtectionParameter
protection)
```

Returns a new Builder object.

Each call to the

getKeyStore()

method on the returned
builder will return a new KeyStore object of type

type

.
Its

load()

method is invoked using a

LoadStoreParameter

that encapsulates

protection

.

The KeyStore is instantiated from

provider

if
non-null. Otherwise, all installed providers are searched.

Calls to

getProtectionParameter()

will return

protection

.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

**Parameters:** type

- the type of KeyStore to be constructed
**Parameters:** provider

- the provider from which the KeyStore is to
be instantiated (or null)
**Parameters:** protection

- the ProtectionParameter securing the Keystore
**Returns:** a new Builder object
**Throws:** NullPointerException

- if type or protection is null

---

#### Method Detail

getKeyStore

```java
public abstract
KeyStore
getKeyStore()
throws
KeyStoreException
```

Returns the KeyStore described by this object.

**Returns:** the

KeyStore

described by this object
**Throws:** KeyStoreException

- if an error occurred during the
operation, for example if the KeyStore could not be
instantiated or loaded

---

#### getKeyStore

public abstract

KeyStore

getKeyStore()
throws

KeyStoreException

Returns the KeyStore described by this object.

getProtectionParameter

```java
public abstract
KeyStore.ProtectionParameter
getProtectionParameter​(
String
alias)
throws
KeyStoreException
```

Returns the ProtectionParameters that should be used to obtain
the

Entry

with the given alias.
The

getKeyStore

method must be invoked before this
method may be called.

**Parameters:** alias

- the alias of the KeyStore entry
**Returns:** the ProtectionParameters that should be used to obtain
the

Entry

with the given alias.
**Throws:** NullPointerException

- if alias is null
**Throws:** KeyStoreException

- if an error occurred during the
operation
**Throws:** IllegalStateException

- if the getKeyStore method has
not been invoked prior to calling this method

---

#### getProtectionParameter

public abstract

KeyStore.ProtectionParameter

getProtectionParameter​(

String

alias)
throws

KeyStoreException

Returns the ProtectionParameters that should be used to obtain
the

Entry

with the given alias.
The

getKeyStore

method must be invoked before this
method may be called.

newInstance

```java
public static
KeyStore.Builder
newInstance​(
KeyStore
keyStore,

KeyStore.ProtectionParameter
protectionParameter)
```

Returns a new Builder that encapsulates the given KeyStore.
The

getKeyStore()

method of the returned object
will return

keyStore

, the

getProtectionParameter()

method will
return

protectionParameters

.

This is useful if an existing KeyStore object needs to be
used with Builder-based APIs.

**Parameters:** keyStore

- the KeyStore to be encapsulated
**Parameters:** protectionParameter

- the ProtectionParameter used to
protect the KeyStore entries
**Returns:** a new Builder object
**Throws:** NullPointerException

- if keyStore or
protectionParameters is null
**Throws:** IllegalArgumentException

- if the keyStore has not been
initialized

---

#### newInstance

public static

KeyStore.Builder

newInstance​(

KeyStore

keyStore,

KeyStore.ProtectionParameter

protectionParameter)

Returns a new Builder that encapsulates the given KeyStore.
The

getKeyStore()

method of the returned object
will return

keyStore

, the

getProtectionParameter()

method will
return

protectionParameters

.

This is useful if an existing KeyStore object needs to be
used with Builder-based APIs.

This is useful if an existing KeyStore object needs to be
used with Builder-based APIs.

newInstance

```java
public static
KeyStore.Builder
newInstance​(
String
type,

Provider
provider,

File
file,

KeyStore.ProtectionParameter
protection)
```

Returns a new Builder object.

The first call to the

getKeyStore()

method on the returned
builder will create a KeyStore of type

type

and call
its

load()

method.
The

inputStream

argument is constructed from

file

.
If

protection

is a

PasswordProtection

, the password is obtained by
calling the

getPassword

method.
Otherwise, if

protection

is a

CallbackHandlerProtection

, the password is obtained
by invoking the CallbackHandler.

Subsequent calls to

getKeyStore()

return the same object
as the initial call. If the initial call failed with a
KeyStoreException, subsequent calls also throw a
KeyStoreException.

The KeyStore is instantiated from

provider

if
non-null. Otherwise, all installed providers are searched.

Calls to

getProtectionParameter()

will return a

PasswordProtection

object encapsulating the password that was used to invoke the

load

method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

**Parameters:** type

- the type of KeyStore to be constructed
**Parameters:** provider

- the provider from which the KeyStore is to
be instantiated (or null)
**Parameters:** file

- the File that contains the KeyStore data
**Parameters:** protection

- the ProtectionParameter securing the KeyStore data
**Returns:** a new Builder object
**Throws:** NullPointerException

- if type, file or protection is null
**Throws:** IllegalArgumentException

- if protection is not an instance
of either PasswordProtection or CallbackHandlerProtection; or
if file does not exist or does not refer to a normal file

---

#### newInstance

public static

KeyStore.Builder

newInstance​(

String

type,

Provider

provider,

File

file,

KeyStore.ProtectionParameter

protection)

Returns a new Builder object.

The first call to the

getKeyStore()

method on the returned
builder will create a KeyStore of type

type

and call
its

load()

method.
The

inputStream

argument is constructed from

file

.
If

protection

is a

PasswordProtection

, the password is obtained by
calling the

getPassword

method.
Otherwise, if

protection

is a

CallbackHandlerProtection

, the password is obtained
by invoking the CallbackHandler.

Subsequent calls to

getKeyStore()

return the same object
as the initial call. If the initial call failed with a
KeyStoreException, subsequent calls also throw a
KeyStoreException.

The KeyStore is instantiated from

provider

if
non-null. Otherwise, all installed providers are searched.

Calls to

getProtectionParameter()

will return a

PasswordProtection

object encapsulating the password that was used to invoke the

load

method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

The first call to the

getKeyStore()

method on the returned
builder will create a KeyStore of type

type

and call
its

load()

method.
The

inputStream

argument is constructed from

file

.
If

protection

is a

PasswordProtection

, the password is obtained by
calling the

getPassword

method.
Otherwise, if

protection

is a

CallbackHandlerProtection

, the password is obtained
by invoking the CallbackHandler.

Subsequent calls to

getKeyStore()

return the same object
as the initial call. If the initial call failed with a
KeyStoreException, subsequent calls also throw a
KeyStoreException.

The KeyStore is instantiated from

provider

if
non-null. Otherwise, all installed providers are searched.

Calls to

getProtectionParameter()

will return a

PasswordProtection

object encapsulating the password that was used to invoke the

load

method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

Subsequent calls to

getKeyStore()

return the same object
as the initial call. If the initial call failed with a
KeyStoreException, subsequent calls also throw a
KeyStoreException.

The KeyStore is instantiated from

provider

if
non-null. Otherwise, all installed providers are searched.

Calls to

getProtectionParameter()

will return a

PasswordProtection

object encapsulating the password that was used to invoke the

load

method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

The KeyStore is instantiated from

provider

if
non-null. Otherwise, all installed providers are searched.

Calls to

getProtectionParameter()

will return a

PasswordProtection

object encapsulating the password that was used to invoke the

load

method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

Calls to

getProtectionParameter()

will return a

PasswordProtection

object encapsulating the password that was used to invoke the

load

method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

newInstance

```java
public static
KeyStore.Builder
newInstance​(
File
file,

KeyStore.ProtectionParameter
protection)
```

Returns a new Builder object.

The first call to the

getKeyStore()

method on the returned
builder will create a KeyStore using

file

to detect the
keystore type and then call its

load()

method.
It uses the same algorithm to determine the keystore type as
described in

KeyStore.getInstance(File, LoadStoreParameter)

.
The

inputStream

argument is constructed from

file

.
If

protection

is a

PasswordProtection

, the password
is obtained by calling the

getPassword

method.
Otherwise, if

protection

is a

CallbackHandlerProtection

,
the password is obtained by invoking the CallbackHandler.

Subsequent calls to

getKeyStore()

return the same object
as the initial call. If the initial call failed with a
KeyStoreException, subsequent calls also throw a KeyStoreException.

Calls to

getProtectionParameter()

will return a

PasswordProtection

object encapsulating the password that was used to invoke the

load

method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

**Parameters:** file

- the File that contains the KeyStore data
**Parameters:** protection

- the ProtectionParameter securing the KeyStore data
**Returns:** a new Builder object
**Throws:** NullPointerException

- if file or protection is null
**Throws:** IllegalArgumentException

- if protection is not an instance
of either PasswordProtection or CallbackHandlerProtection; or
if file does not exist or does not refer to a normal file
**Since:** 9

---

#### newInstance

public static

KeyStore.Builder

newInstance​(

File

file,

KeyStore.ProtectionParameter

protection)

Returns a new Builder object.

The first call to the

getKeyStore()

method on the returned
builder will create a KeyStore using

file

to detect the
keystore type and then call its

load()

method.
It uses the same algorithm to determine the keystore type as
described in

KeyStore.getInstance(File, LoadStoreParameter)

.
The

inputStream

argument is constructed from

file

.
If

protection

is a

PasswordProtection

, the password
is obtained by calling the

getPassword

method.
Otherwise, if

protection

is a

CallbackHandlerProtection

,
the password is obtained by invoking the CallbackHandler.

Subsequent calls to

getKeyStore()

return the same object
as the initial call. If the initial call failed with a
KeyStoreException, subsequent calls also throw a KeyStoreException.

Calls to

getProtectionParameter()

will return a

PasswordProtection

object encapsulating the password that was used to invoke the

load

method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

The first call to the

getKeyStore()

method on the returned
builder will create a KeyStore using

file

to detect the
keystore type and then call its

load()

method.
It uses the same algorithm to determine the keystore type as
described in

KeyStore.getInstance(File, LoadStoreParameter)

.
The

inputStream

argument is constructed from

file

.
If

protection

is a

PasswordProtection

, the password
is obtained by calling the

getPassword

method.
Otherwise, if

protection

is a

CallbackHandlerProtection

,
the password is obtained by invoking the CallbackHandler.

Subsequent calls to

getKeyStore()

return the same object
as the initial call. If the initial call failed with a
KeyStoreException, subsequent calls also throw a KeyStoreException.

Calls to

getProtectionParameter()

will return a

PasswordProtection

object encapsulating the password that was used to invoke the

load

method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

Subsequent calls to

getKeyStore()

return the same object
as the initial call. If the initial call failed with a
KeyStoreException, subsequent calls also throw a KeyStoreException.

Calls to

getProtectionParameter()

will return a

PasswordProtection

object encapsulating the password that was used to invoke the

load

method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

Calls to

getProtectionParameter()

will return a

PasswordProtection

object encapsulating the password that was used to invoke the

load

method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

newInstance

```java
public static
KeyStore.Builder
newInstance​(
String
type,

Provider
provider,

KeyStore.ProtectionParameter
protection)
```

Returns a new Builder object.

Each call to the

getKeyStore()

method on the returned
builder will return a new KeyStore object of type

type

.
Its

load()

method is invoked using a

LoadStoreParameter

that encapsulates

protection

.

The KeyStore is instantiated from

provider

if
non-null. Otherwise, all installed providers are searched.

Calls to

getProtectionParameter()

will return

protection

.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

**Parameters:** type

- the type of KeyStore to be constructed
**Parameters:** provider

- the provider from which the KeyStore is to
be instantiated (or null)
**Parameters:** protection

- the ProtectionParameter securing the Keystore
**Returns:** a new Builder object
**Throws:** NullPointerException

- if type or protection is null

---

#### newInstance

public static

KeyStore.Builder

newInstance​(

String

type,

Provider

provider,

KeyStore.ProtectionParameter

protection)

Returns a new Builder object.

Each call to the

getKeyStore()

method on the returned
builder will return a new KeyStore object of type

type

.
Its

load()

method is invoked using a

LoadStoreParameter

that encapsulates

protection

.

The KeyStore is instantiated from

provider

if
non-null. Otherwise, all installed providers are searched.

Calls to

getProtectionParameter()

will return

protection

.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

Each call to the

getKeyStore()

method on the returned
builder will return a new KeyStore object of type

type

.
Its

load()

method is invoked using a

LoadStoreParameter

that encapsulates

protection

.

The KeyStore is instantiated from

provider

if
non-null. Otherwise, all installed providers are searched.

Calls to

getProtectionParameter()

will return

protection

.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

The KeyStore is instantiated from

provider

if
non-null. Otherwise, all installed providers are searched.

Calls to

getProtectionParameter()

will return

protection

.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

Calls to

getProtectionParameter()

will return

protection

.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

Note

that the

getKeyStore()

method is executed
within the

AccessControlContext

of the code invoking this
method.

---

