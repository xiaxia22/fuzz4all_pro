# Class JarSigner

**Source:** `jdk.jartool\jdk\security\jarsigner\JarSigner.html`

### Class Description

```java
public final class
JarSigner

extends
Object
```

An immutable utility class to sign a jar file.

A caller creates a

JarSigner.Builder

object, (optionally) sets
some parameters, and calls

build

to create
a

JarSigner

object. This

JarSigner

object can then
be used to sign a jar file.

Unless otherwise stated, calling a method of

JarSigner

or

JarSigner.Builder

with a null argument will throw
a

NullPointerException

.

Example:

```java
JarSigner signer = new JarSigner.Builder(key, certPath)
.digestAlgorithm("SHA-1")
.signatureAlgorithm("SHA1withDSA")
.build();
try (ZipFile in = new ZipFile(inputFile);
FileOutputStream out = new FileOutputStream(outputFile)) {
signer.sign(in, out);
}
```

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public void sign​(
ZipFile
file,

OutputStream
os)

Signs a file into an

OutputStream

. This method will not close

file

or

os

.

If an I/O error or signing error occurs during the signing, then it may
do so after some bytes have been written. Consequently, the output
stream may be in an inconsistent state. It is strongly recommended that
it be promptly closed in this case.

**Parameters:**
- file

- the file to sign.
- os

- the output stream.

**Throws:**
- JarSignerException

- if the signing fails.

---

#### public
String
getDigestAlgorithm()

Returns the digest algorithm for this

JarSigner

.

The return value is never null.

**Returns:**
- the digest algorithm.

---

#### public
String
getSignatureAlgorithm()

Returns the signature algorithm for this

JarSigner

.

The return value is never null.

**Returns:**
- the signature algorithm.

---

#### public
URI
getTsa()

Returns the URI of the Time Stamping Authority (TSA).

**Returns:**
- the URI of the TSA.

---

#### public
String
getSignerName()

Returns the signer name of this

JarSigner

.

The return value is never null.

**Returns:**
- the signer name.

---

#### public
String
getProperty​(
String
key)

Returns the value of an additional implementation-specific property
indicated by the specified key. If a property is not set but has a
default value, the default value will be returned.

**Parameters:**
- key

- the name of the property.

**Returns:**
- the value for the property.

**Throws:**
- UnsupportedOperationException

- if the key is not supported
by this implementation.

**Implementation Note:**
- See

JarSigner.Builder.setProperty(java.lang.String, java.lang.String)

for a list of
properties this implementation supports. All property names are
case-insensitive.

---

### Additional Sections

#### Class JarSigner

java.lang.Object

- jdk.security.jarsigner.JarSigner

jdk.security.jarsigner.JarSigner

```java
public final class
JarSigner

extends
Object
```

An immutable utility class to sign a jar file.

A caller creates a

JarSigner.Builder

object, (optionally) sets
some parameters, and calls

build

to create
a

JarSigner

object. This

JarSigner

object can then
be used to sign a jar file.

Unless otherwise stated, calling a method of

JarSigner

or

JarSigner.Builder

with a null argument will throw
a

NullPointerException

.

Example:

```java
JarSigner signer = new JarSigner.Builder(key, certPath)
.digestAlgorithm("SHA-1")
.signatureAlgorithm("SHA1withDSA")
.build();
try (ZipFile in = new ZipFile(inputFile);
FileOutputStream out = new FileOutputStream(outputFile)) {
signer.sign(in, out);
}
```

**Since:** 9

public final class

JarSigner

extends

Object

An immutable utility class to sign a jar file.

A caller creates a

JarSigner.Builder

object, (optionally) sets
some parameters, and calls

build

to create
a

JarSigner

object. This

JarSigner

object can then
be used to sign a jar file.

Unless otherwise stated, calling a method of

JarSigner

or

JarSigner.Builder

with a null argument will throw
a

NullPointerException

.

Example:

```java
JarSigner signer = new JarSigner.Builder(key, certPath)
.digestAlgorithm("SHA-1")
.signatureAlgorithm("SHA1withDSA")
.build();
try (ZipFile in = new ZipFile(inputFile);
FileOutputStream out = new FileOutputStream(outputFile)) {
signer.sign(in, out);
}
```

A caller creates a

JarSigner.Builder

object, (optionally) sets
some parameters, and calls

build

to create
a

JarSigner

object. This

JarSigner

object can then
be used to sign a jar file.

Unless otherwise stated, calling a method of

JarSigner

or

JarSigner.Builder

with a null argument will throw
a

NullPointerException

.

Example:

```java
JarSigner signer = new JarSigner.Builder(key, certPath)
.digestAlgorithm("SHA-1")
.signatureAlgorithm("SHA1withDSA")
.build();
try (ZipFile in = new ZipFile(inputFile);
FileOutputStream out = new FileOutputStream(outputFile)) {
signer.sign(in, out);
}
```

