# Class CollectionCertStoreParameters

**Source:** `java.base\java\security\cert\CollectionCertStoreParameters.html`

### Class Description

```java
public class
CollectionCertStoreParameters

extends
Object

implements
CertStoreParameters
```

Parameters used as input for the Collection

CertStore

algorithm.

This class is used to provide necessary configuration parameters
to implementations of the Collection

CertStore

algorithm. The only parameter included in this class is the

Collection

from which the

CertStore

will
retrieve certificates and CRLs.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

**All Implemented Interfaces:** Cloneable

,

CertStoreParameters

---

### Field Details

*No entries found.*

### Constructor Details

#### public CollectionCertStoreParameters​(
Collection
<?> collection)

Creates an instance of

CollectionCertStoreParameters

which will allow certificates and CRLs to be retrieved from the
specified

Collection

. If the specified

Collection

contains an object that is not a

Certificate

or

CRL

, that object will be
ignored by the Collection

CertStore

.

The

Collection

is

not

copied. Instead, a
reference is used. This allows the caller to subsequently add or
remove

Certificates

or

CRL

s from the

Collection

, thus changing the set of

Certificates

or

CRL

s available to the
Collection

CertStore

. The Collection

CertStore

will not modify the contents of the

Collection

.

If the

Collection

will be modified by one thread while
another thread is calling a method of a Collection

CertStore

that has been initialized with this

Collection

, the

Collection

must have fail-fast iterators.

**Parameters:**
- collection

- a

Collection

of

Certificate

s and

CRL

s

**Throws:**
- NullPointerException

- if

collection

is

null

---

#### public CollectionCertStoreParameters()

Creates an instance of

CollectionCertStoreParameters

with
the default parameter values (an empty and immutable

Collection

).

---

### Method Details

#### public
Collection
<?> getCollection()

Returns the

Collection

from which

Certificate

s
and

CRL

s are retrieved. This is

not

a copy of the

Collection

, it is a reference. This allows the caller to
subsequently add or remove

Certificates

or

CRL

s from the

Collection

.

**Returns:**
- the

Collection

(never null)

---

#### public
Object
clone()

Returns a copy of this object. Note that only a reference to the

Collection

is copied, and not the contents.

**Specified by:**
- clone

in interface

CertStoreParameters

**Overrides:**
- clone

in class

Object

**Returns:**
- the copy

**See Also:**
- Cloneable

---

#### public
String
toString()

Returns a formatted string describing the parameters.

**Overrides:**
- toString

in class

Object

**Returns:**
- a formatted string describing the parameters

---

### Additional Sections

#### Class CollectionCertStoreParameters

java.lang.Object

- java.security.cert.CollectionCertStoreParameters

java.security.cert.CollectionCertStoreParameters

**All Implemented Interfaces:** Cloneable

,

CertStoreParameters

```java
public class
CollectionCertStoreParameters

extends
Object

implements
CertStoreParameters
```

Parameters used as input for the Collection

CertStore

algorithm.

This class is used to provide necessary configuration parameters
to implementations of the Collection

CertStore

algorithm. The only parameter included in this class is the

Collection

from which the

CertStore

will
retrieve certificates and CRLs.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

**Since:** 1.4
**See Also:** Collection

,

CertStore

public class

CollectionCertStoreParameters

extends

Object

implements

CertStoreParameters

Parameters used as input for the Collection

CertStore

algorithm.

This class is used to provide necessary configuration parameters
to implementations of the Collection

CertStore

algorithm. The only parameter included in this class is the

Collection

from which the

CertStore

will
retrieve certificates and CRLs.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

This class is used to provide necessary configuration parameters
to implementations of the Collection

CertStore

algorithm. The only parameter included in this class is the

Collection

from which the

CertStore

will
retrieve certificates and CRLs.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CollectionCertStoreParameters

()

Creates an instance of

CollectionCertStoreParameters

with
the default parameter values (an empty and immutable

Collection

).

CollectionCertStoreParameters

​(

Collection

<?> collection)

Creates an instance of

CollectionCertStoreParameters

which will allow certificates and CRLs to be retrieved from the
specified

Collection

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a copy of this object.

Collection

<?>

getCollection

()

Returns the

Collection

from which

Certificate

s
and

CRL

s are retrieved.

String

toString

()

Returns a formatted string describing the parameters.

- Methods declared in class java.lang.

Object

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

Constructor

Description

CollectionCertStoreParameters

()

Creates an instance of

