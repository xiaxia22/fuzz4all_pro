# Class SecureClassLoader

**Source:** `java.base\java\security\SecureClassLoader.html`

### Class Description

```java
public class
SecureClassLoader

extends
ClassLoader
```

This class extends ClassLoader with additional support for defining
classes with an associated code source and permissions which are
retrieved by the system policy by default.

**Direct Known Subclasses:** URLClassLoader

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SecureClassLoader​(
ClassLoader
parent)

Creates a new SecureClassLoader using the specified parent
class loader for delegation.

If there is a security manager, this method first
calls the security manager's

checkCreateClassLoader

method to ensure creation of a class loader is allowed.

**Parameters:**
- parent

- the parent ClassLoader

**Throws:**
- SecurityException

- if a security manager exists and its

checkCreateClassLoader

method doesn't allow
creation of a class loader.

**See Also:**
- SecurityManager.checkCreateClassLoader()

---

#### protected SecureClassLoader()

Creates a new SecureClassLoader using the default parent class
loader for delegation.

If there is a security manager, this method first
calls the security manager's

checkCreateClassLoader

method to ensure creation of a class loader is allowed.

**Throws:**
- SecurityException

- if a security manager exists and its

checkCreateClassLoader

method doesn't allow
creation of a class loader.

**See Also:**
- SecurityManager.checkCreateClassLoader()

---

#### protected SecureClassLoader​(
String
name,

ClassLoader
parent)

Creates a new

SecureClassLoader

of the specified name and
using the specified parent class loader for delegation.

**Parameters:**
- name

- class loader name; or

null

if not named
- parent

- the parent class loader

**Throws:**
- IllegalArgumentException

- if the given name is empty.
- SecurityException

- if a security manager exists and its

SecurityManager.checkCreateClassLoader()

method
doesn't allow creation of a class loader.

**Since:**
- 9

---

### Method Details

#### protected final
Class
<?> defineClass​(
String
name,
byte[] b,
int off,
int len,

CodeSource
cs)

Converts an array of bytes into an instance of class Class,
with an optional CodeSource. Before the
class can be used it must be resolved.

If a non-null CodeSource is supplied a ProtectionDomain is
constructed and associated with the class being defined.

**Parameters:**
- name

- the expected name of the class, or

null

if not known, using '.' and not '/' as the separator
and without a trailing ".class" suffix.
- b

- the bytes that make up the class data. The bytes in
positions

off

through

off+len-1

should have the format of a valid class file as defined by

The Java™ Virtual Machine Specification

.
- off

- the start offset in

b

of the class data
- len

- the length of the class data
- cs

- the associated CodeSource, or

null

if none

**Returns:**
- the

Class

object created from the data,
and optional CodeSource.

**Throws:**
- ClassFormatError

- if the data did not contain a valid class
- IndexOutOfBoundsException

- if either

off

or

len

is negative, or if

off+len

is greater than

b.length

.
- SecurityException

- if an attempt is made to add this class
to a package that contains classes that were signed by
a different set of certificates than this class, or if
the class name begins with "java.".

---

#### protected final
Class
<?> defineClass​(
String
name,

ByteBuffer
b,

CodeSource
cs)

Converts a

ByteBuffer

into an instance of class

Class

, with an optional CodeSource.
Before the class can be used it must be resolved.

If a non-null CodeSource is supplied a ProtectionDomain is
constructed and associated with the class being defined.

**Parameters:**
- name

- the expected name of the class, or

null

if not known, using '.' and not '/' as the separator
and without a trailing ".class" suffix.
- b

- the bytes that make up the class data. The bytes from positions

b.position()

through

b.position() + b.limit() -1

should have the format of a valid class file as defined by

The Java™ Virtual Machine Specification

.
- cs

- the associated CodeSource, or

null

if none

**Returns:**
- the

Class

object created from the data,
and optional CodeSource.

**Throws:**
- ClassFormatError

- if the data did not contain a valid class
- SecurityException

- if an attempt is made to add this class
to a package that contains classes that were signed by
a different set of certificates than this class, or if
the class name begins with "java.".

**Since:**
- 1.5

---

#### protected
PermissionCollection
getPermissions​(
CodeSource
codesource)

Returns the permissions for the given CodeSource object.