Unless otherwise stated, calling a method of

JarSigner

or

JarSigner.Builder

with a null argument will throw
a

NullPointerException

.

Example:

```java
JarSigner signer = new JarSigner.Builder(key, certPath)
.digestAlgorithm("SHA-1")
.signatureAlgorithm("SHA1withDSA")
.build();
try (ZipFile in = new ZipFile(inputFile);
FileOutputStream out = new FileOutputStream(outputFile)) {
signer.sign(in, out);
}
```

Example:

```java
JarSigner signer = new JarSigner.Builder(key, certPath)
.digestAlgorithm("SHA-1")
.signatureAlgorithm("SHA1withDSA")
.build();
try (ZipFile in = new ZipFile(inputFile);
FileOutputStream out = new FileOutputStream(outputFile)) {
signer.sign(in, out);
}
```

JarSigner signer = new JarSigner.Builder(key, certPath)
.digestAlgorithm("SHA-1")
.signatureAlgorithm("SHA1withDSA")
.build();
try (ZipFile in = new ZipFile(inputFile);
FileOutputStream out = new FileOutputStream(outputFile)) {
signer.sign(in, out);
}

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

JarSigner.Builder

A mutable builder class that can create an immutable

JarSigner

from various signing-related parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDigestAlgorithm

()

Returns the digest algorithm for this

JarSigner

.

String

getProperty

​(

String

key)

Returns the value of an additional implementation-specific property
indicated by the specified key.

String

getSignatureAlgorithm

()

Returns the signature algorithm for this

JarSigner

.

String

getSignerName

()

Returns the signer name of this

JarSigner

.

URI

getTsa

()

Returns the URI of the Time Stamping Authority (TSA).

void

sign

​(

ZipFile

file,

OutputStream

os)

Signs a file into an

OutputStream

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

toString

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

static class

JarSigner.Builder

A mutable builder class that can create an immutable

JarSigner

from various signing-related parameters.

---

#### Nested Class Summary

A mutable builder class that can create an immutable

JarSigner

from various signing-related parameters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDigestAlgorithm

()

Returns the digest algorithm for this

JarSigner

.

String

getProperty

​(

String

key)

Returns the value of an additional implementation-specific property
indicated by the specified key.

String

getSignatureAlgorithm

()

Returns the signature algorithm for this

JarSigner

.

String

getSignerName

()

Returns the signer name of this

JarSigner

.

URI

getTsa

()

Returns the URI of the Time Stamping Authority (TSA).

void

sign

​(

ZipFile

file,

OutputStream

os)

Signs a file into an

OutputStream

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the digest algorithm for this

JarSigner

.

Returns the value of an additional implementation-specific property
indicated by the specified key.

Returns the signature algorithm for this

JarSigner

.

Returns the signer name of this

JarSigner

.

Returns the URI of the Time Stamping Authority (TSA).

Signs a file into an

OutputStream

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

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ METHOD DETAIL ==========

- Method Detail

- sign

```java
public void sign​(
ZipFile
file,

OutputStream
os)
```

Signs a file into an

OutputStream

. This method will not close

file

or

os

.

If an I/O error or signing error occurs during the signing, then it may
do so after some bytes have been written. Consequently, the output
stream may be in an inconsistent state. It is strongly recommended that
it be promptly closed in this case.

**Parameters:** file

- the file to sign.
**Parameters:** os

- the output stream.
**Throws:** JarSignerException

- if the signing fails.

- getDigestAlgorithm

```java
public
String
getDigestAlgorithm()
```

Returns the digest algorithm for this

JarSigner

.

The return value is never null.

**Returns:** the digest algorithm.

- getSignatureAlgorithm

```java
public
String
getSignatureAlgorithm()
```

Returns the signature algorithm for this

JarSigner

.

The return value is never null.

**Returns:** the signature algorithm.

- getTsa

```java
public
URI
getTsa()
```

Returns the URI of the Time Stamping Authority (TSA).

**Returns:** the URI of the TSA.

- getSignerName

```java
public
String
getSignerName()
```

Returns the signer name of this

JarSigner

.

The return value is never null.

**Returns:** the signer name.

- getProperty

```java
public
String
getProperty​(
String
key)
```

Returns the value of an additional implementation-specific property
indicated by the specified key. If a property is not set but has a
default value, the default value will be returned.

**Implementation Note:** See

JarSigner.Builder.setProperty(java.lang.String, java.lang.String)

for a list of
properties this implementation supports. All property names are
case-insensitive.
**Parameters:** key

- the name of the property.
**Returns:** the value for the property.
**Throws:** UnsupportedOperationException

- if the key is not supported
by this implementation.

