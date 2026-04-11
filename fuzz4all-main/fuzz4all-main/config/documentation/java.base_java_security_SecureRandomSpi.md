# Class SecureRandomSpi

**Source:** `java.base\java\security\SecureRandomSpi.html`

### Class Description

```java
public abstract class
SecureRandomSpi

extends
Object

implements
Serializable
```

This class defines the

Service Provider Interface

(

SPI

)
for the

SecureRandom

class.

All the abstract methods in this class must be implemented by each
service provider who wishes to supply the implementation
of a cryptographically strong pseudo-random number generator.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public SecureRandomSpi()

Constructor without a parameter.

---

#### protected SecureRandomSpi​(
SecureRandomParameters
params)

Constructor with a parameter.

**Parameters:**
- params

- the

SecureRandomParameters

object.
This argument can be

null

.

**Throws:**
- IllegalArgumentException

- if

params

is
unrecognizable or unsupported by this

SecureRandom

**Since:**
- 9

---

### Method Details

#### protected abstract void engineSetSeed​(byte[] seed)

Reseeds this random object with the given seed. The seed supplements,
rather than replaces, the existing seed. Thus, repeated calls
are guaranteed never to reduce randomness.

**Parameters:**
- seed

- the seed.

---

#### protected abstract void engineNextBytes​(byte[] bytes)

Generates a user-specified number of random bytes.

Some random number generators can only generate a limited amount
of random bytes per invocation. If the size of

bytes

is greater than this limit, the implementation should invoke
its generation process multiple times to completely fill the
buffer before returning from this method.

**Parameters:**
- bytes

- the array to be filled in with random bytes.

---

#### protected void engineNextBytes​(byte[] bytes,

SecureRandomParameters
params)

Generates a user-specified number of random bytes with
additional parameters.

Some random number generators can only generate a limited amount
of random bytes per invocation. If the size of

bytes

is greater than this limit, the implementation should invoke
its generation process multiple times to completely fill the
buffer before returning from this method.

**Parameters:**
- bytes

- the array to be filled in with random bytes
- params

- additional parameters

**Throws:**
- UnsupportedOperationException

- if the implementation
has not overridden this method
- IllegalArgumentException

- if

params

is

null

,
illegal or unsupported by this

SecureRandom

**Since:**
- 9

**Implementation Requirements:**
- The default implementation throws
an

UnsupportedOperationException

.

---

#### protected abstract byte[] engineGenerateSeed​(int numBytes)

Returns the given number of seed bytes. This call may be used to
seed other random number generators.

**Parameters:**
- numBytes

- the number of seed bytes to generate.

**Returns:**
- the seed bytes.

---

#### protected void engineReseed​(
SecureRandomParameters
params)

Reseeds this random object with entropy input read from its
entropy source with additional parameters.

If this method is called by

SecureRandom.reseed()

,

params

will be

null

.

Do not override this method if the implementation does not
support reseeding.

**Parameters:**
- params

- extra parameters, can be

null

.

**Throws:**
- UnsupportedOperationException

- if the implementation
has not overridden this method
- IllegalArgumentException

- if

params

is
illegal or unsupported by this

SecureRandom

**Since:**
- 9

**Implementation Requirements:**
- The default implementation throws
an

UnsupportedOperationException

.

---

#### protected
SecureRandomParameters
engineGetParameters()

Returns the effective

SecureRandomParameters

for this

SecureRandom

instance.

**Returns:**
- the effective

SecureRandomParameters

parameters,
or

null

if no parameters were used.

**Since:**
- 9

**Implementation Requirements:**
- The default implementation returns

null

.

---

#### public
String
toString()

Returns a Human-readable string representation of this

SecureRandom

.

**Overrides:**
- toString

in class

Object

**Returns:**
- the string representation

---

### Additional Sections

#### Class SecureRandomSpi

java.lang.Object

- java.security.SecureRandomSpi

java.security.SecureRandomSpi

**All Implemented Interfaces:** Serializable

