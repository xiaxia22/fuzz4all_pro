# Class CertPath

**Source:** `java.base\java\security\cert\CertPath.html`

### Class Description

```java
public abstract class
CertPath

extends
Object

implements
Serializable
```

An immutable sequence of certificates (a certification path).

This is an abstract class that defines the methods common to all

CertPath

s. Subclasses can handle different kinds of
certificates (X.509, PGP, etc.).

All

CertPath

objects have a type, a list of

Certificate

s, and one or more supported encodings. Because the

CertPath

class is immutable, a

CertPath

cannot
change in any externally visible way after being constructed. This
stipulation applies to all public fields and methods of this class and any
added or overridden by subclasses.

The type is a

String

that identifies the type of

Certificate

s in the certification path. For each
certificate

cert

in a certification path

certPath

,

cert.getType().equals(certPath.getType())

must be

true

.

The list of

Certificate

s is an ordered

List

of
zero or more

Certificate

s. This

List

and all
of the

Certificate

s contained in it must be immutable.

Each

CertPath

object must support one or more encodings
so that the object can be translated into a byte array for storage or
transmission to other parties. Preferably, these encodings should be
well-documented standards (such as PKCS#7). One of the encodings supported
by a

CertPath

is considered the default encoding. This
encoding is used if no encoding is explicitly requested (for the

getEncoded()

method, for instance).

All

CertPath

objects are also

Serializable

.

CertPath

objects are resolved into an alternate

CertPathRep

object during serialization. This allows
a

CertPath

object to be serialized into an equivalent
representation regardless of its underlying implementation.

CertPath

objects can be created with a

CertificateFactory

or they can be returned by other classes,
such as a

CertPathBuilder

.

By convention, X.509

CertPath

s (consisting of

X509Certificate

s), are ordered starting with the target
certificate and ending with a certificate issued by the trust anchor. That
is, the issuer of one certificate is the subject of the following one. The
certificate representing the

TrustAnchor

should not be
included in the certification path. Unvalidated X.509

CertPath

s
may not follow these conventions. PKIX

CertPathValidator

s will
detect any departure from these conventions that cause the certification
path to be invalid and throw a

CertPathValidatorException

.

Every implementation of the Java platform is required to support the
following standard

CertPath

encodings:

- PKCS7
- PkiPath

These encodings are described in the

CertPath Encodings section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other encodings are supported.

Concurrent Access

All

CertPath

objects must be thread-safe. That is, multiple
threads may concurrently invoke the methods defined in this class on a
single

CertPath

object (or more than one) with no
ill effects. This is also true for the

List

returned by

CertPath.getCertificates

.

Requiring

CertPath

objects to be immutable and thread-safe
allows them to be passed around to various pieces of code without worrying
about coordinating access. Providing this thread-safety is
generally not difficult, since the

CertPath

and

List

objects in question are immutable.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected CertPath​(
String
type)

Creates a

CertPath

of the specified type.

This constructor is protected because most users should use a

CertificateFactory

to create

CertPath

s.

**Parameters:**
- type

- the standard name of the type of

Certificate

s in this path

---

### Method Details

#### public
String
getType()

Returns the type of

Certificate

s in this certification
path. This is the same string that would be returned by

cert.getType()

for all

Certificate

s in the certification path.

**Returns:**
- the type of

Certificate

s in this certification
path (never null)

---

#### public abstract
Iterator
<
String
> getEncodings()

Returns an iteration of the encodings supported by this certification
path, with the default encoding first. Attempts to modify the returned

Iterator

via its

remove

method result in an

UnsupportedOperationException

.

**Returns:**
- an

Iterator

over the names of the supported
encodings (as Strings)

---

#### public boolean equals​(
Object
other)

Compares this certification path for equality with the specified
object. Two

CertPath

s are equal if and only if their
types are equal and their certificate

List

s (and by
implication the

Certificate

s in those

List

s)
are equal. A

CertPath

is never equal to an object that is
not a

CertPath

.

This algorithm is implemented by this method. If it is overridden,
the behavior specified here must be maintained.

**Overrides:**
- equals

in class

Object

**Parameters:**
- other

- the object to test for equality with this certification path

**Returns:**
- true if the specified object is equal to this certification path,
false otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hashcode for this certification path. The hash code of
a certification path is defined to be the result of the following
calculation:

```java
hashCode = path.getType().hashCode();
hashCode = 31*hashCode + path.getCertificates().hashCode();
```

This ensures that

path1.equals(path2)

implies that

path1.hashCode()==path2.hashCode()

for any two certification
paths,

path1

and

path2

, as required by the
general contract of

Object.hashCode

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hashcode value for this certification path

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string representation of this certification path.
This calls the

toString

method on each of the

Certificate

s in the path.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this certification path

---

#### public abstract byte[] getEncoded()
throws
CertificateEncodingException

Returns the encoded form of this certification path, using the default
encoding.

**Returns:**
- the encoded bytes

**Throws:**
- CertificateEncodingException

- if an encoding error occurs

---

#### public abstract byte[] getEncoded​(
String
encoding)
throws
CertificateEncodingException

Returns the encoded form of this certification path, using the
specified encoding.

**Parameters:**
- encoding

- the name of the encoding to use

**Returns:**
- the encoded bytes

**Throws:**
- CertificateEncodingException

- if an encoding error occurs or
the encoding requested is not supported

---