Method Detail

- sign

```java
public void sign​(
ZipFile
file,

OutputStream
os)
```

Signs a file into an

OutputStream

. This method will not close

file

or

os

.

If an I/O error or signing error occurs during the signing, then it may
do so after some bytes have been written. Consequently, the output
stream may be in an inconsistent state. It is strongly recommended that
it be promptly closed in this case.

**Parameters:** file

- the file to sign.
**Parameters:** os

- the output stream.
**Throws:** JarSignerException

- if the signing fails.

- getDigestAlgorithm

```java
public
String
getDigestAlgorithm()
```

Returns the digest algorithm for this

JarSigner

.

The return value is never null.

**Returns:** the digest algorithm.

- getSignatureAlgorithm

```java
public
String
getSignatureAlgorithm()
```

Returns the signature algorithm for this

JarSigner

.

The return value is never null.

**Returns:** the signature algorithm.

- getTsa

```java
public
URI
getTsa()
```

Returns the URI of the Time Stamping Authority (TSA).

**Returns:** the URI of the TSA.

- getSignerName

```java
public
String
getSignerName()
```

Returns the signer name of this

JarSigner

.

The return value is never null.

**Returns:** the signer name.

- getProperty

```java
public
String
getProperty​(
String
key)
```

Returns the value of an additional implementation-specific property
indicated by the specified key. If a property is not set but has a
default value, the default value will be returned.

**Implementation Note:** See

JarSigner.Builder.setProperty(java.lang.String, java.lang.String)

for a list of
properties this implementation supports. All property names are
case-insensitive.
**Parameters:** key

- the name of the property.
**Returns:** the value for the property.
**Throws:** UnsupportedOperationException

- if the key is not supported
by this implementation.

---

#### Method Detail

sign

```java
public void sign​(
ZipFile
file,

OutputStream
os)
```

Signs a file into an

OutputStream

. This method will not close

file

or

os

.

If an I/O error or signing error occurs during the signing, then it may
do so after some bytes have been written. Consequently, the output
stream may be in an inconsistent state. It is strongly recommended that
it be promptly closed in this case.

**Parameters:** file

- the file to sign.
**Parameters:** os

- the output stream.
**Throws:** JarSignerException

- if the signing fails.

---

#### sign

public void sign​(

ZipFile

file,

OutputStream

os)

Signs a file into an

OutputStream

. This method will not close

file

or

os

.

If an I/O error or signing error occurs during the signing, then it may
do so after some bytes have been written. Consequently, the output
stream may be in an inconsistent state. It is strongly recommended that
it be promptly closed in this case.

If an I/O error or signing error occurs during the signing, then it may
do so after some bytes have been written. Consequently, the output
stream may be in an inconsistent state. It is strongly recommended that
it be promptly closed in this case.

getDigestAlgorithm

```java
public
String
getDigestAlgorithm()
```

Returns the digest algorithm for this

JarSigner

.

The return value is never null.

**Returns:** the digest algorithm.

---

#### getDigestAlgorithm

public

String

getDigestAlgorithm()

Returns the digest algorithm for this

JarSigner

.

The return value is never null.

The return value is never null.

getSignatureAlgorithm

```java
public
String
getSignatureAlgorithm()
```

Returns the signature algorithm for this

JarSigner

.

The return value is never null.

**Returns:** the signature algorithm.

---

#### getSignatureAlgorithm

public

String

getSignatureAlgorithm()

Returns the signature algorithm for this

JarSigner

.

The return value is never null.

The return value is never null.

getTsa

```java
public
URI
getTsa()
```

Returns the URI of the Time Stamping Authority (TSA).

**Returns:** the URI of the TSA.

---

#### getTsa

public

URI

getTsa()

Returns the URI of the Time Stamping Authority (TSA).

getSignerName

```java
public
String
getSignerName()
```

Returns the signer name of this

JarSigner

.

The return value is never null.

**Returns:** the signer name.

---

#### getSignerName

public

String

getSignerName()

Returns the signer name of this

JarSigner

.

The return value is never null.

The return value is never null.

getProperty

```java
public
String
getProperty​(
String
key)
```

Returns the value of an additional implementation-specific property
indicated by the specified key. If a property is not set but has a
default value, the default value will be returned.

**Implementation Note:** See

JarSigner.Builder.setProperty(java.lang.String, java.lang.String)

for a list of
properties this implementation supports. All property names are
case-insensitive.
**Parameters:** key

- the name of the property.
**Returns:** the value for the property.
**Throws:** UnsupportedOperationException

- if the key is not supported
by this implementation.

---

#### getProperty

public

String

getProperty​(

String

key)

Returns the value of an additional implementation-specific property
indicated by the specified key. If a property is not set but has a
default value, the default value will be returned.

---

