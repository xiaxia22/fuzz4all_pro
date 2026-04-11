# Interface CertStoreParameters

**Source:** `java.base\java\security\cert\CertStoreParameters.html`

### Class Description

```java
public interface
CertStoreParameters

extends
Cloneable
```

A specification of

CertStore

parameters.

The purpose of this interface is to group (and provide type safety for)
all

CertStore

parameter specifications. All

CertStore

parameter specifications must implement this
interface.

Typically, a

CertStoreParameters

object is passed as a parameter
to one of the

CertStore.getInstance

methods.
The

getInstance

method returns a

CertStore

that
is used for retrieving

Certificate

s and

CRL

s. The

CertStore

that is returned is initialized with the specified
parameters. The type of parameters needed may vary between different types
of

CertStore

s.

**All Superinterfaces:** Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
clone()

Makes a copy of this

CertStoreParameters

.

The precise meaning of "copy" may depend on the class of
the

CertStoreParameters

object. A typical implementation
performs a "deep copy" of this object, but this is not an absolute
requirement. Some implementations may perform a "shallow copy" of some
or all of the fields of this object.

Note that the

CertStore.getInstance

methods make a copy
of the specified

CertStoreParameters

. A deep copy
implementation of

clone

is safer and more robust, as it
prevents the caller from corrupting a shared

CertStore

by
subsequently modifying the contents of its initialization parameters.
However, a shallow copy implementation of

clone

is more
appropriate for applications that need to hold a reference to a
parameter contained in the

CertStoreParameters

. For example,
a shallow copy clone allows an application to release the resources of
a particular

CertStore

initialization parameter immediately,
rather than waiting for the garbage collection mechanism. This should
be done with the utmost care, since the

CertStore

may still
be in use by other threads.

Each subclass should state the precise behavior of this method so
that users and developers know what to expect.

**Returns:**
- a copy of this

CertStoreParameters

---

### Additional Sections

#### Interface CertStoreParameters

**All Superinterfaces:** Cloneable

**All Known Implementing Classes:** CollectionCertStoreParameters

,

LDAPCertStoreParameters

,

URICertStoreParameters

```java
public interface
CertStoreParameters

extends
Cloneable
```

A specification of

CertStore

parameters.

The purpose of this interface is to group (and provide type safety for)
all

CertStore

parameter specifications. All

CertStore

parameter specifications must implement this
interface.

Typically, a

CertStoreParameters

object is passed as a parameter
to one of the

CertStore.getInstance

methods.
The

getInstance

method returns a

CertStore

that
is used for retrieving

Certificate

s and

CRL

s. The

CertStore

that is returned is initialized with the specified
parameters. The type of parameters needed may vary between different types
of

CertStore

s.

**Since:** 1.4
**See Also:** CertStore.getInstance(java.lang.String, java.security.cert.CertStoreParameters)

public interface

CertStoreParameters

extends

Cloneable

A specification of

CertStore

parameters.

The purpose of this interface is to group (and provide type safety for)
all

CertStore

parameter specifications. All

CertStore

parameter specifications must implement this
interface.

Typically, a

CertStoreParameters

object is passed as a parameter
to one of the

CertStore.getInstance

methods.
The

getInstance

method returns a

CertStore

that
is used for retrieving

Certificate

s and

CRL

s. The

CertStore

that is returned is initialized with the specified
parameters. The type of parameters needed may vary between different types
of

CertStore

s.

The purpose of this interface is to group (and provide type safety for)
all

CertStore

parameter specifications. All

CertStore

parameter specifications must implement this
interface.

Typically, a

CertStoreParameters

object is passed as a parameter
to one of the

CertStore.getInstance

methods.
The

getInstance

method returns a

CertStore

that
is used for retrieving

Certificate

s and

CRL

s. The

CertStore

that is returned is initialized with the specified
parameters. The type of parameters needed may vary between different types
of

CertStore

s.

Typically, a

CertStoreParameters

object is passed as a parameter
to one of the

CertStore.getInstance

methods.
The

getInstance

method returns a

CertStore

that
is used for retrieving

Certificate

s and

CRL

s. The

CertStore

that is returned is initialized with the specified
parameters. The type of parameters needed may vary between different types
of

CertStore

s.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

clone

()

Makes a copy of this

CertStoreParameters

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

clone

()

Makes a copy of this

CertStoreParameters

.

---

#### Method Summary

Makes a copy of this

CertStoreParameters