This method is invoked by the defineClass method which takes
a CodeSource as an argument when it is constructing the
ProtectionDomain for the class being defined.

**Parameters:**
- codesource

- the codesource.

**Returns:**
- the permissions granted to the codesource.

---

### Additional Sections

#### Class SecureClassLoader

java.lang.Object

- java.lang.ClassLoader
- - java.security.SecureClassLoader

java.lang.ClassLoader

- java.security.SecureClassLoader

java.security.SecureClassLoader

**Direct Known Subclasses:** URLClassLoader

```java
public class
SecureClassLoader

extends
ClassLoader
```

This class extends ClassLoader with additional support for defining
classes with an associated code source and permissions which are
retrieved by the system policy by default.

**Since:** 1.2

public class

SecureClassLoader

extends

ClassLoader

This class extends ClassLoader with additional support for defining
classes with an associated code source and permissions which are
retrieved by the system policy by default.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SecureClassLoader

()

Creates a new SecureClassLoader using the default parent class
loader for delegation.

protected

SecureClassLoader

​(

ClassLoader

parent)

Creates a new SecureClassLoader using the specified parent
class loader for delegation.

protected

SecureClassLoader

​(

String

name,

ClassLoader

parent)

Creates a new

SecureClassLoader

of the specified name and
using the specified parent class loader for delegation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Class

<?>

defineClass

​(

String

name,
byte[] b,
int off,
int len,

CodeSource

cs)

Converts an array of bytes into an instance of class Class,
with an optional CodeSource.

protected

Class

<?>

defineClass

​(

String

name,

ByteBuffer

b,

CodeSource

cs)

Converts a

ByteBuffer

into an instance of class

Class

, with an optional CodeSource.

protected

PermissionCollection

getPermissions

​(

CodeSource

codesource)

Returns the permissions for the given CodeSource object.

- Methods declared in class java.lang.

ClassLoader

clearAssertionStatus

,

defineClass

,

defineClass

,

defineClass

,

defineClass

,

definePackage

,

findClass

,

findClass

,

findLibrary

,

findLoadedClass

,

findResource

,

findResource

,

findResources

,

findSystemClass

,

getClassLoadingLock

,

getDefinedPackage

,

getDefinedPackages

,

getName

,

getPackage

,

getPackages

,

getParent

,

getPlatformClassLoader

,

getResource

,

getResourceAsStream

,

getResources

,

getSystemClassLoader

,

getSystemResource

,

getSystemResourceAsStream

,

getSystemResources

,

getUnnamedModule

,

isRegisteredAsParallelCapable

,

loadClass

,

loadClass

,

registerAsParallelCapable

,

resolveClass

,

resources

,

setClassAssertionStatus

,

setDefaultAssertionStatus

,

setPackageAssertionStatus

,

setSigners

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

SecureClassLoader

()

Creates a new SecureClassLoader using the default parent class
loader for delegation.

protected

SecureClassLoader

​(

ClassLoader

parent)

Creates a new SecureClassLoader using the specified parent
class loader for delegation.

protected

SecureClassLoader

​(

String

name,

ClassLoader

parent)

Creates a new

SecureClassLoader

of the specified name and
using the specified parent class loader for delegation.

---

#### Constructor Summary

Creates a new SecureClassLoader using the default parent class
loader for delegation.

Creates a new SecureClassLoader using the specified parent
class loader for delegation.

Creates a new

SecureClassLoader

of the specified name and
using the specified parent class loader for delegation.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Class

<?>

defineClass

​(

String

name,
byte[] b,
int off,
int len,

CodeSource

cs)

Converts an array of bytes into an instance of class Class,
with an optional CodeSource.

protected

Class

<?>

defineClass

​(

String

name,

ByteBuffer

b,

CodeSource

cs)

Converts a

ByteBuffer

into an instance of class

Class

, with an optional CodeSource.

protected

PermissionCollection

getPermissions

​(

CodeSource

codesource)

Returns the permissions for the given CodeSource object.

- Methods declared in class java.lang.

ClassLoader

clearAssertionStatus

,

defineClass

,

defineClass

,

defineClass

,

defineClass

,

definePackage

,

findClass

,

findClass

,

findLibrary

,

findLoadedClass

,

findResource

,

findResource