```java
public abstract class
SecureRandomSpi

extends
Object

implements
Serializable
```

This class defines the

Service Provider Interface

(

SPI

)
for the

SecureRandom

class.

All the abstract methods in this class must be implemented by each
service provider who wishes to supply the implementation
of a cryptographically strong pseudo-random number generator.

**Implementation Requirements:** If the

SecureRandomSpi(SecureRandomParameters)

constructor is overridden in an implementation, it will always be called
whenever a

SecureRandom

is instantiated. Precisely, if an object is
instantiated with one of

SecureRandom

's

getInstance

methods

without

a

SecureRandomParameters

parameter,
the constructor will be called with a

null

argument and the
implementation is responsible for creating its own

SecureRandomParameters

parameter for use when

engineGetParameters()

is called. If an object
is instantiated with one of

SecureRandom

's

getInstance

methods

with

a

SecureRandomParameters

argument,
the constructor will be called with that argument. The

engineGetParameters()

method must not return

null

.

Otherwise, if the

SecureRandomSpi(SecureRandomParameters)

constructor is not overridden in an implementation, the

SecureRandomSpi()

constructor must be overridden and it will be
called if an object is instantiated with one of

SecureRandom

's

getInstance

methods

without

a

SecureRandomParameters

argument. Calling one of

SecureRandom

's

getInstance

methods

with

a

SecureRandomParameters

argument will never
return an instance of this implementation. The

engineGetParameters()

method must return

null

.

See

SecureRandom

for additional details on thread safety. By
default, a

SecureRandomSpi

implementation is considered to be
not safe for use by multiple concurrent threads and

SecureRandom

will synchronize access to each of the applicable engine methods
(see

SecureRandom

for the list of methods). However, if a

SecureRandomSpi

implementation is thread-safe, the

service provider attribute

"ThreadSafe" should be set to "true" during
its registration, as follows:

```java
put("SecureRandom.AlgName ThreadSafe", "true");
```

or

```java
putService(new Service(this, "SecureRandom", "AlgName", className,
null, Map.of("ThreadSafe", "true")));
```

SecureRandom

will call the applicable engine methods
without any synchronization.
**Since:** 1.2
**See Also:** Serialized Form

public abstract class

SecureRandomSpi

extends

Object

implements

Serializable

This class defines the

Service Provider Interface

(

SPI

)
for the

SecureRandom

class.

All the abstract methods in this class must be implemented by each
service provider who wishes to supply the implementation
of a cryptographically strong pseudo-random number generator.

All the abstract methods in this class must be implemented by each
service provider who wishes to supply the implementation
of a cryptographically strong pseudo-random number generator.

Otherwise, if the

SecureRandomSpi(SecureRandomParameters)

constructor is not overridden in an implementation, the

SecureRandomSpi()

constructor must be overridden and it will be
called if an object is instantiated with one of

SecureRandom

's

getInstance

methods

without

a

SecureRandomParameters

argument. Calling one of

SecureRandom

's

getInstance

methods

with

a

SecureRandomParameters

argument will never
return an instance of this implementation. The

engineGetParameters()

method must return

null

.

See

SecureRandom

for additional details on thread safety. By
default, a

SecureRandomSpi

implementation is considered to be
not safe for use by multiple concurrent threads and

SecureRandom

will synchronize access to each of the applicable engine methods
(see

SecureRandom

for the list of methods). However, if a

SecureRandomSpi

implementation is thread-safe, the

service provider attribute

"ThreadSafe" should be set to "true" during
its registration, as follows:

```java
put("SecureRandom.AlgName ThreadSafe", "true");
```

or

```java
putService(new Service(this, "SecureRandom", "AlgName", className,
null, Map.of("ThreadSafe", "true")));
```

SecureRandom

will call the applicable engine methods
without any synchronization.

See

SecureRandom

for additional details on thread safety. By
default, a

SecureRandomSpi

implementation is considered to be
not safe for use by multiple concurrent threads and

SecureRandom