CollectionCertStoreParameters

with
the default parameter values (an empty and immutable

Collection

).

CollectionCertStoreParameters

​(

Collection

<?> collection)

Creates an instance of

CollectionCertStoreParameters

which will allow certificates and CRLs to be retrieved from the
specified

Collection

.

---

#### Constructor Summary

Creates an instance of

CollectionCertStoreParameters

with
the default parameter values (an empty and immutable

Collection

).

Creates an instance of

CollectionCertStoreParameters

which will allow certificates and CRLs to be retrieved from the
specified

Collection

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a copy of this object.

Collection

<?>

getCollection

()

Returns the

Collection

from which

Certificate

s
and

CRL

s are retrieved.

String

toString

()

Returns a formatted string describing the parameters.

- Methods declared in class java.lang.

Object

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

Returns a copy of this object.

Returns the

Collection

from which

Certificate

s
and

CRL

s are retrieved.

Returns a formatted string describing the parameters.

Methods declared in class java.lang.

Object

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

- CollectionCertStoreParameters

```java
public CollectionCertStoreParameters​(
Collection
<?> collection)
```

Creates an instance of

CollectionCertStoreParameters

which will allow certificates and CRLs to be retrieved from the
specified

Collection

. If the specified

Collection

contains an object that is not a

Certificate

or

CRL

, that object will be
ignored by the Collection

CertStore

.

The

Collection

is

not

copied. Instead, a
reference is used. This allows the caller to subsequently add or
remove

Certificates

or

CRL

s from the

Collection

, thus changing the set of

Certificates

or

CRL

s available to the
Collection

CertStore

. The Collection

CertStore

will not modify the contents of the

Collection

.

If the

Collection

will be modified by one thread while
another thread is calling a method of a Collection

CertStore

that has been initialized with this

Collection

, the

Collection

must have fail-fast iterators.

**Parameters:** collection

- a

Collection

of

Certificate

s and

CRL

s
**Throws:** NullPointerException

- if

collection

is

null

- CollectionCertStoreParameters

```java
public CollectionCertStoreParameters()
```

Creates an instance of

CollectionCertStoreParameters

with
the default parameter values (an empty and immutable

Collection

).

============ METHOD DETAIL ==========

- Method Detail

- getCollection

```java
public
Collection
<?> getCollection()
```

Returns the

Collection

from which

Certificate

s
and

CRL

s are retrieved. This is

not

a copy of the

Collection

, it is a reference. This allows the caller to
subsequently add or remove

Certificates

or

CRL

s from the

Collection

.

**Returns:** the

Collection

(never null)

- clone

```java
public
Object
clone()
```

Returns a copy of this object. Note that only a reference to the

Collection

is copied, and not the contents.

**Specified by:** clone

in interface

CertStoreParameters
**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

- toString

```java
public
String
toString()
```

Returns a formatted string describing the parameters.

**Overrides:** toString

in class

Object
**Returns:** a formatted string describing the parameters

Constructor Detail

- CollectionCertStoreParameters

```java
public CollectionCertStoreParameters​(
Collection
<?> collection)
```

Creates an instance of

CollectionCertStoreParameters

which will allow certificates and CRLs to be retrieved from the
specified

Collection

. If the specified

Collection

contains an object that is not a

Certificate

or

CRL

, that object will be
ignored by the Collection

CertStore

.

The

Collection

is

not

copied. Instead, a
reference is used. This allows the caller to subsequently add or
remove

Certificates

or

CRL

s from the

Collection

, thus changing the set of

Certificates

or

CRL

s available to the
Collection

CertStore

. The Collection

CertStore

will not modify the contents of the

Collection

.

If the

Collection

will be modified by one thread while
another thread is calling a method of a Collection

CertStore

that has been initialized with this

Collection

, the

Collection

must have fail-fast iterators.

**Parameters:** collection

- a

Collection

of

Certificate

s and

CRL

s
**Throws:** NullPointerException

- if

collection

is

null

- CollectionCertStoreParameters

```java
public CollectionCertStoreParameters()
```

Creates an instance of

CollectionCertStoreParameters

with
the default parameter values (an empty and immutable

Collection

).

---

#### Constructor Detail

CollectionCertStoreParameters

```java
public CollectionCertStoreParameters​(
Collection
<?> collection)
```

Creates an instance of

CollectionCertStoreParameters

which will allow certificates and CRLs to be retrieved from the
specified

Collection

. If the specified

Collection

contains an object that is not a

Certificate