,

findResources

,

findSystemClass

,

getClassLoadingLock

,

getDefinedPackage

,

getDefinedPackages

,

getName

,

getPackage

,

getPackages

,

getParent

,

getPlatformClassLoader

,

getResource

,

getResourceAsStream

,

getResources

,

getSystemClassLoader

,

getSystemResource

,

getSystemResourceAsStream

,

getSystemResources

,

getUnnamedModule

,

isRegisteredAsParallelCapable

,

loadClass

,

loadClass

,

registerAsParallelCapable

,

resolveClass

,

resources

,

setClassAssertionStatus

,

setDefaultAssertionStatus

,

setPackageAssertionStatus

,

setSigners

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

Converts an array of bytes into an instance of class Class,
with an optional CodeSource.

Converts a

ByteBuffer

into an instance of class

Class

, with an optional CodeSource.

Returns the permissions for the given CodeSource object.

Methods declared in class java.lang.

ClassLoader

clearAssertionStatus

,

defineClass

,

defineClass

,

defineClass

,

defineClass

,

definePackage

,

findClass

,

findClass

,

findLibrary

,

findLoadedClass

,

findResource

,

findResource

,

findResources

,

findSystemClass

,

getClassLoadingLock

,

getDefinedPackage

,

getDefinedPackages

,

getName

,

getPackage

,

getPackages

,

getParent

,

getPlatformClassLoader

,

getResource

,

getResourceAsStream

,

getResources

,

getSystemClassLoader

,

getSystemResource

,

getSystemResourceAsStream

,

getSystemResources

,

getUnnamedModule

,

isRegisteredAsParallelCapable

,

loadClass

,

loadClass

,

registerAsParallelCapable

,

resolveClass

,

resources

,

setClassAssertionStatus

,

setDefaultAssertionStatus

,

setPackageAssertionStatus

,

setSigners

---

#### Methods declared in class java.lang. ClassLoader

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

- SecureClassLoader

```java
protected SecureClassLoader​(
ClassLoader
parent)
```

Creates a new SecureClassLoader using the specified parent
class loader for delegation.

If there is a security manager, this method first
calls the security manager's

checkCreateClassLoader

method to ensure creation of a class loader is allowed.

**Parameters:** parent

- the parent ClassLoader
**Throws:** SecurityException

- if a security manager exists and its

checkCreateClassLoader

method doesn't allow
creation of a class loader.
**See Also:** SecurityManager.checkCreateClassLoader()

- SecureClassLoader

```java
protected SecureClassLoader()
```

Creates a new SecureClassLoader using the default parent class
loader for delegation.

If there is a security manager, this method first
calls the security manager's

checkCreateClassLoader

method to ensure creation of a class loader is allowed.

**Throws:** SecurityException

- if a security manager exists and its

checkCreateClassLoader

method doesn't allow
creation of a class loader.
**See Also:** SecurityManager.checkCreateClassLoader()

- SecureClassLoader

```java
protected SecureClassLoader​(
String
name,

ClassLoader
parent)
```

Creates a new

SecureClassLoader

of the specified name and
using the specified parent class loader for delegation.

**Parameters:** name

- class loader name; or

null

if not named
**Parameters:** parent

- the parent class loader
**Throws:** IllegalArgumentException

- if the given name is empty.
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkCreateClassLoader()

method
doesn't allow creation of a class loader.
**Since:** 9

============ METHOD DETAIL ==========

- Method Detail

- defineClass

```java
protected final
Class
<?> defineClass​(
String
name,
byte[] b,
int off,
int len,

CodeSource
cs)
```

Converts an array of bytes into an instance of class Class,
with an optional CodeSource. Before the
class can be used it must be resolved.

If a non-null CodeSource is supplied a ProtectionDomain is
constructed and associated with the class being defined.

**Parameters:** name

- the expected name of the class, or

null

if not known, using '.' and not '/' as the separator
and without a trailing ".class" suffix.
**Parameters:** b

- the bytes that make up the class data. The bytes in
positions

off

through

off+len-1

should have the format of a valid class file as defined by

The Java™ Virtual Machine Specification

.
**Parameters:** off

- the start offset in

b

of the class data
**Parameters:** len

- the length of the class data
**Parameters:** cs