.

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
Object
clone()
```

Makes a copy of this

CertStoreParameters

.

The precise meaning of "copy" may depend on the class of
the

CertStoreParameters

object. A typical implementation
performs a "deep copy" of this object, but this is not an absolute
requirement. Some implementations may perform a "shallow copy" of some
or all of the fields of this object.

Note that the

CertStore.getInstance

methods make a copy
of the specified

CertStoreParameters

. A deep copy
implementation of

clone

is safer and more robust, as it
prevents the caller from corrupting a shared

CertStore

by
subsequently modifying the contents of its initialization parameters.
However, a shallow copy implementation of

clone

is more
appropriate for applications that need to hold a reference to a
parameter contained in the

CertStoreParameters

. For example,
a shallow copy clone allows an application to release the resources of
a particular

CertStore

initialization parameter immediately,
rather than waiting for the garbage collection mechanism. This should
be done with the utmost care, since the

CertStore

may still
be in use by other threads.

Each subclass should state the precise behavior of this method so
that users and developers know what to expect.

**Returns:** a copy of this

CertStoreParameters

Method Detail

- clone

```java
Object
clone()
```

Makes a copy of this

CertStoreParameters

.

The precise meaning of "copy" may depend on the class of
the

CertStoreParameters

object. A typical implementation
performs a "deep copy" of this object, but this is not an absolute
requirement. Some implementations may perform a "shallow copy" of some
or all of the fields of this object.

Note that the

CertStore.getInstance

methods make a copy
of the specified

CertStoreParameters

. A deep copy
implementation of

clone

is safer and more robust, as it
prevents the caller from corrupting a shared

CertStore

by
subsequently modifying the contents of its initialization parameters.
However, a shallow copy implementation of

clone

is more
appropriate for applications that need to hold a reference to a
parameter contained in the

CertStoreParameters

. For example,
a shallow copy clone allows an application to release the resources of
a particular

CertStore

initialization parameter immediately,
rather than waiting for the garbage collection mechanism. This should
be done with the utmost care, since the

CertStore

may still
be in use by other threads.

Each subclass should state the precise behavior of this method so
that users and developers know what to expect.

**Returns:** a copy of this

CertStoreParameters

---

#### Method Detail

clone

```java
Object
clone()
```

Makes a copy of this

CertStoreParameters

.

The precise meaning of "copy" may depend on the class of
the

CertStoreParameters

object. A typical implementation
performs a "deep copy" of this object, but this is not an absolute
requirement. Some implementations may perform a "shallow copy" of some
or all of the fields of this object.

Note that the

CertStore.getInstance

methods make a copy
of the specified

CertStoreParameters

. A deep copy
implementation of

clone

is safer and more robust, as it
prevents the caller from corrupting a shared

CertStore

by
subsequently modifying the contents of its initialization parameters.
However, a shallow copy implementation of

clone

is more
appropriate for applications that need to hold a reference to a
parameter contained in the

CertStoreParameters

. For example,
a shallow copy clone allows an application to release the resources of
a particular

CertStore

initialization parameter immediately,
rather than waiting for the garbage collection mechanism. This should
be done with the utmost care, since the

CertStore

may still
be in use by other threads.

Each subclass should state the precise behavior of this method so
that users and developers know what to expect.

**Returns:** a copy of this

CertStoreParameters

---

#### clone

Object

clone()

Makes a copy of this

CertStoreParameters

.

The precise meaning of "copy" may depend on the class of
the

CertStoreParameters

object. A typical implementation
performs a "deep copy" of this object, but this is not an absolute
requirement. Some implementations may perform a "shallow copy" of some
or all of the fields of this object.

Note that the

CertStore.getInstance

methods make a copy
of the specified

CertStoreParameters

. A deep copy
implementation of

clone

is safer and more robust, as it
prevents the caller from corrupting a shared

CertStore

by
subsequently modifying the contents of its initialization parameters.
However, a shallow copy implementation of

clone

is more
appropriate for applications that need to hold a reference to a
parameter contained in the

CertStoreParameters

. For example,
a shallow copy clone allows an application to release the resources of
a particular

CertStore

initialization parameter immediately,
rather than waiting for the garbage collection mechanism. This should
be done with the utmost care, since the

CertStore

may still
be in use by other threads.

Each subclass should state the precise behavior of this method so
that users and developers know what to expect.

The precise meaning of "copy" may depend on the class of
the

CertStoreParameters

object. A typical implementation
performs a "deep copy" of this object, but this is not an absolute
requirement. Some implementations may perform a "shallow copy" of some
or all of the fields of this object.

Note that the

CertStore.getInstance

methods make a copy
of the specified

CertStoreParameters

. A deep copy
implementation of

clone

is safer and more robust, as it
prevents the caller from corrupting a shared

CertStore

by
subsequently modifying the contents of its initialization parameters.
However, a shallow copy implementation of

clone

is more
appropriate for applications that need to hold a reference to a
parameter contained in the

CertStoreParameters

. For example,
a shallow copy clone allows an application to release the resources of
a particular

CertStore

initialization parameter immediately,
rather than waiting for the garbage collection mechanism. This should
be done with the utmost care, since the

CertStore

may still
be in use by other threads.

Each subclass should state the precise behavior of this method so
that users and developers know what to expect.

Note that the

CertStore.getInstance

methods make a copy
of the specified

CertStoreParameters

. A deep copy
implementation of

clone

is safer and more robust, as it
prevents the caller from corrupting a shared

CertStore

by
subsequently modifying the contents of its initialization parameters.
However, a shallow copy implementation of

clone

is more
appropriate for applications that need to hold a reference to a
parameter contained in the

CertStoreParameters

. For example,
a shallow copy clone allows an application to release the resources of
a particular

CertStore

initialization parameter immediately,
rather than waiting for the garbage collection mechanism. This should
be done with the utmost care, since the

CertStore

may still
be in use by other threads.

Each subclass should state the precise behavior of this method so
that users and developers know what to expect.

Each subclass should state the precise behavior of this method so
that users and developers know what to expect.

---