will synchronize access to each of the applicable engine methods
(see

SecureRandom

for the list of methods). However, if a

SecureRandomSpi

implementation is thread-safe, the

service provider attribute

"ThreadSafe" should be set to "true" during
its registration, as follows:

```java
put("SecureRandom.AlgName ThreadSafe", "true");
```

or

```java
putService(new Service(this, "SecureRandom", "AlgName", className,
null, Map.of("ThreadSafe", "true")));
```

SecureRandom

will call the applicable engine methods
without any synchronization.

put("SecureRandom.AlgName ThreadSafe", "true");

putService(new Service(this, "SecureRandom", "AlgName", className,
null, Map.of("ThreadSafe", "true")));

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

SecureRandomSpi

()

Constructor without a parameter.

protected

SecureRandomSpi

​(

SecureRandomParameters

params)

Constructor with a parameter.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected abstract byte[]

engineGenerateSeed

​(int numBytes)

Returns the given number of seed bytes.

protected

SecureRandomParameters

engineGetParameters

()

Returns the effective

SecureRandomParameters

for this

SecureRandom

instance.

protected abstract void

engineNextBytes

​(byte[] bytes)

Generates a user-specified number of random bytes.

protected void

engineNextBytes

​(byte[] bytes,

SecureRandomParameters

params)

Generates a user-specified number of random bytes with
additional parameters.

protected void

engineReseed

​(

SecureRandomParameters

params)

Reseeds this random object with entropy input read from its
entropy source with additional parameters.

protected abstract void

engineSetSeed

​(byte[] seed)

Reseeds this random object with the given seed.

String

toString

()

Returns a Human-readable string representation of this

SecureRandom

.

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

SecureRandomSpi

()

Constructor without a parameter.

protected

SecureRandomSpi

​(

SecureRandomParameters

params)

Constructor with a parameter.

---

#### Constructor Summary

Constructor without a parameter.

Constructor with a parameter.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected abstract byte[]

engineGenerateSeed

​(int numBytes)

Returns the given number of seed bytes.

protected

SecureRandomParameters

engineGetParameters

()

Returns the effective

SecureRandomParameters

for this

SecureRandom

instance.

protected abstract void

engineNextBytes

​(byte[] bytes)

Generates a user-specified number of random bytes.

protected void

engineNextBytes

​(byte[] bytes,

SecureRandomParameters

params)

Generates a user-specified number of random bytes with
additional parameters.

protected void

engineReseed

​(

SecureRandomParameters

params)

Reseeds this random object with entropy input read from its
entropy source with additional parameters.

protected abstract void

engineSetSeed

​(byte[] seed)

Reseeds this random object with the given seed.

String

toString

()

Returns a Human-readable string representation of this

SecureRandom

.

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

wait

,

wait

,

wait

---

#### Method Summary

Returns the given number of seed bytes.

Returns the effective

SecureRandomParameters

for this

SecureRandom

instance.

Generates a user-specified number of random bytes.

Generates a user-specified number of random bytes with
additional parameters.

Reseeds this random object with entropy input read from its
entropy source with additional parameters.

Reseeds this random object with the given seed.

Returns a Human-readable string representation of this

SecureRandom

.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SecureRandomSpi

```java
public SecureRandomSpi()
```

Constructor without a parameter.

- SecureRandomSpi

```java
protected SecureRandomSpi​(
SecureRandomParameters
params)
```

Constructor with a parameter.

**Parameters:** params

- the

SecureRandomParameters

object.
This argument can be

null

.
**Throws:** IllegalArgumentException

- if

params

is
unrecognizable or unsupported by this

SecureRandom
**Since:** 9

============ METHOD DETAIL ==========

- Method Detail

- engineSetSeed

```java
protected abstract void engineSetSeed​(byte[] seed)
```

Reseeds this random object with the given seed. The seed supplements,
rather than replaces, the existing seed. Thus, repeated calls
are guaranteed never to reduce randomness.

**Parameters:** seed