- the associated CodeSource, or

null

if none
**Returns:** the

Class

object created from the data,
and optional CodeSource.
**Throws:** ClassFormatError

- if the data did not contain a valid class
**Throws:** IndexOutOfBoundsException

- if either

off

or

len

is negative, or if

off+len

is greater than

b.length

.
**Throws:** SecurityException

- if an attempt is made to add this class
to a package that contains classes that were signed by
a different set of certificates than this class, or if
the class name begins with "java.".

- defineClass

```java
protected final
Class
<?> defineClass​(
String
name,

ByteBuffer
b,

CodeSource
cs)
```

Converts a

ByteBuffer

into an instance of class

Class

, with an optional CodeSource.
Before the class can be used it must be resolved.

If a non-null CodeSource is supplied a ProtectionDomain is
constructed and associated with the class being defined.

**Parameters:** name

- the expected name of the class, or

null

if not known, using '.' and not '/' as the separator
and without a trailing ".class" suffix.
**Parameters:** b

- the bytes that make up the class data. The bytes from positions

b.position()

through

b.position() + b.limit() -1

should have the format of a valid class file as defined by

The Java™ Virtual Machine Specification

.
**Parameters:** cs

- the associated CodeSource, or

null

if none
**Returns:** the

Class

object created from the data,
and optional CodeSource.
**Throws:** ClassFormatError

- if the data did not contain a valid class
**Throws:** SecurityException

- if an attempt is made to add this class
to a package that contains classes that were signed by
a different set of certificates than this class, or if
the class name begins with "java.".
**Since:** 1.5

- getPermissions

```java
protected
PermissionCollection
getPermissions​(
CodeSource
codesource)
```

Returns the permissions for the given CodeSource object.

This method is invoked by the defineClass method which takes
a CodeSource as an argument when it is constructing the
ProtectionDomain for the class being defined.

**Parameters:** codesource

- the codesource.
**Returns:** the permissions granted to the codesource.

Constructor Detail

- SecureClassLoader

```java
protected SecureClassLoader​(
ClassLoader
parent)
```

Creates a new SecureClassLoader using the specified parent
class loader for delegation.

If there is a security manager, this method first
calls the security manager's

checkCreateClassLoader

method to ensure creation of a class loader is allowed.

**Parameters:** parent

- the parent ClassLoader
**Throws:** SecurityException

- if a security manager exists and its

checkCreateClassLoader

method doesn't allow
creation of a class loader.
**See Also:** SecurityManager.checkCreateClassLoader()

- SecureClassLoader

```java
protected SecureClassLoader()
```

Creates a new SecureClassLoader using the default parent class
loader for delegation.

If there is a security manager, this method first
calls the security manager's

checkCreateClassLoader

method to ensure creation of a class loader is allowed.

**Throws:** SecurityException

- if a security manager exists and its

checkCreateClassLoader

method doesn't allow
creation of a class loader.
**See Also:** SecurityManager.checkCreateClassLoader()

- SecureClassLoader

```java
protected SecureClassLoader​(
String
name,

ClassLoader
parent)
```

Creates a new

SecureClassLoader

of the specified name and
using the specified parent class loader for delegation.

**Parameters:** name

- class loader name; or

null

if not named
**Parameters:** parent

- the parent class loader
**Throws:** IllegalArgumentException

- if the given name is empty.
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkCreateClassLoader()

method
doesn't allow creation of a class loader.
**Since:** 9

---

#### Constructor Detail

SecureClassLoader

```java
protected SecureClassLoader​(
ClassLoader
parent)
```

Creates a new SecureClassLoader using the specified parent
class loader for delegation.

If there is a security manager, this method first
calls the security manager's

checkCreateClassLoader

method to ensure creation of a class loader is allowed.

**Parameters:** parent

- the parent ClassLoader
**Throws:** SecurityException

- if a security manager exists and its

checkCreateClassLoader

method doesn't allow
creation of a class loader.
**See Also:** SecurityManager.checkCreateClassLoader()

---

#### SecureClassLoader

protected SecureClassLoader​(

ClassLoader

parent)

Creates a new SecureClassLoader using the specified parent
class loader for delegation.

If there is a security manager, this method first
calls the security manager's

checkCreateClassLoader