#### public abstract
List
<? extends
Certificate
> getCertificates()

Returns the list of certificates in this certification path.
The

List

returned must be immutable and thread-safe.

**Returns:**
- an immutable

List

of

Certificate

s
(may be empty, but not null)

---

#### protected
Object
writeReplace()
throws
ObjectStreamException

Replaces the

CertPath

to be serialized with a

CertPathRep

object.

**Returns:**
- the

CertPathRep

to be serialized

**Throws:**
- ObjectStreamException

- if a

CertPathRep

object
representing this certification path could not be created

---

### Additional Sections

#### Class CertPath

java.lang.Object

- java.security.cert.CertPath

java.security.cert.CertPath

**All Implemented Interfaces:** Serializable

```java
public abstract class
CertPath

extends
Object

implements
Serializable
```

An immutable sequence of certificates (a certification path).

This is an abstract class that defines the methods common to all

CertPath

s. Subclasses can handle different kinds of
certificates (X.509, PGP, etc.).

All

CertPath

objects have a type, a list of

Certificate

s, and one or more supported encodings. Because the

CertPath

class is immutable, a

CertPath

cannot
change in any externally visible way after being constructed. This
stipulation applies to all public fields and methods of this class and any
added or overridden by subclasses.

The type is a

String

that identifies the type of

Certificate

s in the certification path. For each
certificate

cert

in a certification path

certPath

,

cert.getType().equals(certPath.getType())

must be

true

.

The list of

Certificate

s is an ordered

List

of
zero or more

Certificate

s. This

List

and all
of the

Certificate

s contained in it must be immutable.

Each

CertPath