- the seed.

- engineNextBytes

```java
protected abstract void engineNextBytes​(byte[] bytes)
```

Generates a user-specified number of random bytes.

Some random number generators can only generate a limited amount
of random bytes per invocation. If the size of

bytes

is greater than this limit, the implementation should invoke
its generation process multiple times to completely fill the
buffer before returning from this method.

**Parameters:** bytes

- the array to be filled in with random bytes.

- engineNextBytes

```java
protected void engineNextBytes​(byte[] bytes,

SecureRandomParameters
params)
```

Generates a user-specified number of random bytes with
additional parameters.

Some random number generators can only generate a limited amount
of random bytes per invocation. If the size of

bytes

is greater than this limit, the implementation should invoke
its generation process multiple times to completely fill the
buffer before returning from this method.

**Implementation Requirements:** The default implementation throws
an

UnsupportedOperationException

.
**Parameters:** bytes

- the array to be filled in with random bytes
**Parameters:** params

- additional parameters
**Throws:** UnsupportedOperationException

- if the implementation
has not overridden this method
**Throws:** IllegalArgumentException

- if

params

is

null

,
illegal or unsupported by this

SecureRandom
**Since:** 9

- engineGenerateSeed

```java
protected abstract byte[] engineGenerateSeed​(int numBytes)
```

Returns the given number of seed bytes. This call may be used to
seed other random number generators.

**Parameters:** numBytes

- the number of seed bytes to generate.
**Returns:** the seed bytes.

- engineReseed

```java
protected void engineReseed​(
SecureRandomParameters
params)
```

Reseeds this random object with entropy input read from its
entropy source with additional parameters.

If this method is called by

SecureRandom.reseed()

,

params

will be

null

.

Do not override this method if the implementation does not
support reseeding.

**Implementation Requirements:** The default implementation throws
an

UnsupportedOperationException

.
**Parameters:** params

- extra parameters, can be

null

.
**Throws:** UnsupportedOperationException

- if the implementation
has not overridden this method
**Throws:** IllegalArgumentException

- if

params

is
illegal or unsupported by this

SecureRandom
**Since:** 9

- engineGetParameters

```java
protected
SecureRandomParameters
engineGetParameters()
```

Returns the effective

SecureRandomParameters

for this

SecureRandom

instance.

**Implementation Requirements:** The default implementation returns

null

.
**Returns:** the effective

SecureRandomParameters

parameters,
or

null

if no parameters were used.
**Since:** 9

- toString

```java
public
String
toString()
```

Returns a Human-readable string representation of this

SecureRandom

.

**Overrides:** toString

in class

Object
**Returns:** the string representation

Constructor Detail

- SecureRandomSpi

```java
public SecureRandomSpi()
```

Constructor without a parameter.

- SecureRandomSpi

```java
protected SecureRandomSpi​(
SecureRandomParameters
params)
```

Constructor with a parameter.

**Parameters:** params

- the

SecureRandomParameters

object.
This argument can be

null

.
**Throws:** IllegalArgumentException

- if

params

is
unrecognizable or unsupported by this

SecureRandom
**Since:** 9

---

#### Constructor Detail

SecureRandomSpi

```java
public SecureRandomSpi()
```

Constructor without a parameter.

---

#### SecureRandomSpi

public SecureRandomSpi()

Constructor without a parameter.

SecureRandomSpi

```java
protected SecureRandomSpi​(
SecureRandomParameters
params)
```

Constructor with a parameter.

**Parameters:** params

- the

SecureRandomParameters

object.
This argument can be

null

.
**Throws:** IllegalArgumentException

- if

params

is
unrecognizable or unsupported by this

SecureRandom
**Since:** 9

---

#### SecureRandomSpi

protected SecureRandomSpi​(

SecureRandomParameters

params)

Constructor with a parameter.

Method Detail

- engineSetSeed

```java
protected abstract void engineSetSeed​(byte[] seed)
```