method to ensure creation of a class loader is allowed.

If there is a security manager, this method first
calls the security manager's

checkCreateClassLoader

method to ensure creation of a class loader is allowed.

SecureClassLoader

```java
protected SecureClassLoader()
```

Creates a new SecureClassLoader using the default parent class
loader for delegation.

If there is a security manager, this method first
calls the security manager's

checkCreateClassLoader

method to ensure creation of a class loader is allowed.

**Throws:** SecurityException

- if a security manager exists and its

checkCreateClassLoader

method doesn't allow
creation of a class loader.
**See Also:** SecurityManager.checkCreateClassLoader()

---

#### SecureClassLoader

protected SecureClassLoader()

Creates a new SecureClassLoader using the default parent class
loader for delegation.

If there is a security manager, this method first
calls the security manager's

checkCreateClassLoader

method to ensure creation of a class loader is allowed.

If there is a security manager, this method first
calls the security manager's

checkCreateClassLoader

method to ensure creation of a class loader is allowed.

SecureClassLoader

```java
protected SecureClassLoader​(
String
name,

ClassLoader
parent)
```

Creates a new

SecureClassLoader

of the specified name and
using the specified parent class loader for delegation.

**Parameters:** name

- class loader name; or

null

if not named
**Parameters:** parent

- the parent class loader
**Throws:** IllegalArgumentException

- if the given name is empty.
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkCreateClassLoader()

method
doesn't allow creation of a class loader.
**Since:** 9

---

#### SecureClassLoader

protected SecureClassLoader​(

String

name,

ClassLoader

parent)

Creates a new

SecureClassLoader

of the specified name and
using the specified parent class loader for delegation.

Method Detail

- defineClass

```java
protected final
Class
<?> defineClass​(
String
name,
byte[] b,
int off,
int len,

CodeSource
cs)
```

Converts an array of bytes into an instance of class Class,
with an optional CodeSource. Before the
class can be used it must be resolved.

If a non-null CodeSource is supplied a ProtectionDomain is
constructed and associated with the class being defined.

**Parameters:** name

- the expected name of the class, or

null

if not known, using '.' and not '/' as the separator
and without a trailing ".class" suffix.
**Parameters:** b

- the bytes that make up the class data. The bytes in
positions

off

through

off+len-1

should have the format of a valid class file as defined by

The Java™ Virtual Machine Specification

.
**Parameters:** off

- the start offset in

b

of the class data
**Parameters:** len

- the length of the class data
**Parameters:** cs

- the associated CodeSource, or

null

if none
**Returns:** the

Class

object created from the data,
and optional CodeSource.
**Throws:** ClassFormatError

- if the data did not contain a valid class
**Throws:** IndexOutOfBoundsException

- if either

off

or

len

is negative, or if

off+len

is greater than

b.length

.
**Throws:** SecurityException

- if an attempt is made to add this class
to a package that contains classes that were signed by
a different set of certificates than this class, or if
the class name begins with "java.".

- defineClass

```java
protected final
Class
<?> defineClass​(
String
name,

ByteBuffer
b,

CodeSource
cs)
```

Converts a

ByteBuffer

into an instance of class

Class

, with an optional CodeSource.
Before the class can be used it must be resolved.

If a non-null CodeSource is supplied a ProtectionDomain is
constructed and associated with the class being defined.

**Parameters:** name

- the expected name of the class, or

null

if not known, using '.' and not '/' as the separator
and without a trailing ".class" suffix.
**Parameters:** b

- the bytes that make up the class data. The bytes from positions

b.position()

through

b.position() + b.limit() -1

should have the format of a valid class file as defined by

The Java™ Virtual Machine Specification

.
**Parameters:** cs

- the associated CodeSource, or

null

if none
**Returns:** the

Class

object created from the data,
and optional CodeSource.
**Throws:** ClassFormatError

- if the data did not contain a valid class
**Throws:** SecurityException

- if an attempt is made to add this class
to a package that contains classes that were signed by
a different set of certificates than this class, or if
the class name begins with "java.".
**Since:** 1.5

- getPermissions

```java
protected
PermissionCollection
getPermissions​(
CodeSource
codesource)
```

Returns the permissions for the given CodeSource object.