or

CRL

, that object will be
ignored by the Collection

CertStore

.

The

Collection

is

not

copied. Instead, a
reference is used. This allows the caller to subsequently add or
remove

Certificates

or

CRL

s from the

Collection

, thus changing the set of

Certificates

or

CRL

s available to the
Collection

CertStore

. The Collection

CertStore

will not modify the contents of the

Collection

.

If the

Collection

will be modified by one thread while
another thread is calling a method of a Collection

CertStore

that has been initialized with this

Collection

, the

Collection

must have fail-fast iterators.

**Parameters:** collection

- a

Collection

of

Certificate

s and

CRL

s
**Throws:** NullPointerException

- if

collection

is

null

---

#### CollectionCertStoreParameters

public CollectionCertStoreParameters​(

Collection

<?> collection)

Creates an instance of

CollectionCertStoreParameters

which will allow certificates and CRLs to be retrieved from the
specified

Collection

. If the specified

Collection

contains an object that is not a

Certificate

or

CRL

, that object will be
ignored by the Collection

CertStore

.

The

Collection

is

not

copied. Instead, a
reference is used. This allows the caller to subsequently add or
remove

Certificates

or

CRL

s from the

Collection

, thus changing the set of

Certificates

or

CRL

s available to the
Collection

CertStore

. The Collection

CertStore

will not modify the contents of the

Collection

.

If the

Collection

will be modified by one thread while
another thread is calling a method of a Collection

CertStore

that has been initialized with this

Collection

, the

Collection

must have fail-fast iterators.

The

Collection

is

not

copied. Instead, a
reference is used. This allows the caller to subsequently add or
remove

Certificates

or

CRL

s from the

Collection

, thus changing the set of

Certificates

or

CRL

s available to the
Collection

CertStore

. The Collection

CertStore

will not modify the contents of the

Collection

.

If the

Collection

will be modified by one thread while
another thread is calling a method of a Collection

CertStore

that has been initialized with this

Collection

, the

Collection

must have fail-fast iterators.

If the

Collection

will be modified by one thread while
another thread is calling a method of a Collection

CertStore

that has been initialized with this

Collection

, the

Collection

must have fail-fast iterators.

CollectionCertStoreParameters

```java
public CollectionCertStoreParameters()
```

Creates an instance of

CollectionCertStoreParameters

with
the default parameter values (an empty and immutable

Collection

).

---

#### CollectionCertStoreParameters

public CollectionCertStoreParameters()

Creates an instance of

CollectionCertStoreParameters

with
the default parameter values (an empty and immutable

Collection

).

Method Detail

- getCollection

```java
public
Collection
<?> getCollection()
```

Returns the

Collection

from which

Certificate

s
and

CRL

s are retrieved. This is

not

a copy of the

Collection

, it is a reference. This allows the caller to
subsequently add or remove

Certificates

or

CRL

s from the

Collection

.

**Returns:** the

Collection

(never null)

- clone

```java
public
Object
clone()
```

Returns a copy of this object. Note that only a reference to the

Collection

is copied, and not the contents.

**Specified by:** clone

in interface

CertStoreParameters
**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

- toString

```java
public
String
toString()
```

Returns a formatted string describing the parameters.

**Overrides:** toString

in class

Object
**Returns:** a formatted string describing the parameters

---

#### Method Detail

getCollection

```java
public
Collection
<?> getCollection()
```

Returns the

Collection

from which

Certificate

s
and

CRL

s are retrieved. This is

not

a copy of the

Collection

, it is a reference. This allows the caller to
subsequently add or remove

Certificates

or

CRL

s from the

Collection

.

**Returns:** the

Collection

(never null)

---

#### getCollection

public

Collection

<?> getCollection()

Returns the

Collection

from which

Certificate

s
and

CRL

s are retrieved. This is

not

a copy of the

Collection

, it is a reference. This allows the caller to
subsequently add or remove

Certificates

or

CRL

s from the

Collection

.

clone

```java
public
Object
clone()
```

Returns a copy of this object. Note that only a reference to the

Collection

is copied, and not the contents.

**Specified by:** clone

in interface

CertStoreParameters
**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a copy of this object. Note that only a reference to the

Collection

is copied, and not the contents.

toString

```java
public
String
toString()
```

Returns a formatted string describing the parameters.

**Overrides:** toString

in class

Object
**Returns:** a formatted string describing the parameters

---

#### toString

public

String

toString()

Returns a formatted string describing the parameters.

---