Reseeds this random object with the given seed. The seed supplements,
rather than replaces, the existing seed. Thus, repeated calls
are guaranteed never to reduce randomness.

**Parameters:** seed

- the seed.

- engineNextBytes

```java
protected abstract void engineNextBytes​(byte[] bytes)
```

Generates a user-specified number of random bytes.

Some random number generators can only generate a limited amount
of random bytes per invocation. If the size of

bytes

is greater than this limit, the implementation should invoke
its generation process multiple times to completely fill the
buffer before returning from this method.

**Parameters:** bytes

- the array to be filled in with random bytes.

- engineNextBytes

```java
protected void engineNextBytes​(byte[] bytes,

SecureRandomParameters
params)
```

Generates a user-specified number of random bytes with
additional parameters.

Some random number generators can only generate a limited amount
of random bytes per invocation. If the size of

bytes

is greater than this limit, the implementation should invoke
its generation process multiple times to completely fill the
buffer before returning from this method.

**Implementation Requirements:** The default implementation throws
an

UnsupportedOperationException

.
**Parameters:** bytes

- the array to be filled in with random bytes
**Parameters:** params

- additional parameters
**Throws:** UnsupportedOperationException

- if the implementation
has not overridden this method
**Throws:** IllegalArgumentException

- if

params

is

null

,
illegal or unsupported by this

SecureRandom
**Since:** 9

- engineGenerateSeed

```java
protected abstract byte[] engineGenerateSeed​(int numBytes)
```

Returns the given number of seed bytes. This call may be used to
seed other random number generators.

**Parameters:** numBytes

- the number of seed bytes to generate.
**Returns:** the seed bytes.

- engineReseed

```java
protected void engineReseed​(
SecureRandomParameters
params)
```

Reseeds this random object with entropy input read from its
entropy source with additional parameters.

If this method is called by

SecureRandom.reseed()

,

params

will be

null

.

Do not override this method if the implementation does not
support reseeding.

**Implementation Requirements:** The default implementation throws
an

UnsupportedOperationException

.
**Parameters:** params

- extra parameters, can be

null

.
**Throws:** UnsupportedOperationException

- if the implementation
has not overridden this method
**Throws:** IllegalArgumentException

- if

params

is
illegal or unsupported by this

SecureRandom
**Since:** 9

- engineGetParameters

```java
protected
SecureRandomParameters
engineGetParameters()
```

Returns the effective

SecureRandomParameters

for this

SecureRandom

instance.

**Implementation Requirements:** The default implementation returns

null

.
**Returns:** the effective

SecureRandomParameters

parameters,
or

null

if no parameters were used.
**Since:** 9

- toString

```java
public
String
toString()
```

Returns a Human-readable string representation of this

SecureRandom

.

**Overrides:** toString

in class

Object
**Returns:** the string representation

---

#### Method Detail

engineSetSeed

```java
protected abstract void engineSetSeed​(byte[] seed)
```

Reseeds this random object with the given seed. The seed supplements,
rather than replaces, the existing seed. Thus, repeated calls
are guaranteed never to reduce randomness.

**Parameters:** seed

- the seed.

---

#### engineSetSeed

protected abstract void engineSetSeed​(byte[] seed)

Reseeds this random object with the given seed. The seed supplements,
rather than replaces, the existing seed. Thus, repeated calls
are guaranteed never to reduce randomness.

engineNextBytes

```java
protected abstract void engineNextBytes​(byte[] bytes)
```

Generates a user-specified number of random bytes.

Some random number generators can only generate a limited amount
of random bytes per invocation. If the size of

bytes

is greater than this limit, the implementation should invoke
its generation process multiple times to completely fill the
buffer before returning from this method.

**Parameters:** bytes

- the array to be filled in with random bytes.

---

#### engineNextBytes

protected abstract void engineNextBytes​(byte[] bytes)

Generates a user-specified number of random bytes.

Some random number generators can only generate a limited amount
of random bytes per invocation. If the size of

bytes