This method is invoked by the defineClass method which takes
a CodeSource as an argument when it is constructing the
ProtectionDomain for the class being defined.

**Parameters:** codesource

- the codesource.
**Returns:** the permissions granted to the codesource.

---

#### Method Detail

defineClass

```java
protected final
Class
<?> defineClass​(
String
name,
byte[] b,
int off,
int len,

CodeSource
cs)
```

Converts an array of bytes into an instance of class Class,
with an optional CodeSource. Before the
class can be used it must be resolved.

If a non-null CodeSource is supplied a ProtectionDomain is
constructed and associated with the class being defined.

**Parameters:** name

- the expected name of the class, or

null

if not known, using '.' and not '/' as the separator
and without a trailing ".class" suffix.
**Parameters:** b

- the bytes that make up the class data. The bytes in
positions

off

through

off+len-1

should have the format of a valid class file as defined by

The Java™ Virtual Machine Specification

.
**Parameters:** off

- the start offset in

b

of the class data
**Parameters:** len

- the length of the class data
**Parameters:** cs

- the associated CodeSource, or

null

if none
**Returns:** the

Class

object created from the data,
and optional CodeSource.
**Throws:** ClassFormatError

- if the data did not contain a valid class
**Throws:** IndexOutOfBoundsException

- if either

off

or

len

is negative, or if

off+len

is greater than

b.length

.
**Throws:** SecurityException

- if an attempt is made to add this class
to a package that contains classes that were signed by
a different set of certificates than this class, or if
the class name begins with "java.".

---

#### defineClass

protected final

Class

<?> defineClass​(

String

name,
byte[] b,
int off,
int len,

CodeSource

cs)

Converts an array of bytes into an instance of class Class,
with an optional CodeSource. Before the
class can be used it must be resolved.

If a non-null CodeSource is supplied a ProtectionDomain is
constructed and associated with the class being defined.

If a non-null CodeSource is supplied a ProtectionDomain is
constructed and associated with the class being defined.

defineClass

```java
protected final
Class
<?> defineClass​(
String
name,

ByteBuffer
b,

CodeSource
cs)
```

Converts a

ByteBuffer

into an instance of class

Class

, with an optional CodeSource.
Before the class can be used it must be resolved.

If a non-null CodeSource is supplied a ProtectionDomain is
constructed and associated with the class being defined.

**Parameters:** name

- the expected name of the class, or

null

if not known, using '.' and not '/' as the separator
and without a trailing ".class" suffix.
**Parameters:** b

- the bytes that make up the class data. The bytes from positions

b.position()

through

b.position() + b.limit() -1

should have the format of a valid class file as defined by

The Java™ Virtual Machine Specification

.
**Parameters:** cs

- the associated CodeSource, or

null

if none
**Returns:** the

Class

object created from the data,
and optional CodeSource.
**Throws:** ClassFormatError

- if the data did not contain a valid class
**Throws:** SecurityException

- if an attempt is made to add this class
to a package that contains classes that were signed by
a different set of certificates than this class, or if
the class name begins with "java.".
**Since:** 1.5

---

#### defineClass

protected final

Class

<?> defineClass​(

String

name,

ByteBuffer

b,

CodeSource

cs)

Converts a

ByteBuffer

into an instance of class

Class

, with an optional CodeSource.
Before the class can be used it must be resolved.

If a non-null CodeSource is supplied a ProtectionDomain is
constructed and associated with the class being defined.

If a non-null CodeSource is supplied a ProtectionDomain is
constructed and associated with the class being defined.

getPermissions

```java
protected
PermissionCollection
getPermissions​(
CodeSource
codesource)
```

Returns the permissions for the given CodeSource object.

This method is invoked by the defineClass method which takes
a CodeSource as an argument when it is constructing the
ProtectionDomain for the class being defined.

**Parameters:** codesource

- the codesource.
**Returns:** the permissions granted to the codesource.

---

#### getPermissions

protected

PermissionCollection

getPermissions​(

CodeSource

codesource)

Returns the permissions for the given CodeSource object.

This method is invoked by the defineClass method which takes
a CodeSource as an argument when it is constructing the
ProtectionDomain for the class being defined.

This method is invoked by the defineClass method which takes
a CodeSource as an argument when it is constructing the
ProtectionDomain for the class being defined.

---