object must support one or more encodings
so that the object can be translated into a byte array for storage or
transmission to other parties. Preferably, these encodings should be
well-documented standards (such as PKCS#7). One of the encodings supported
by a

CertPath

is considered the default encoding. This
encoding is used if no encoding is explicitly requested (for the

getEncoded()

method, for instance).

All

CertPath

objects are also

Serializable

.

CertPath

objects are resolved into an alternate

CertPathRep

object during serialization. This allows
a

CertPath

object to be serialized into an equivalent
representation regardless of its underlying implementation.

CertPath

objects can be created with a

CertificateFactory

or they can be returned by other classes,
such as a

CertPathBuilder

.

By convention, X.509

CertPath

s (consisting of

X509Certificate

s), are ordered starting with the target
certificate and ending with a certificate issued by the trust anchor. That
is, the issuer of one certificate is the subject of the following one. The
certificate representing the

TrustAnchor

should not be
included in the certification path. Unvalidated X.509

CertPath

s
may not follow these conventions. PKIX

CertPathValidator

s will
detect any departure from these conventions that cause the certification
path to be invalid and throw a

CertPathValidatorException

.

Every implementation of the Java platform is required to support the
following standard

CertPath

encodings:

- PKCS7
- PkiPath

These encodings are described in the

CertPath Encodings section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other encodings are supported.

Concurrent Access

All

CertPath

objects must be thread-safe. That is, multiple
threads may concurrently invoke the methods defined in this class on a
single

CertPath

object (or more than one) with no
ill effects. This is also true for the

List

returned by

CertPath.getCertificates

.

Requiring

CertPath

objects to be immutable and thread-safe
allows them to be passed around to various pieces of code without worrying
about coordinating access. Providing this thread-safety is
generally not difficult, since the

CertPath

and

List

objects in question are immutable.

**Since:** 1.4
**See Also:** CertificateFactory

,

CertPathBuilder

,

Serialized Form

public abstract class

CertPath

extends

Object

implements

Serializable

An immutable sequence of certificates (a certification path).

This is an abstract class that defines the methods common to all

CertPath

s. Subclasses can handle different kinds of
certificates (X.509, PGP, etc.).

All

CertPath

objects have a type, a list of

Certificate

s, and one or more supported encodings. Because the

CertPath

class is immutable, a

CertPath

cannot
change in any externally visible way after being constructed. This
stipulation applies to all public fields and methods of this class and any
added or overridden by subclasses.

The type is a

String

that identifies the type of

Certificate

s in the certification path. For each
certificate

cert

in a certification path

certPath

,

cert.getType().equals(certPath.getType())

must be

true

.

The list of

Certificate

s is an ordered

List

of
zero or more

Certificate

s. This

List

and all
of the

Certificate

s contained in it must be immutable.

Each

CertPath

object must support one or more encodings
so that the object can be translated into a byte array for storage or
transmission to other parties. Preferably, these encodings should be
well-documented standards (such as PKCS#7). One of the encodings supported
by a

CertPath

is considered the default encoding. This
encoding is used if no encoding is explicitly requested (for the

getEncoded()

method, for instance).

All

CertPath

objects are also

Serializable

.

CertPath

objects are resolved into an alternate

CertPathRep

object during serialization. This allows
a

CertPath

object to be serialized into an equivalent
representation regardless of its underlying implementation.

CertPath

objects can be created with a

CertificateFactory

or they can be returned by other classes,
such as a

CertPathBuilder

.

By convention, X.509

CertPath

s (consisting of

X509Certificate

s), are ordered starting with the target
certificate and ending with a certificate issued by the trust anchor. That
is, the issuer of one certificate is the subject of the following one. The
certificate representing the

TrustAnchor

should not be
included in the certification path. Unvalidated X.509

CertPath

s
may not follow these conventions. PKIX

CertPathValidator

s will
detect any departure from these conventions that cause the certification
path to be invalid and throw a

CertPathValidatorException

.

Every implementation of the Java platform is required to support the
following standard

CertPath

encodings:

- PKCS7
- PkiPath

These encodings are described in the

CertPath Encodings section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other encodings are supported.

Concurrent Access

All

CertPath

objects must be thread-safe. That is, multiple
threads may concurrently invoke the methods defined in this class on a
single

CertPath

object (or more than one) with no
ill effects. This is also true for the

List

returned by

CertPath.getCertificates

.

Requiring

CertPath

objects to be immutable and thread-safe
allows them to be passed around to various pieces of code without worrying
about coordinating access. Providing this thread-safety is
generally not difficult, since the

CertPath

and

List

objects in question are immutable.

This is an abstract class that defines the methods common to all

CertPath

s. Subclasses can handle different kinds of
certificates (X.509, PGP, etc.).

All

CertPath

objects have a type, a list of

Certificate

s, and one or more supported encodings. Because the

CertPath

class is immutable, a

CertPath

cannot
change in any externally visible way after being constructed. This
stipulation applies to all public fields and methods of this class and any
added or overridden by subclasses.

The type is a

String

that identifies the type of

Certificate

s in the certification path. For each
certificate

cert

in a certification path

certPath

,

cert.getType().equals(certPath.getType())

must be

true

.

The list of

Certificate

s is an ordered

List

of
zero or more

Certificate

s. This

List

and all
of the

Certificate

s contained in it must be immutable.

Each

CertPath

object must support one or more encodings
so that the object can be translated into a byte array for storage or
transmission to other parties. Preferably, these encodings should be
well-documented standards (such as PKCS#7). One of the encodings supported
by a

CertPath

is considered the default encoding. This
encoding is used if no encoding is explicitly requested (for the

getEncoded()

method, for instance).

All

CertPath

objects are also

Serializable

.

CertPath

objects are resolved into an alternate

CertPathRep

object during serialization. This allows
a

CertPath

object to be serialized into an equivalent
representation regardless of its underlying implementation.

CertPath

objects can be created with a

CertificateFactory

or they can be returned by other classes,
such as a

CertPathBuilder

.

By convention, X.509

CertPath

s (consisting of

X509Certificate

s), are ordered starting with the target
certificate and ending with a certificate issued by the trust anchor. That
is, the issuer of one certificate is the subject of the following one. The
certificate representing the

TrustAnchor

should not be
included in the certification path. Unvalidated X.509

CertPath

s
may not follow these conventions. PKIX

CertPathValidator

s will
detect any departure from these conventions that cause the certification
path to be invalid and throw a

CertPathValidatorException

.

Every implementation of the Java platform is required to support the
following standard

CertPath

encodings:

- PKCS7
- PkiPath

These encodings are described in the

CertPath Encodings section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other encodings are supported.

Concurrent Access

All

CertPath

objects must be thread-safe. That is, multiple
threads may concurrently invoke the methods defined in this class on a
single

CertPath

object (or more than one) with no
ill effects. This is also true for the

List

returned by

CertPath.getCertificates

.

Requiring

CertPath

objects to be immutable and thread-safe
allows them to be passed around to various pieces of code without worrying
about coordinating access. Providing this thread-safety is
generally not difficult, since the

CertPath

and

List

objects in question are immutable.

All

CertPath

objects have a type, a list of

Certificate

s, and one or more supported encodings. Because the

CertPath

class is immutable, a

CertPath

cannot
change in any externally visible way after being constructed. This
stipulation applies to all public fields and methods of this class and any
added or overridden by subclasses.

The type is a

String

that identifies the type of

Certificate

s in the certification path. For each
certificate

cert

in a certification path

certPath

,

cert.getType().equals(certPath.getType())

must be

true

.

The list of

Certificate

s is an ordered

List

of
zero or more

Certificate

s. This

List

and all
of the

Certificate

s contained in it must be immutable.

Each

CertPath

object must support one or more encodings
so that the object can be translated into a byte array for storage or
transmission to other parties. Preferably, these encodings should be
well-documented standards (such as PKCS#7). One of the encodings supported
by a

CertPath

is considered the default encoding. This
encoding is used if no encoding is explicitly requested (for the

getEncoded()

method, for instance).

All

CertPath

objects are also

Serializable

.

CertPath

objects are resolved into an alternate

CertPathRep

object during serialization. This allows
a

CertPath

object to be serialized into an equivalent
representation regardless of its underlying implementation.

CertPath

objects can be created with a

CertificateFactory

or they can be returned by other classes,
such as a

CertPathBuilder

.

By convention, X.509

CertPath

s (consisting of

X509Certificate

s), are ordered starting with the target
certificate and ending with a certificate issued by the trust anchor. That
is, the issuer of one certificate is the subject of the following one. The
certificate representing the

TrustAnchor

should not be
included in the certification path. Unvalidated X.509

CertPath

s
may not follow these conventions. PKIX

CertPathValidator

s will
detect any departure from these conventions that cause the certification
path to be invalid and throw a

CertPathValidatorException

.

Every implementation of the Java platform is required to support the
following standard

CertPath

encodings:

- PKCS7
- PkiPath

These encodings are described in the

CertPath Encodings section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other encodings are supported.

Concurrent Access

All

CertPath

objects must be thread-safe. That is, multiple
threads may concurrently invoke the methods defined in this class on a
single

CertPath

object (or more than one) with no
ill effects. This is also true for the

List

returned by

CertPath.getCertificates

.

Requiring

CertPath

objects to be immutable and thread-safe
allows them to be passed around to various pieces of code without worrying
about coordinating access. Providing this thread-safety is
generally not difficult, since the

CertPath

and

List

objects in question are immutable.

The type is a

String

that identifies the type of

Certificate

s in the certification path. For each
certificate

cert

in a certification path

certPath

,

cert.getType().equals(certPath.getType())

must be

true

.

The list of

Certificate

s is an ordered

List

of
zero or more

Certificate

s. This

List

and all
of the

Certificate

s contained in it must be immutable.

Each

CertPath

object must support one or more encodings
so that the object can be translated into a byte array for storage or
transmission to other parties. Preferably, these encodings should be
well-documented standards (such as PKCS#7). One of the encodings supported
by a

CertPath

is considered the default encoding. This
encoding is used if no encoding is explicitly requested (for the

getEncoded()

method, for instance).

All

CertPath

objects are also

Serializable

.

CertPath

objects are resolved into an alternate

CertPathRep

object during serialization. This allows
a

CertPath

object to be serialized into an equivalent
representation regardless of its underlying implementation.

CertPath

objects can be created with a

CertificateFactory

or they can be returned by other classes,
such as a

CertPathBuilder

.

By convention, X.509

CertPath

s (consisting of

X509Certificate

s), are ordered starting with the target
certificate and ending with a certificate issued by the trust anchor. That
is, the issuer of one certificate is the subject of the following one. The
certificate representing the

TrustAnchor

should not be
included in the certification path. Unvalidated X.509

CertPath

s
may not follow these conventions. PKIX

CertPathValidator

s will
detect any departure from these conventions that cause the certification
path to be invalid and throw a

CertPathValidatorException

.

Every implementation of the Java platform is required to support the
following standard

CertPath

encodings:

- PKCS7
- PkiPath

These encodings are described in the

CertPath Encodings section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other encodings are supported.

Concurrent Access

All

CertPath

objects must be thread-safe. That is, multiple
threads may concurrently invoke the methods defined in this class on a
single

CertPath

object (or more than one) with no
ill effects. This is also true for the

List

returned by

CertPath.getCertificates

.

Requiring

CertPath

objects to be immutable and thread-safe
allows them to be passed around to various pieces of code without worrying
about coordinating access. Providing this thread-safety is
generally not difficult, since the

CertPath

and

List

objects in question are immutable.

The list of

Certificate

s is an ordered

List

of
zero or more

Certificate

s. This

List

and all
of the

Certificate

s contained in it must be immutable.

Each

CertPath

object must support one or more encodings
so that the object can be translated into a byte array for storage or
transmission to other parties. Preferably, these encodings should be
well-documented standards (such as PKCS#7). One of the encodings supported
by a

CertPath

is considered the default encoding. This
encoding is used if no encoding is explicitly requested (for the

getEncoded()

method, for instance).

All

CertPath

objects are also

Serializable

.

CertPath

objects are resolved into an alternate

CertPathRep

object during serialization. This allows
a

CertPath

object to be serialized into an equivalent
representation regardless of its underlying implementation.

CertPath

objects can be created with a

CertificateFactory

or they can be returned by other classes,
such as a

CertPathBuilder

.

By convention, X.509

CertPath

s (consisting of

X509Certificate

s), are ordered starting with the target
certificate and ending with a certificate issued by the trust anchor. That
is, the issuer of one certificate is the subject of the following one. The
certificate representing the

TrustAnchor

should not be
included in the certification path. Unvalidated X.509

CertPath

s
may not follow these conventions. PKIX

CertPathValidator

s will
detect any departure from these conventions that cause the certification
path to be invalid and throw a

CertPathValidatorException

.

Every implementation of the Java platform is required to support the
following standard

CertPath

encodings:

- PKCS7
- PkiPath

These encodings are described in the

CertPath Encodings section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other encodings are supported.

Concurrent Access

All

CertPath

objects must be thread-safe. That is, multiple
threads may concurrently invoke the methods defined in this class on a
single

CertPath

object (or more than one) with no
ill effects. This is also true for the

List

returned by

CertPath.getCertificates

.

Requiring

CertPath

objects to be immutable and thread-safe
allows them to be passed around to various pieces of code without worrying
about coordinating access. Providing this thread-safety is
generally not difficult, since the

CertPath

and

List

objects in question are immutable.

Each

CertPath

object must support one or more encodings
so that the object can be translated into a byte array for storage or
transmission to other parties. Preferably, these encodings should be
well-documented standards (such as PKCS#7). One of the encodings supported
by a

CertPath

is considered the default encoding. This
encoding is used if no encoding is explicitly requested (for the

getEncoded()

method, for instance).

All

CertPath

objects are also

Serializable

.

CertPath

objects are resolved into an alternate

CertPathRep

object during serialization. This allows
a

CertPath

object to be serialized into an equivalent
representation regardless of its underlying implementation.

CertPath

objects can be created with a

CertificateFactory

or they can be returned by other classes,
such as a

CertPathBuilder

.

By convention, X.509

CertPath

s (consisting of

X509Certificate

s), are ordered starting with the target
certificate and ending with a certificate issued by the trust anchor. That
is, the issuer of one certificate is the subject of the following one. The
certificate representing the

TrustAnchor

should not be
included in the certification path. Unvalidated X.509

CertPath

s
may not follow these conventions. PKIX

CertPathValidator

s will
detect any departure from these conventions that cause the certification
path to be invalid and throw a

CertPathValidatorException

.

Every implementation of the Java platform is required to support the
following standard

CertPath

encodings:

- PKCS7
- PkiPath

These encodings are described in the

CertPath Encodings section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other encodings are supported.

Concurrent Access

All

CertPath

objects must be thread-safe. That is, multiple
threads may concurrently invoke the methods defined in this class on a
single

CertPath

object (or more than one) with no
ill effects. This is also true for the

List

returned by

CertPath.getCertificates

.

Requiring

CertPath

objects to be immutable and thread-safe
allows them to be passed around to various pieces of code without worrying
about coordinating access. Providing this thread-safety is
generally not difficult, since the

CertPath

and

List

objects in question are immutable.

All

CertPath

objects are also

Serializable

.

CertPath

objects are resolved into an alternate

CertPathRep

object during serialization. This allows
a

CertPath

object to be serialized into an equivalent
representation regardless of its underlying implementation.

CertPath

objects can be created with a

CertificateFactory

or they can be returned by other classes,
such as a

CertPathBuilder

.

By convention, X.509

CertPath

s (consisting of

X509Certificate

s), are ordered starting with the target
certificate and ending with a certificate issued by the trust anchor. That
is, the issuer of one certificate is the subject of the following one. The
certificate representing the

TrustAnchor

should not be
included in the certification path. Unvalidated X.509

CertPath

s
may not follow these conventions. PKIX

CertPathValidator

s will
detect any departure from these conventions that cause the certification
path to be invalid and throw a

CertPathValidatorException

.

Every implementation of the Java platform is required to support the
following standard

CertPath

encodings:

- PKCS7
- PkiPath

These encodings are described in the

CertPath Encodings section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other encodings are supported.

Concurrent Access

All

CertPath

objects must be thread-safe. That is, multiple
threads may concurrently invoke the methods defined in this class on a
single

CertPath

object (or more than one) with no
ill effects. This is also true for the

List

returned by

CertPath.getCertificates

.

Requiring

CertPath

objects to be immutable and thread-safe
allows them to be passed around to various pieces of code without worrying
about coordinating access. Providing this thread-safety is
generally not difficult, since the

CertPath

and

List

objects in question are immutable.

CertPath

objects can be created with a

CertificateFactory

or they can be returned by other classes,
such as a

CertPathBuilder

.

By convention, X.509

CertPath

s (consisting of

X509Certificate

s), are ordered starting with the target
certificate and ending with a certificate issued by the trust anchor. That
is, the issuer of one certificate is the subject of the following one. The
certificate representing the

TrustAnchor

should not be
included in the certification path. Unvalidated X.509

CertPath

s
may not follow these conventions. PKIX

CertPathValidator

s will
detect any departure from these conventions that cause the certification
path to be invalid and throw a

CertPathValidatorException

.

Every implementation of the Java platform is required to support the
following standard

CertPath

encodings:

- PKCS7
- PkiPath

These encodings are described in the

CertPath Encodings section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other encodings are supported.

Concurrent Access

All

CertPath

objects must be thread-safe. That is, multiple
threads may concurrently invoke the methods defined in this class on a
single

CertPath

object (or more than one) with no
ill effects. This is also true for the

List

returned by

CertPath.getCertificates

.

Requiring

CertPath

objects to be immutable and thread-safe
allows them to be passed around to various pieces of code without worrying
about coordinating access. Providing this thread-safety is
generally not difficult, since the

CertPath

and

List

objects in question are immutable.

By convention, X.509

CertPath

s (consisting of

X509Certificate

s), are ordered starting with the target
certificate and ending with a certificate issued by the trust anchor. That
is, the issuer of one certificate is the subject of the following one. The
certificate representing the

TrustAnchor

should not be
included in the certification path. Unvalidated X.509

CertPath

s
may not follow these conventions. PKIX

CertPathValidator

s will
detect any departure from these conventions that cause the certification
path to be invalid and throw a

CertPathValidatorException

.

Every implementation of the Java platform is required to support the
following standard

CertPath

encodings:

- PKCS7
- PkiPath

These encodings are described in the

CertPath Encodings section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other encodings are supported.

Concurrent Access

All

CertPath

objects must be thread-safe. That is, multiple
threads may concurrently invoke the methods defined in this class on a
single

CertPath

object (or more than one) with no
ill effects. This is also true for the

List

returned by

CertPath.getCertificates

.

Requiring

CertPath

objects to be immutable and thread-safe
allows them to be passed around to various pieces of code without worrying
about coordinating access. Providing this thread-safety is
generally not difficult, since the

CertPath

and

List

objects in question are immutable.

Every implementation of the Java platform is required to support the
following standard

CertPath

encodings:

- PKCS7
- PkiPath

These encodings are described in the

CertPath Encodings section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other encodings are supported.

Concurrent Access

All

CertPath

objects must be thread-safe. That is, multiple
threads may concurrently invoke the methods defined in this class on a
single

CertPath

object (or more than one) with no
ill effects. This is also true for the

List

returned by

CertPath.getCertificates

.

Requiring

CertPath

objects to be immutable and thread-safe
allows them to be passed around to various pieces of code without worrying
about coordinating access. Providing this thread-safety is
generally not difficult, since the

CertPath

and

List

objects in question are immutable.

PKCS7

PkiPath

Concurrent Access

All

CertPath

objects must be thread-safe. That is, multiple
threads may concurrently invoke the methods defined in this class on a
single

CertPath

object (or more than one) with no
ill effects. This is also true for the

List

returned by

CertPath.getCertificates

.

Requiring

CertPath

objects to be immutable and thread-safe
allows them to be passed around to various pieces of code without worrying
about coordinating access. Providing this thread-safety is
generally not difficult, since the

CertPath

and

List

objects in question are immutable.

All

CertPath

objects must be thread-safe. That is, multiple
threads may concurrently invoke the methods defined in this class on a
single

CertPath

object (or more than one) with no
ill effects. This is also true for the

List

returned by

CertPath.getCertificates

.

Requiring

CertPath

objects to be immutable and thread-safe
allows them to be passed around to various pieces of code without worrying
about coordinating access. Providing this thread-safety is
generally not difficult, since the

CertPath

and

List

objects in question are immutable.

Requiring

CertPath

objects to be immutable and thread-safe
allows them to be passed around to various pieces of code without worrying
about coordinating access. Providing this thread-safety is
generally not difficult, since the

CertPath

and

List

objects in question are immutable.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected static class

CertPath.CertPathRep

Alternate

CertPath

class for serialization.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CertPath

​(

String

type)

Creates a

CertPath

of the specified type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

other)

Compares this certification path for equality with the specified
object.

abstract

List

<? extends

Certificate

>

getCertificates

()

Returns the list of certificates in this certification path.

abstract byte[]

getEncoded

()

Returns the encoded form of this certification path, using the default
encoding.

abstract byte[]

getEncoded

​(

String

encoding)

Returns the encoded form of this certification path, using the
specified encoding.

abstract

Iterator

<

String

>

getEncodings

()

Returns an iteration of the encodings supported by this certification
path, with the default encoding first.

String

getType

()

Returns the type of

Certificate

s in this certification
path.

int

hashCode

()

Returns the hashcode for this certification path.

String

toString

()

Returns a string representation of this certification path.

protected

Object

writeReplace

()

Replaces the

CertPath

to be serialized with a

CertPathRep

object.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected static class

CertPath.CertPathRep

Alternate

CertPath

class for serialization.

---

#### Nested Class Summary

Alternate

CertPath

class for serialization.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CertPath

​(

String

type)

Creates a

CertPath

of the specified type.

---

#### Constructor Summary

Creates a

CertPath

of the specified type.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

other)

Compares this certification path for equality with the specified
object.

abstract

List

<? extends

Certificate

>

getCertificates

()

Returns the list of certificates in this certification path.

abstract byte[]

getEncoded

()

Returns the encoded form of this certification path, using the default
encoding.

abstract byte[]

getEncoded

​(

String

encoding)

Returns the encoded form of this certification path, using the
specified encoding.

abstract

Iterator

<

String

>

getEncodings

()

Returns an iteration of the encodings supported by this certification
path, with the default encoding first.

String

getType

()

Returns the type of

Certificate

s in this certification
path.

int

hashCode

()

Returns the hashcode for this certification path.

String

toString

()

Returns a string representation of this certification path.

protected

Object

writeReplace

()

Replaces the

CertPath

to be serialized with a

CertPathRep

object.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

Compares this certification path for equality with the specified
object.

Returns the list of certificates in this certification path.

Returns the encoded form of this certification path, using the default
encoding.

Returns the encoded form of this certification path, using the
specified encoding.

Returns an iteration of the encodings supported by this certification
path, with the default encoding first.

Returns the type of

Certificate

s in this certification
path.

Returns the hashcode for this certification path.

Returns a string representation of this certification path.

Replaces the

CertPath

to be serialized with a

CertPathRep

object.

Methods declared in class java.lang.

Object

clone

,

finalize

,

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CertPath

```java
protected CertPath​(
String
type)
```

Creates a

CertPath

of the specified type.

This constructor is protected because most users should use a

CertificateFactory

to create

CertPath

s.

**Parameters:** type

- the standard name of the type of

Certificate

s in this path

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
public
String
getType()
```

Returns the type of

Certificate

s in this certification
path. This is the same string that would be returned by

cert.getType()

for all

Certificate

s in the certification path.

**Returns:** the type of

Certificate

s in this certification
path (never null)

- getEncodings

```java
public abstract
Iterator
<
String
> getEncodings()
```

Returns an iteration of the encodings supported by this certification
path, with the default encoding first. Attempts to modify the returned

Iterator

via its

remove

method result in an

UnsupportedOperationException

.

**Returns:** an

Iterator

over the names of the supported
encodings (as Strings)

- equals

```java
public boolean equals​(
Object
other)
```

Compares this certification path for equality with the specified
object. Two

CertPath

s are equal if and only if their
types are equal and their certificate

List

s (and by
implication the

Certificate

s in those

List

s)
are equal. A

CertPath

is never equal to an object that is
not a

CertPath

.

This algorithm is implemented by this method. If it is overridden,
the behavior specified here must be maintained.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to test for equality with this certification path
**Returns:** true if the specified object is equal to this certification path,
false otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hashcode for this certification path. The hash code of
a certification path is defined to be the result of the following
calculation:

```java
hashCode = path.getType().hashCode();
hashCode = 31*hashCode + path.getCertificates().hashCode();
```

This ensures that

path1.equals(path2)

implies that

path1.hashCode()==path2.hashCode()

for any two certification
paths,

path1

and

path2

, as required by the
general contract of

Object.hashCode

.

**Overrides:** hashCode

in class

Object
**Returns:** the hashcode value for this certification path
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this certification path.
This calls the

toString

method on each of the

Certificate

s in the path.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this certification path

- getEncoded

```java
public abstract byte[] getEncoded()
throws
CertificateEncodingException
```

Returns the encoded form of this certification path, using the default
encoding.

**Returns:** the encoded bytes
**Throws:** CertificateEncodingException

- if an encoding error occurs

- getEncoded

```java
public abstract byte[] getEncoded​(
String
encoding)
throws
CertificateEncodingException
```

Returns the encoded form of this certification path, using the
specified encoding.

**Parameters:** encoding

- the name of the encoding to use
**Returns:** the encoded bytes
**Throws:** CertificateEncodingException

- if an encoding error occurs or
the encoding requested is not supported

- getCertificates

```java
public abstract
List
<? extends
Certificate
> getCertificates()
```

Returns the list of certificates in this certification path.
The

List

returned must be immutable and thread-safe.

**Returns:** an immutable

List

of

Certificate

s
(may be empty, but not null)

- writeReplace

```java
protected
Object
writeReplace()
throws
ObjectStreamException
```

Replaces the

CertPath

to be serialized with a

CertPathRep

object.

**Returns:** the

CertPathRep

to be serialized
**Throws:** ObjectStreamException

- if a

CertPathRep

object
representing this certification path could not be created

Constructor Detail

- CertPath

```java
protected CertPath​(
String
type)
```

Creates a

CertPath

of the specified type.

This constructor is protected because most users should use a

CertificateFactory

to create

CertPath

s.

**Parameters:** type

- the standard name of the type of

Certificate

s in this path

---

#### Constructor Detail

CertPath

```java
protected CertPath​(
String
type)
```

Creates a

CertPath

of the specified type.

This constructor is protected because most users should use a

CertificateFactory

to create

CertPath

s.

**Parameters:** type

- the standard name of the type of

Certificate

s in this path

---

#### CertPath

protected CertPath​(

String

type)

Creates a

CertPath

of the specified type.

This constructor is protected because most users should use a

CertificateFactory

to create

CertPath

s.

This constructor is protected because most users should use a

CertificateFactory

to create

CertPath

s.

Method Detail

- getType

```java
public
String
getType()
```

Returns the type of

Certificate

s in this certification
path. This is the same string that would be returned by

cert.getType()

for all

Certificate

s in the certification path.

**Returns:** the type of

Certificate

s in this certification
path (never null)

- getEncodings

```java
public abstract
Iterator
<
String
> getEncodings()
```

Returns an iteration of the encodings supported by this certification
path, with the default encoding first. Attempts to modify the returned

Iterator

via its

remove

method result in an

UnsupportedOperationException

.

**Returns:** an

Iterator

over the names of the supported
encodings (as Strings)

- equals

```java
public boolean equals​(
Object
other)
```

Compares this certification path for equality with the specified
object. Two

CertPath

s are equal if and only if their
types are equal and their certificate

List

s (and by
implication the

Certificate

s in those

List

s)
are equal. A

CertPath

is never equal to an object that is
not a

CertPath

.

This algorithm is implemented by this method. If it is overridden,
the behavior specified here must be maintained.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to test for equality with this certification path
**Returns:** true if the specified object is equal to this certification path,
false otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hashcode for this certification path. The hash code of
a certification path is defined to be the result of the following
calculation:

```java
hashCode = path.getType().hashCode();
hashCode = 31*hashCode + path.getCertificates().hashCode();
```

This ensures that

path1.equals(path2)

implies that

path1.hashCode()==path2.hashCode()

for any two certification
paths,

path1

and

path2

, as required by the
general contract of

Object.hashCode

.

**Overrides:** hashCode

in class

Object
**Returns:** the hashcode value for this certification path
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this certification path.
This calls the

toString

method on each of the

Certificate

s in the path.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this certification path

- getEncoded

```java
public abstract byte[] getEncoded()
throws
CertificateEncodingException
```

Returns the encoded form of this certification path, using the default
encoding.

**Returns:** the encoded bytes
**Throws:** CertificateEncodingException

- if an encoding error occurs

- getEncoded

```java
public abstract byte[] getEncoded​(
String
encoding)
throws
CertificateEncodingException
```

Returns the encoded form of this certification path, using the
specified encoding.

**Parameters:** encoding

- the name of the encoding to use
**Returns:** the encoded bytes
**Throws:** CertificateEncodingException

- if an encoding error occurs or
the encoding requested is not supported

- getCertificates

```java
public abstract
List
<? extends
Certificate
> getCertificates()
```

Returns the list of certificates in this certification path.
The

List

returned must be immutable and thread-safe.

**Returns:** an immutable

List

of

Certificate

s
(may be empty, but not null)

- writeReplace

```java
protected
Object
writeReplace()
throws
ObjectStreamException
```

Replaces the

CertPath

to be serialized with a

CertPathRep

object.

**Returns:** the

CertPathRep

to be serialized
**Throws:** ObjectStreamException

- if a

CertPathRep

object
representing this certification path could not be created

---

#### Method Detail

getType

```java
public
String
getType()
```

Returns the type of

Certificate

s in this certification
path. This is the same string that would be returned by

cert.getType()

for all

Certificate

s in the certification path.

**Returns:** the type of

Certificate

s in this certification
path (never null)

---

#### getType

public

String

getType()

Returns the type of

Certificate

s in this certification
path. This is the same string that would be returned by

cert.getType()

for all

Certificate

s in the certification path.

getEncodings

```java
public abstract
Iterator
<
String
> getEncodings()
```

Returns an iteration of the encodings supported by this certification
path, with the default encoding first. Attempts to modify the returned

Iterator

via its

remove

method result in an

UnsupportedOperationException

.

**Returns:** an

Iterator

over the names of the supported
encodings (as Strings)

---

#### getEncodings

public abstract

Iterator

<

String

> getEncodings()

Returns an iteration of the encodings supported by this certification
path, with the default encoding first. Attempts to modify the returned

Iterator

via its

remove

method result in an

UnsupportedOperationException

.

equals

```java
public boolean equals​(
Object
other)
```

Compares this certification path for equality with the specified
object. Two

CertPath

s are equal if and only if their
types are equal and their certificate

List

s (and by
implication the

Certificate

s in those

List

s)
are equal. A

CertPath

is never equal to an object that is
not a

CertPath

.

This algorithm is implemented by this method. If it is overridden,
the behavior specified here must be maintained.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to test for equality with this certification path
**Returns:** true if the specified object is equal to this certification path,
false otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

other)

Compares this certification path for equality with the specified
object. Two

CertPath

s are equal if and only if their
types are equal and their certificate

List

s (and by
implication the

Certificate

s in those

List

s)
are equal. A

CertPath

is never equal to an object that is
not a

CertPath

.

This algorithm is implemented by this method. If it is overridden,
the behavior specified here must be maintained.

This algorithm is implemented by this method. If it is overridden,
the behavior specified here must be maintained.

hashCode

```java
public int hashCode()
```

Returns the hashcode for this certification path. The hash code of
a certification path is defined to be the result of the following
calculation:

```java
hashCode = path.getType().hashCode();
hashCode = 31*hashCode + path.getCertificates().hashCode();
```

This ensures that

path1.equals(path2)

implies that

path1.hashCode()==path2.hashCode()

for any two certification
paths,

path1

and

path2

, as required by the
general contract of

Object.hashCode

.

**Overrides:** hashCode

in class

Object
**Returns:** the hashcode value for this certification path
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hashcode for this certification path. The hash code of
a certification path is defined to be the result of the following
calculation:

```java
hashCode = path.getType().hashCode();
hashCode = 31*hashCode + path.getCertificates().hashCode();
```

This ensures that

path1.equals(path2)

implies that

path1.hashCode()==path2.hashCode()

for any two certification
paths,

path1

and

path2

, as required by the
general contract of

Object.hashCode

.

hashCode = path.getType().hashCode();
hashCode = 31*hashCode + path.getCertificates().hashCode();

toString

```java
public
String
toString()
```

Returns a string representation of this certification path.
This calls the

toString

method on each of the

Certificate

s in the path.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this certification path

---

#### toString

public

String

toString()

Returns a string representation of this certification path.
This calls the

toString

method on each of the

Certificate

s in the path.

getEncoded

```java
public abstract byte[] getEncoded()
throws
CertificateEncodingException
```

Returns the encoded form of this certification path, using the default
encoding.

**Returns:** the encoded bytes
**Throws:** CertificateEncodingException

- if an encoding error occurs

---

#### getEncoded

public abstract byte[] getEncoded()
throws

CertificateEncodingException

Returns the encoded form of this certification path, using the default
encoding.

getEncoded

```java
public abstract byte[] getEncoded​(
String
encoding)
throws
CertificateEncodingException
```

Returns the encoded form of this certification path, using the
specified encoding.

**Parameters:** encoding

- the name of the encoding to use
**Returns:** the encoded bytes
**Throws:** CertificateEncodingException

- if an encoding error occurs or
the encoding requested is not supported

---

#### getEncoded

public abstract byte[] getEncoded​(

String

encoding)
throws

CertificateEncodingException

Returns the encoded form of this certification path, using the
specified encoding.

getCertificates

```java
public abstract
List
<? extends
Certificate
> getCertificates()
```

Returns the list of certificates in this certification path.
The

List

returned must be immutable and thread-safe.

**Returns:** an immutable

List

of

Certificate

s
(may be empty, but not null)

---

#### getCertificates

public abstract

List

<? extends

Certificate

> getCertificates()

Returns the list of certificates in this certification path.
The

List

returned must be immutable and thread-safe.

writeReplace

```java
protected
Object
writeReplace()
throws
ObjectStreamException
```

Replaces the

CertPath

to be serialized with a

CertPathRep

object.

**Returns:** the

CertPathRep

to be serialized
**Throws:** ObjectStreamException

- if a

CertPathRep

object
representing this certification path could not be created

---

#### writeReplace

protected

Object

writeReplace()
throws

ObjectStreamException

Replaces the

CertPath

to be serialized with a

CertPathRep

object.

---