is greater than this limit, the implementation should invoke
its generation process multiple times to completely fill the
buffer before returning from this method.

Some random number generators can only generate a limited amount
of random bytes per invocation. If the size of

bytes

is greater than this limit, the implementation should invoke
its generation process multiple times to completely fill the
buffer before returning from this method.

engineNextBytes

```java
protected void engineNextBytes​(byte[] bytes,

SecureRandomParameters
params)
```

Generates a user-specified number of random bytes with
additional parameters.

Some random number generators can only generate a limited amount
of random bytes per invocation. If the size of

bytes

is greater than this limit, the implementation should invoke
its generation process multiple times to completely fill the
buffer before returning from this method.

**Implementation Requirements:** The default implementation throws
an

UnsupportedOperationException

.
**Parameters:** bytes

- the array to be filled in with random bytes
**Parameters:** params

- additional parameters
**Throws:** UnsupportedOperationException

- if the implementation
has not overridden this method
**Throws:** IllegalArgumentException

- if

params

is

null

,
illegal or unsupported by this

SecureRandom
**Since:** 9

---

#### engineNextBytes

protected void engineNextBytes​(byte[] bytes,

SecureRandomParameters

params)

Generates a user-specified number of random bytes with
additional parameters.

Some random number generators can only generate a limited amount
of random bytes per invocation. If the size of

bytes

is greater than this limit, the implementation should invoke
its generation process multiple times to completely fill the
buffer before returning from this method.

Some random number generators can only generate a limited amount
of random bytes per invocation. If the size of

bytes

is greater than this limit, the implementation should invoke
its generation process multiple times to completely fill the
buffer before returning from this method.

engineGenerateSeed

```java
protected abstract byte[] engineGenerateSeed​(int numBytes)
```

Returns the given number of seed bytes. This call may be used to
seed other random number generators.

**Parameters:** numBytes

- the number of seed bytes to generate.
**Returns:** the seed bytes.

---

#### engineGenerateSeed

protected abstract byte[] engineGenerateSeed​(int numBytes)

Returns the given number of seed bytes. This call may be used to
seed other random number generators.

engineReseed

```java
protected void engineReseed​(
SecureRandomParameters
params)
```

Reseeds this random object with entropy input read from its
entropy source with additional parameters.

If this method is called by

SecureRandom.reseed()

,

params

will be

null

.

Do not override this method if the implementation does not
support reseeding.

**Implementation Requirements:** The default implementation throws
an

UnsupportedOperationException

.
**Parameters:** params

- extra parameters, can be

null

.
**Throws:** UnsupportedOperationException

- if the implementation
has not overridden this method
**Throws:** IllegalArgumentException

- if

params

is
illegal or unsupported by this

SecureRandom
**Since:** 9

---

#### engineReseed

protected void engineReseed​(

SecureRandomParameters

params)

Reseeds this random object with entropy input read from its
entropy source with additional parameters.

If this method is called by

SecureRandom.reseed()

,

params

will be

null

.

Do not override this method if the implementation does not
support reseeding.

If this method is called by

SecureRandom.reseed()

,

params

will be

null

.

Do not override this method if the implementation does not
support reseeding.

Do not override this method if the implementation does not
support reseeding.

engineGetParameters

```java
protected
SecureRandomParameters
engineGetParameters()
```

Returns the effective

SecureRandomParameters

for this

SecureRandom

instance.

**Implementation Requirements:** The default implementation returns

null

.
**Returns:** the effective

SecureRandomParameters

parameters,
or

null

if no parameters were used.
**Since:** 9

---

#### engineGetParameters

protected

SecureRandomParameters

engineGetParameters()

Returns the effective

SecureRandomParameters

for this

SecureRandom

instance.

toString

```java
public
String
toString()
```

Returns a Human-readable string representation of this

SecureRandom

.

**Overrides:** toString

in class

Object
**Returns:** the string representation

---

#### toString

public

String

toString()

Returns a Human-readable string representation of this

SecureRandom

.

---

