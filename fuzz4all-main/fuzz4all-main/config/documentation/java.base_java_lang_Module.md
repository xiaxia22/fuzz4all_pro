# Class Module

**Source:** `java.base\java\lang\Module.html`

### Class Description

```java
public final class
Module

extends
Object

implements
AnnotatedElement
```

Represents a run-time module, either

named

or unnamed.

Named modules have a

name

and are constructed by the
Java Virtual Machine when a graph of modules is defined to the Java virtual
machine to create a

module layer

.

An unnamed module does not have a name. There is an unnamed module for
each

ClassLoader

, obtained by invoking its

getUnnamedModule

method. All types that are
not in a named module are members of their defining class loader's unnamed
module.

The package names that are parameters or returned by methods defined in
this class are the fully-qualified names of the packages as defined in
section 6.5.3 of

The Java™ Language Specification

, for
example,

"java.lang"

.

Unless otherwise specified, passing a

null

argument to a method
in this class causes a

NullPointerException

to
be thrown.

**All Implemented Interfaces:** AnnotatedElement

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public boolean isNamed()

Returns

true

if this module is a named module.

**Returns:**
- true

if this is a named module

**See Also:**
- ClassLoader.getUnnamedModule()

---

#### public
String
getName()

Returns the module name or

null

if this module is an unnamed
module.

**Returns:**
- The module name

---

#### public
ClassLoader
getClassLoader()

Returns the

ClassLoader

for this module.

If there is a security manager then its

checkPermission

method if first called with a

RuntimePermission("getClassLoader")

permission to check that the caller is allowed to get access to the
class loader.

**Returns:**
- The class loader for this module

**Throws:**
- SecurityException

- If denied by the security manager

---

#### public
ModuleDescriptor
getDescriptor()

Returns the module descriptor for this module or

null

if this
module is an unnamed module.

**Returns:**
- The module descriptor for this module

---

#### public
ModuleLayer
getLayer()

Returns the module layer that contains this module or

null

if
this module is not in a module layer.

A module layer contains named modules and therefore this method always
returns

null

when invoked on an unnamed module.

Dynamic modules

are
named modules that are generated at runtime. A dynamic module may or may
not be in a module layer.

**Returns:**
- The module layer that contains this module

**See Also:**
- Proxy

---

#### public boolean canRead​(
Module
other)

Indicates if this module reads the given module. This method returns

true

if invoked to test if this module reads itself. It also
returns

true

if invoked on an unnamed module (as unnamed
modules read all modules).

**Parameters:**
- other

- The other module

**Returns:**
- true

if this module reads

other

**See Also:**
- addReads(Module)

---

#### public
Module
addReads​(
Module
other)

If the caller's module is this module then update this module to read
the given module.

This method is a no-op if

other

is this module (all modules read
themselves), this module is an unnamed module (as unnamed modules read
all modules), or this module already reads

other

.

**Parameters:**
- other

- The other module

**Returns:**
- this module

**Throws:**
- IllegalCallerException

- If this is a named module and the caller's module is not this
module

**See Also:**
- canRead(java.lang.Module)

**Implementation Note:**
- Read edges

added by this method are

weak

and
do not prevent

other

from being GC'ed when this module is
strongly reachable.

---

#### public boolean isExported​(
String
pn,

Module
other)

Returns

true

if this module exports the given package to at
least the given module.

This method returns

true

if invoked to test if a package in
this module is exported to itself. It always returns

true

when
invoked on an unnamed module. A package that is

open

to
the given module is considered exported to that module at run-time and
so this method returns

true

if the package is open to the given
module.

This method does not check if the given module reads this module.

**Parameters:**
- pn

- The package name
- other

- The other module

**Returns:**
- true

if this module exports the package to at least the
given module

**See Also:**
- ModuleDescriptor.exports()

,

addExports(String,Module)

---

#### public boolean isOpen​(
String
pn,

Module
other)

Returns

true

if this module has

opened

a package to at
least the given module.

This method returns

true

if invoked to test if a package in
this module is open to itself. It returns

true

when invoked on an

open

module with a package in the module.
It always returns

true

when invoked on an unnamed module.

This method does not check if the given module reads this module.

**Parameters:**
- pn

- The package name
- other

- The other module

**Returns:**
- true

if this module has

opened

the package
to at least the given module

**See Also:**
- ModuleDescriptor.opens()

,

addOpens(String,Module)

,

AccessibleObject.setAccessible(boolean)

,

MethodHandles.privateLookupIn(java.lang.Class<?>, java.lang.invoke.MethodHandles.Lookup)

---

#### public boolean isExported​(
String
pn)

Returns

true

if this module exports the given package
unconditionally.

This method always returns

true

when invoked on an unnamed
module. A package that is

opened

unconditionally
is considered exported unconditionally at run-time and so this method
returns

true

if the package is opened unconditionally.

This method does not check if the given module reads this module.

**Parameters:**
- pn

- The package name

**Returns:**
- true

if this module exports the package unconditionally

**See Also:**
- ModuleDescriptor.exports()

---

#### public boolean isOpen​(
String
pn)

Returns

true

if this module has

opened

a package
unconditionally.

This method always returns

true

when invoked on an unnamed
module. Additionally, it always returns

true

when invoked on an

open

module with a package in the
module.

This method does not check if the given module reads this module.

**Parameters:**
- pn

- The package name

**Returns:**
- true

if this module has

opened

the package
unconditionally

**See Also:**
- ModuleDescriptor.opens()

---

#### public
Module
addExports​(
String
pn,

Module
other)

If the caller's module is this module then update this module to export
the given package to the given module.

This method has no effect if the package is already exported (or

open

) to the given module.

**Parameters:**
- pn

- The package name
- other

- The module

**Returns:**
- this module

**Throws:**
- IllegalArgumentException

- If

pn

is

null

, or this is a named module and the
package

pn

is not a package in this module
- IllegalCallerException

- If this is a named module and the caller's module is not this
module

**See Also:**
- isExported(String,Module)

**API Note:**
- As specified in section 5.4.3 of the

The Java™
Virtual Machine Specification

, if an attempt to resolve a
symbolic reference fails because of a linkage error, then subsequent
attempts to resolve the reference always fail with the same error that
was thrown as a result of the initial resolution attempt.

**See The Java™ Virtual Machine Specification :**
- 5.4.3 Resolution

---

#### public
Module
addOpens​(
String
pn,

Module
other)

If this module has

opened

a package to at least the caller
module then update this module to open the package to the given module.
Opening a package with this method allows all types in the package,
and all their members, not just public types and their public members,
to be reflected on by the given module when using APIs that support
private access or a way to bypass or suppress default Java language
access control checks.

This method has no effect if the package is already

open

to the given module.

**Parameters:**
- pn

- The package name
- other

- The module

**Returns:**
- this module

**Throws:**
- IllegalArgumentException

- If

pn

is

null

, or this is a named module and the
package

pn

is not a package in this module
- IllegalCallerException

- If this is a named module and this module has not opened the
package to at least the caller's module

**See Also:**
- isOpen(String,Module)

,

AccessibleObject.setAccessible(boolean)

,

MethodHandles.privateLookupIn(java.lang.Class<?>, java.lang.invoke.MethodHandles.Lookup)

**API Note:**
- This method can be used for cases where a

consumer
module

uses a qualified opens to open a package to an

API
module

but where the reflective access to the members of classes in
the consumer module is delegated to code in another module. Code in the
API module can use this method to open the package in the consumer module
to the other module.

---

#### public
Module
addUses​(
Class
<?> service)

If the caller's module is this module then update this module to add a
service dependence on the given service type. This method is intended
for use by frameworks that invoke

ServiceLoader

on behalf of other modules or where the framework is
passed a reference to the service type by other code. This method is
a no-op when invoked on an unnamed module or an automatic module.

This method does not cause

resolveAndBind

to be re-run.

**Parameters:**
- service

- The service type

**Returns:**
- this module

**Throws:**
- IllegalCallerException

- If this is a named module and the caller's module is not this
module

**See Also:**
- canUse(Class)

,

ModuleDescriptor.uses()

---

#### public boolean canUse​(
Class
<?> service)

Indicates if this module has a service dependence on the given service
type. This method always returns

true

when invoked on an unnamed
module or an automatic module.

**Parameters:**
- service

- The service type

**Returns:**
- true

if this module uses service type

st

**See Also:**
- addUses(Class)

---

#### public
Set
<
String
> getPackages()

Returns the set of package names for the packages in this module.

For named modules, the returned set contains an element for each
package in the module.

For unnamed modules, this method is the equivalent to invoking the

getDefinedPackages

method of
this module's class loader and returning the set of package names.

**Returns:**
- the set of the package names of the packages in this module

---

#### public <T extends
Annotation
> T getAnnotation​(
Class
<T> annotationClass)

Returns this element's annotation for the specified type if
such an annotation is

present

, else null.
This method returns

null

when invoked on an unnamed module.

**Specified by:**
- getAnnotation

in interface

AnnotatedElement

**Parameters:**
- annotationClass

- the Class object corresponding to the
annotation type

**Returns:**
- this element's annotation for the specified annotation type if
present on this element, else null

**Type Parameters:**
- T

- the type of the annotation to query for and return if present

---

#### public
Annotation
[] getAnnotations()

Returns annotations that are

present

on this element.

If there are no annotations

present

on this element, the return
value is an array of length 0.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.
This method returns an empty array when invoked on an unnamed module.

**Specified by:**
- getAnnotations

in interface

AnnotatedElement

**Returns:**
- annotations present on this element

---

#### public
Annotation
[] getDeclaredAnnotations()

Returns annotations that are

directly present

on this element.
This method ignores inherited annotations.

If there are no annotations

directly present

on this element,
the return value is an array of length 0.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.
This method returns an empty array when invoked on an unnamed module.

**Specified by:**
- getDeclaredAnnotations

in interface

AnnotatedElement

**Returns:**
- annotations directly present on this element

---

#### public
InputStream
getResourceAsStream​(
String
name)
throws
IOException

Returns an input stream for reading a resource in this module.
The

name

parameter is a

'/'

-separated path name that
identifies the resource. As with

Class.getResourceAsStream

, this method delegates to the module's class
loader

findResource(String,String)

method, invoking it with the module name
(or

null

when the module is unnamed) and the name of the
resource. If the resource name has a leading slash then it is dropped
before delegation.

A resource in a named module may be

encapsulated

so that
it cannot be located by code in other modules. Whether a resource can be
located or not is determined as follows:

- If the resource name ends with "

.class

" then it is not
encapsulated.
- A

package name

is derived from the resource name. If
the package name is a

package

in the
module then the resource can only be located by the caller of this
method when the package is

open

to at least the caller's module. If the resource is not in a
package in the module then the resource is not encapsulated.

In the above, the

package name

for a resource is derived
from the subsequence of characters that precedes the last

'/'

in
the name and then replacing each

'/'

character in the subsequence
with

'.'

. A leading slash is ignored when deriving the package
name. As an example, the package name derived for a resource named
"

a/b/c/foo.properties

" is "

a.b.c

". A resource name
with the name "

META-INF/MANIFEST.MF

" is never encapsulated
because "

META-INF

" is not a legal package name.

This method returns

null

if the resource is not in this
module, the resource is encapsulated and cannot be located by the caller,
or access to the resource is denied by the security manager.

**Parameters:**
- name

- The resource name

**Returns:**
- An input stream for reading the resource or

null

**Throws:**
- IOException

- If an I/O error occurs

**See Also:**
- Class.getResourceAsStream(String)

---

#### public
String
toString()

Returns the string representation of this module. For a named module,
the representation is the string

"module"

, followed by a space,
and then the module name. For an unnamed module, the representation is
the string

"unnamed module"

, followed by a space, and then an
implementation specific string that identifies the unnamed module.

**Overrides:**
- toString

in class

Object

**Returns:**
- The string representation of this module

---

### Additional Sections

#### Class Module

java.lang.Object

- java.lang.Module

java.lang.Module

**All Implemented Interfaces:** AnnotatedElement

```java
public final class
Module

extends
Object

implements
AnnotatedElement
```

Represents a run-time module, either

named

or unnamed.

Named modules have a

name

and are constructed by the
Java Virtual Machine when a graph of modules is defined to the Java virtual
machine to create a

module layer

.

An unnamed module does not have a name. There is an unnamed module for
each

ClassLoader

, obtained by invoking its

getUnnamedModule

method. All types that are
not in a named module are members of their defining class loader's unnamed
module.

The package names that are parameters or returned by methods defined in
this class are the fully-qualified names of the packages as defined in
section 6.5.3 of

The Java™ Language Specification

, for
example,

"java.lang"

.

Unless otherwise specified, passing a

null

argument to a method
in this class causes a

NullPointerException

to
be thrown.

**Since:** 9
**See Also:** Class.getModule()

public final class

Module

extends

Object

implements

AnnotatedElement

Represents a run-time module, either

named

or unnamed.

Named modules have a

name

and are constructed by the
Java Virtual Machine when a graph of modules is defined to the Java virtual
machine to create a

module layer

.

An unnamed module does not have a name. There is an unnamed module for
each

ClassLoader

, obtained by invoking its

getUnnamedModule

method. All types that are
not in a named module are members of their defining class loader's unnamed
module.

The package names that are parameters or returned by methods defined in
this class are the fully-qualified names of the packages as defined in
section 6.5.3 of

The Java™ Language Specification

, for
example,

"java.lang"

.

Unless otherwise specified, passing a

null

argument to a method
in this class causes a

NullPointerException

to
be thrown.

Named modules have a

name

and are constructed by the
Java Virtual Machine when a graph of modules is defined to the Java virtual
machine to create a

module layer

.

An unnamed module does not have a name. There is an unnamed module for
each

ClassLoader

, obtained by invoking its

getUnnamedModule

method. All types that are
not in a named module are members of their defining class loader's unnamed
module.

The package names that are parameters or returned by methods defined in
this class are the fully-qualified names of the packages as defined in
section 6.5.3 of

The Java™ Language Specification

, for
example,

"java.lang"

.

Unless otherwise specified, passing a

null

argument to a method
in this class causes a

NullPointerException

to
be thrown.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Module

addExports

​(

String

pn,

Module

other)

If the caller's module is this module then update this module to export
the given package to the given module.

Module

addOpens

​(

String

pn,

Module

other)

If this module has

opened

a package to at least the caller
module then update this module to open the package to the given module.

Module

addReads

​(

Module

other)

If the caller's module is this module then update this module to read
the given module.

Module

addUses

​(

Class

<?> service)

If the caller's module is this module then update this module to add a
service dependence on the given service type.

boolean

canRead

​(

Module

other)

Indicates if this module reads the given module.

boolean

canUse

​(

Class

<?> service)

Indicates if this module has a service dependence on the given service
type.

<T extends

Annotation

>

T

getAnnotation

​(

Class

<T> annotationClass)

Returns this element's annotation for the specified type if
such an annotation is

present

, else null.

Annotation

[]

getAnnotations

()

Returns annotations that are

present

on this element.

ClassLoader

getClassLoader

()

Returns the

ClassLoader

for this module.

Annotation

[]

getDeclaredAnnotations

()

Returns annotations that are

directly present

on this element.

ModuleDescriptor

getDescriptor

()

Returns the module descriptor for this module or

null

if this
module is an unnamed module.

ModuleLayer

getLayer

()

Returns the module layer that contains this module or

null

if
this module is not in a module layer.

String

getName

()

Returns the module name or

null

if this module is an unnamed
module.

Set

<

String

>

getPackages

()

Returns the set of package names for the packages in this module.

InputStream

getResourceAsStream

​(

String

name)

Returns an input stream for reading a resource in this module.

boolean

isExported

​(

String

pn)

Returns

true

if this module exports the given package
unconditionally.

boolean

isExported

​(

String

pn,

Module

other)

Returns

true

if this module exports the given package to at
least the given module.

boolean

isNamed

()

Returns

true

if this module is a named module.

boolean

isOpen

​(

String

pn)

Returns

true

if this module has

opened

a package
unconditionally.

boolean

isOpen

​(

String

pn,

Module

other)

Returns

true

if this module has

opened

a package to at
least the given module.

String

toString

()

Returns the string representation of this module.

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

- Methods declared in interface java.lang.reflect.

AnnotatedElement

getAnnotationsByType

,

getDeclaredAnnotation

,

getDeclaredAnnotationsByType

,

isAnnotationPresent

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Module

addExports

​(

String

pn,

Module

other)

If the caller's module is this module then update this module to export
the given package to the given module.

Module

addOpens

​(

String

pn,

Module

other)

If this module has

opened

a package to at least the caller
module then update this module to open the package to the given module.

Module

addReads

​(

Module

other)

If the caller's module is this module then update this module to read
the given module.

Module

addUses

​(

Class

<?> service)

If the caller's module is this module then update this module to add a
service dependence on the given service type.

boolean

canRead

​(

Module

other)

Indicates if this module reads the given module.

boolean

canUse

​(

Class

<?> service)

Indicates if this module has a service dependence on the given service
type.

<T extends

Annotation

>

T

getAnnotation

​(

Class

<T> annotationClass)

Returns this element's annotation for the specified type if
such an annotation is

present

, else null.

Annotation

[]

getAnnotations

()

Returns annotations that are

present

on this element.

ClassLoader

getClassLoader

()

Returns the

ClassLoader

for this module.

Annotation

[]

getDeclaredAnnotations

()

Returns annotations that are

directly present

on this element.

ModuleDescriptor

getDescriptor

()

Returns the module descriptor for this module or

null

if this
module is an unnamed module.

ModuleLayer

getLayer

()

Returns the module layer that contains this module or

null

if
this module is not in a module layer.

String

getName

()

Returns the module name or

null

if this module is an unnamed
module.

Set

<

String

>

getPackages

()

Returns the set of package names for the packages in this module.

InputStream

getResourceAsStream

​(

String

name)

Returns an input stream for reading a resource in this module.

boolean

isExported

​(

String

pn)

Returns

true

if this module exports the given package
unconditionally.

boolean

isExported

​(

String

pn,

Module

other)

Returns

true

if this module exports the given package to at
least the given module.

boolean

isNamed

()

Returns

true

if this module is a named module.

boolean

isOpen

​(

String

pn)

Returns

true

if this module has

opened

a package
unconditionally.

boolean

isOpen

​(

String

pn,

Module

other)

Returns

true

if this module has

opened

a package to at
least the given module.

String

toString

()

Returns the string representation of this module.

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

- Methods declared in interface java.lang.reflect.

AnnotatedElement

getAnnotationsByType

,

getDeclaredAnnotation

,

getDeclaredAnnotationsByType

,

isAnnotationPresent

---

#### Method Summary

If the caller's module is this module then update this module to export
the given package to the given module.

If this module has

opened

a package to at least the caller
module then update this module to open the package to the given module.

If the caller's module is this module then update this module to read
the given module.

If the caller's module is this module then update this module to add a
service dependence on the given service type.

Indicates if this module reads the given module.

Indicates if this module has a service dependence on the given service
type.

Returns this element's annotation for the specified type if
such an annotation is

present

, else null.

Returns annotations that are

present

on this element.

Returns the

ClassLoader

for this module.

Returns annotations that are

directly present

on this element.

Returns the module descriptor for this module or

null

if this
module is an unnamed module.

Returns the module layer that contains this module or

null

if
this module is not in a module layer.

Returns the module name or

null

if this module is an unnamed
module.

Returns the set of package names for the packages in this module.

Returns an input stream for reading a resource in this module.

Returns

true

if this module exports the given package
unconditionally.

Returns

true

if this module exports the given package to at
least the given module.

Returns

true

if this module is a named module.

Returns

true

if this module has

opened

a package
unconditionally.

Returns

true

if this module has

opened

a package to at
least the given module.

Returns the string representation of this module.

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

Methods declared in interface java.lang.reflect.

AnnotatedElement

getAnnotationsByType

,

getDeclaredAnnotation

,

getDeclaredAnnotationsByType

,

isAnnotationPresent

---

#### Methods declared in interface java.lang.reflect. AnnotatedElement

============ METHOD DETAIL ==========

- Method Detail

- isNamed

```java
public boolean isNamed()
```

Returns

true

if this module is a named module.

**Returns:** true

if this is a named module
**See Also:** ClassLoader.getUnnamedModule()

- getName

```java
public
String
getName()
```

Returns the module name or

null

if this module is an unnamed
module.

**Returns:** The module name

- getClassLoader

```java
public
ClassLoader
getClassLoader()
```

Returns the

ClassLoader

for this module.

If there is a security manager then its

checkPermission

method if first called with a

RuntimePermission("getClassLoader")

permission to check that the caller is allowed to get access to the
class loader.

**Returns:** The class loader for this module
**Throws:** SecurityException

- If denied by the security manager

- getDescriptor

```java
public
ModuleDescriptor
getDescriptor()
```

Returns the module descriptor for this module or

null

if this
module is an unnamed module.

**Returns:** The module descriptor for this module

- getLayer

```java
public
ModuleLayer
getLayer()
```

Returns the module layer that contains this module or

null

if
this module is not in a module layer.

A module layer contains named modules and therefore this method always
returns

null

when invoked on an unnamed module.

Dynamic modules

are
named modules that are generated at runtime. A dynamic module may or may
not be in a module layer.

**Returns:** The module layer that contains this module
**See Also:** Proxy

- canRead

```java
public boolean canRead​(
Module
other)
```

Indicates if this module reads the given module. This method returns

true

if invoked to test if this module reads itself. It also
returns

true

if invoked on an unnamed module (as unnamed
modules read all modules).

**Parameters:** other

- The other module
**Returns:** true

if this module reads

other
**See Also:** addReads(Module)

- addReads

```java
public
Module
addReads​(
Module
other)
```

If the caller's module is this module then update this module to read
the given module.

This method is a no-op if

other

is this module (all modules read
themselves), this module is an unnamed module (as unnamed modules read
all modules), or this module already reads

other

.

**Implementation Note:** Read edges

added by this method are

weak

and
do not prevent

other

from being GC'ed when this module is
strongly reachable.
**Parameters:** other

- The other module
**Returns:** this module
**Throws:** IllegalCallerException

- If this is a named module and the caller's module is not this
module
**See Also:** canRead(java.lang.Module)

- isExported

```java
public boolean isExported​(
String
pn,

Module
other)
```

Returns

true

if this module exports the given package to at
least the given module.

This method returns

true

if invoked to test if a package in
this module is exported to itself. It always returns

true

when
invoked on an unnamed module. A package that is

open

to
the given module is considered exported to that module at run-time and
so this method returns

true

if the package is open to the given
module.

This method does not check if the given module reads this module.

**Parameters:** pn

- The package name
**Parameters:** other

- The other module
**Returns:** true

if this module exports the package to at least the
given module
**See Also:** ModuleDescriptor.exports()

,

addExports(String,Module)

- isOpen

```java
public boolean isOpen​(
String
pn,

Module
other)
```

Returns

true

if this module has

opened

a package to at
least the given module.

This method returns

true

if invoked to test if a package in
this module is open to itself. It returns

true

when invoked on an

open

module with a package in the module.
It always returns

true

when invoked on an unnamed module.

This method does not check if the given module reads this module.

**Parameters:** pn

- The package name
**Parameters:** other

- The other module
**Returns:** true

if this module has

opened

the package
to at least the given module
**See Also:** ModuleDescriptor.opens()

,

addOpens(String,Module)

,

AccessibleObject.setAccessible(boolean)

,

MethodHandles.privateLookupIn(java.lang.Class<?>, java.lang.invoke.MethodHandles.Lookup)

- isExported

```java
public boolean isExported​(
String
pn)
```

Returns

true

if this module exports the given package
unconditionally.

This method always returns

true

when invoked on an unnamed
module. A package that is

opened

unconditionally
is considered exported unconditionally at run-time and so this method
returns

true

if the package is opened unconditionally.

This method does not check if the given module reads this module.

**Parameters:** pn

- The package name
**Returns:** true

if this module exports the package unconditionally
**See Also:** ModuleDescriptor.exports()

- isOpen

```java
public boolean isOpen​(
String
pn)
```

Returns

true

if this module has

opened

a package
unconditionally.

This method always returns

true

when invoked on an unnamed
module. Additionally, it always returns

true

when invoked on an

open

module with a package in the
module.

This method does not check if the given module reads this module.

**Parameters:** pn

- The package name
**Returns:** true

if this module has

opened

the package
unconditionally
**See Also:** ModuleDescriptor.opens()

- addExports

```java
public
Module
addExports​(
String
pn,

Module
other)
```

If the caller's module is this module then update this module to export
the given package to the given module.

This method has no effect if the package is already exported (or

open

) to the given module.

**API Note:** As specified in section 5.4.3 of the

The Java™
Virtual Machine Specification

, if an attempt to resolve a
symbolic reference fails because of a linkage error, then subsequent
attempts to resolve the reference always fail with the same error that
was thrown as a result of the initial resolution attempt.
**Parameters:** pn

- The package name
**Parameters:** other

- The module
**Returns:** this module
**Throws:** IllegalArgumentException

- If

pn

is

null

, or this is a named module and the
package

pn

is not a package in this module
**Throws:** IllegalCallerException

- If this is a named module and the caller's module is not this
module
**See Also:** isExported(String,Module)
**See The Java™ Virtual Machine Specification :** 5.4.3 Resolution

- addOpens

```java
public
Module
addOpens​(
String
pn,

Module
other)
```

If this module has

opened

a package to at least the caller
module then update this module to open the package to the given module.
Opening a package with this method allows all types in the package,
and all their members, not just public types and their public members,
to be reflected on by the given module when using APIs that support
private access or a way to bypass or suppress default Java language
access control checks.

This method has no effect if the package is already

open

to the given module.

**API Note:** This method can be used for cases where a

consumer
module

uses a qualified opens to open a package to an

API
module

but where the reflective access to the members of classes in
the consumer module is delegated to code in another module. Code in the
API module can use this method to open the package in the consumer module
to the other module.
**Parameters:** pn

- The package name
**Parameters:** other

- The module
**Returns:** this module
**Throws:** IllegalArgumentException

- If

pn

is

null

, or this is a named module and the
package

pn

is not a package in this module
**Throws:** IllegalCallerException

- If this is a named module and this module has not opened the
package to at least the caller's module
**See Also:** isOpen(String,Module)

,

AccessibleObject.setAccessible(boolean)

,

MethodHandles.privateLookupIn(java.lang.Class<?>, java.lang.invoke.MethodHandles.Lookup)

- addUses

```java
public
Module
addUses​(
Class
<?> service)
```

If the caller's module is this module then update this module to add a
service dependence on the given service type. This method is intended
for use by frameworks that invoke

ServiceLoader

on behalf of other modules or where the framework is
passed a reference to the service type by other code. This method is
a no-op when invoked on an unnamed module or an automatic module.

This method does not cause

resolveAndBind

to be re-run.

**Parameters:** service

- The service type
**Returns:** this module
**Throws:** IllegalCallerException

- If this is a named module and the caller's module is not this
module
**See Also:** canUse(Class)

,

ModuleDescriptor.uses()

- canUse

```java
public boolean canUse​(
Class
<?> service)
```

Indicates if this module has a service dependence on the given service
type. This method always returns

true

when invoked on an unnamed
module or an automatic module.

**Parameters:** service

- The service type
**Returns:** true

if this module uses service type

st
**See Also:** addUses(Class)

- getPackages

```java
public
Set
<
String
> getPackages()
```

Returns the set of package names for the packages in this module.

For named modules, the returned set contains an element for each
package in the module.

For unnamed modules, this method is the equivalent to invoking the

getDefinedPackages

method of
this module's class loader and returning the set of package names.

**Returns:** the set of the package names of the packages in this module

- getAnnotation

```java
public <T extends
Annotation
> T getAnnotation​(
Class
<T> annotationClass)
```

Returns this element's annotation for the specified type if
such an annotation is

present

, else null.
This method returns

null

when invoked on an unnamed module.

**Specified by:** getAnnotation

in interface

AnnotatedElement
**Type Parameters:** T

- the type of the annotation to query for and return if present
**Parameters:** annotationClass

- the Class object corresponding to the
annotation type
**Returns:** this element's annotation for the specified annotation type if
present on this element, else null

- getAnnotations

```java
public
Annotation
[] getAnnotations()
```

Returns annotations that are

present

on this element.

If there are no annotations

present

on this element, the return
value is an array of length 0.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.
This method returns an empty array when invoked on an unnamed module.

**Specified by:** getAnnotations

in interface

AnnotatedElement
**Returns:** annotations present on this element

- getDeclaredAnnotations

```java
public
Annotation
[] getDeclaredAnnotations()
```

Returns annotations that are

directly present

on this element.
This method ignores inherited annotations.

If there are no annotations

directly present

on this element,
the return value is an array of length 0.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.
This method returns an empty array when invoked on an unnamed module.

**Specified by:** getDeclaredAnnotations

in interface

AnnotatedElement
**Returns:** annotations directly present on this element

- getResourceAsStream

```java
public
InputStream
getResourceAsStream​(
String
name)
throws
IOException
```

Returns an input stream for reading a resource in this module.
The

name

parameter is a

'/'

-separated path name that
identifies the resource. As with

Class.getResourceAsStream

, this method delegates to the module's class
loader

findResource(String,String)

method, invoking it with the module name
(or

null

when the module is unnamed) and the name of the
resource. If the resource name has a leading slash then it is dropped
before delegation.

A resource in a named module may be

encapsulated

so that
it cannot be located by code in other modules. Whether a resource can be
located or not is determined as follows:

- If the resource name ends with "

.class

" then it is not
encapsulated.
- A

package name

is derived from the resource name. If
the package name is a

package

in the
module then the resource can only be located by the caller of this
method when the package is

open

to at least the caller's module. If the resource is not in a
package in the module then the resource is not encapsulated.

In the above, the

package name

for a resource is derived
from the subsequence of characters that precedes the last

'/'

in
the name and then replacing each

'/'

character in the subsequence
with

'.'

. A leading slash is ignored when deriving the package
name. As an example, the package name derived for a resource named
"

a/b/c/foo.properties

" is "

a.b.c

". A resource name
with the name "

META-INF/MANIFEST.MF

" is never encapsulated
because "

META-INF

" is not a legal package name.

This method returns

null

if the resource is not in this
module, the resource is encapsulated and cannot be located by the caller,
or access to the resource is denied by the security manager.

**Parameters:** name

- The resource name
**Returns:** An input stream for reading the resource or

null
**Throws:** IOException

- If an I/O error occurs
**See Also:** Class.getResourceAsStream(String)

- toString

```java
public
String
toString()
```

Returns the string representation of this module. For a named module,
the representation is the string

"module"

, followed by a space,
and then the module name. For an unnamed module, the representation is
the string

"unnamed module"

, followed by a space, and then an
implementation specific string that identifies the unnamed module.

**Overrides:** toString

in class

Object
**Returns:** The string representation of this module

Method Detail

- isNamed

```java
public boolean isNamed()
```

Returns

true

if this module is a named module.

**Returns:** true

if this is a named module
**See Also:** ClassLoader.getUnnamedModule()

- getName

```java
public
String
getName()
```

Returns the module name or

null

if this module is an unnamed
module.

**Returns:** The module name

- getClassLoader

```java
public
ClassLoader
getClassLoader()
```

Returns the

ClassLoader

for this module.

If there is a security manager then its

checkPermission

method if first called with a

RuntimePermission("getClassLoader")

permission to check that the caller is allowed to get access to the
class loader.

**Returns:** The class loader for this module
**Throws:** SecurityException

- If denied by the security manager

- getDescriptor

```java
public
ModuleDescriptor
getDescriptor()
```

Returns the module descriptor for this module or

null

if this
module is an unnamed module.

**Returns:** The module descriptor for this module

- getLayer

```java
public
ModuleLayer
getLayer()
```

Returns the module layer that contains this module or

null

if
this module is not in a module layer.

A module layer contains named modules and therefore this method always
returns

null

when invoked on an unnamed module.

Dynamic modules

are
named modules that are generated at runtime. A dynamic module may or may
not be in a module layer.

**Returns:** The module layer that contains this module
**See Also:** Proxy

- canRead

```java
public boolean canRead​(
Module
other)
```

Indicates if this module reads the given module. This method returns

true

if invoked to test if this module reads itself. It also
returns

true

if invoked on an unnamed module (as unnamed
modules read all modules).

**Parameters:** other

- The other module
**Returns:** true

if this module reads

other
**See Also:** addReads(Module)

- addReads

```java
public
Module
addReads​(
Module
other)
```

If the caller's module is this module then update this module to read
the given module.

This method is a no-op if

other

is this module (all modules read
themselves), this module is an unnamed module (as unnamed modules read
all modules), or this module already reads

other

.

**Implementation Note:** Read edges

added by this method are

weak

and
do not prevent

other

from being GC'ed when this module is
strongly reachable.
**Parameters:** other

- The other module
**Returns:** this module
**Throws:** IllegalCallerException

- If this is a named module and the caller's module is not this
module
**See Also:** canRead(java.lang.Module)

- isExported

```java
public boolean isExported​(
String
pn,

Module
other)
```

Returns

true

if this module exports the given package to at
least the given module.

This method returns

true

if invoked to test if a package in
this module is exported to itself. It always returns

true

when
invoked on an unnamed module. A package that is

open

to
the given module is considered exported to that module at run-time and
so this method returns

true

if the package is open to the given
module.

This method does not check if the given module reads this module.

**Parameters:** pn

- The package name
**Parameters:** other

- The other module
**Returns:** true

if this module exports the package to at least the
given module
**See Also:** ModuleDescriptor.exports()

,

addExports(String,Module)

- isOpen

```java
public boolean isOpen​(
String
pn,

Module
other)
```

Returns

true

if this module has

opened

a package to at
least the given module.

This method returns

true

if invoked to test if a package in
this module is open to itself. It returns

true

when invoked on an

open

module with a package in the module.
It always returns

true

when invoked on an unnamed module.

This method does not check if the given module reads this module.

**Parameters:** pn

- The package name
**Parameters:** other

- The other module
**Returns:** true

if this module has

opened

the package
to at least the given module
**See Also:** ModuleDescriptor.opens()

,

addOpens(String,Module)

,

AccessibleObject.setAccessible(boolean)

,

MethodHandles.privateLookupIn(java.lang.Class<?>, java.lang.invoke.MethodHandles.Lookup)

- isExported

```java
public boolean isExported​(
String
pn)
```

Returns

true

if this module exports the given package
unconditionally.

This method always returns

true

when invoked on an unnamed
module. A package that is

opened

unconditionally
is considered exported unconditionally at run-time and so this method
returns

true

if the package is opened unconditionally.

This method does not check if the given module reads this module.

**Parameters:** pn

- The package name
**Returns:** true

if this module exports the package unconditionally
**See Also:** ModuleDescriptor.exports()

- isOpen

```java
public boolean isOpen​(
String
pn)
```

Returns

true

if this module has

opened

a package
unconditionally.

This method always returns

true

when invoked on an unnamed
module. Additionally, it always returns

true

when invoked on an

open

module with a package in the
module.

This method does not check if the given module reads this module.

**Parameters:** pn

- The package name
**Returns:** true

if this module has

opened

the package
unconditionally
**See Also:** ModuleDescriptor.opens()

- addExports

```java
public
Module
addExports​(
String
pn,

Module
other)
```

If the caller's module is this module then update this module to export
the given package to the given module.

This method has no effect if the package is already exported (or

open

) to the given module.

**API Note:** As specified in section 5.4.3 of the

The Java™
Virtual Machine Specification

, if an attempt to resolve a
symbolic reference fails because of a linkage error, then subsequent
attempts to resolve the reference always fail with the same error that
was thrown as a result of the initial resolution attempt.
**Parameters:** pn

- The package name
**Parameters:** other

- The module
**Returns:** this module
**Throws:** IllegalArgumentException

- If

pn

is

null

, or this is a named module and the
package

pn

is not a package in this module
**Throws:** IllegalCallerException

- If this is a named module and the caller's module is not this
module
**See Also:** isExported(String,Module)
**See The Java™ Virtual Machine Specification :** 5.4.3 Resolution

- addOpens

```java
public
Module
addOpens​(
String
pn,

Module
other)
```

If this module has

opened

a package to at least the caller
module then update this module to open the package to the given module.
Opening a package with this method allows all types in the package,
and all their members, not just public types and their public members,
to be reflected on by the given module when using APIs that support
private access or a way to bypass or suppress default Java language
access control checks.

This method has no effect if the package is already

open

to the given module.

**API Note:** This method can be used for cases where a

consumer
module

uses a qualified opens to open a package to an

API
module

but where the reflective access to the members of classes in
the consumer module is delegated to code in another module. Code in the
API module can use this method to open the package in the consumer module
to the other module.
**Parameters:** pn

- The package name
**Parameters:** other

- The module
**Returns:** this module
**Throws:** IllegalArgumentException

- If

pn

is

null

, or this is a named module and the
package

pn

is not a package in this module
**Throws:** IllegalCallerException

- If this is a named module and this module has not opened the
package to at least the caller's module
**See Also:** isOpen(String,Module)

,

AccessibleObject.setAccessible(boolean)

,

MethodHandles.privateLookupIn(java.lang.Class<?>, java.lang.invoke.MethodHandles.Lookup)

- addUses

```java
public
Module
addUses​(
Class
<?> service)
```

If the caller's module is this module then update this module to add a
service dependence on the given service type. This method is intended
for use by frameworks that invoke

ServiceLoader

on behalf of other modules or where the framework is
passed a reference to the service type by other code. This method is
a no-op when invoked on an unnamed module or an automatic module.

This method does not cause

resolveAndBind

to be re-run.

**Parameters:** service

- The service type
**Returns:** this module
**Throws:** IllegalCallerException

- If this is a named module and the caller's module is not this
module
**See Also:** canUse(Class)

,

ModuleDescriptor.uses()

- canUse

```java
public boolean canUse​(
Class
<?> service)
```

Indicates if this module has a service dependence on the given service
type. This method always returns

true

when invoked on an unnamed
module or an automatic module.

**Parameters:** service

- The service type
**Returns:** true

if this module uses service type

st
**See Also:** addUses(Class)

- getPackages

```java
public
Set
<
String
> getPackages()
```

Returns the set of package names for the packages in this module.

For named modules, the returned set contains an element for each
package in the module.

For unnamed modules, this method is the equivalent to invoking the

getDefinedPackages

method of
this module's class loader and returning the set of package names.

**Returns:** the set of the package names of the packages in this module

- getAnnotation

```java
public <T extends
Annotation
> T getAnnotation​(
Class
<T> annotationClass)
```

Returns this element's annotation for the specified type if
such an annotation is

present

, else null.
This method returns

null

when invoked on an unnamed module.

**Specified by:** getAnnotation

in interface

AnnotatedElement
**Type Parameters:** T

- the type of the annotation to query for and return if present
**Parameters:** annotationClass

- the Class object corresponding to the
annotation type
**Returns:** this element's annotation for the specified annotation type if
present on this element, else null

- getAnnotations

```java
public
Annotation
[] getAnnotations()
```

Returns annotations that are

present

on this element.

If there are no annotations

present

on this element, the return
value is an array of length 0.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.
This method returns an empty array when invoked on an unnamed module.

**Specified by:** getAnnotations

in interface

AnnotatedElement
**Returns:** annotations present on this element

- getDeclaredAnnotations

```java
public
Annotation
[] getDeclaredAnnotations()
```

Returns annotations that are

directly present

on this element.
This method ignores inherited annotations.

If there are no annotations

directly present

on this element,
the return value is an array of length 0.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.
This method returns an empty array when invoked on an unnamed module.

**Specified by:** getDeclaredAnnotations

in interface

AnnotatedElement
**Returns:** annotations directly present on this element

- getResourceAsStream

```java
public
InputStream
getResourceAsStream​(
String
name)
throws
IOException
```

Returns an input stream for reading a resource in this module.
The

name

parameter is a

'/'

-separated path name that
identifies the resource. As with

Class.getResourceAsStream

, this method delegates to the module's class
loader

findResource(String,String)

method, invoking it with the module name
(or

null

when the module is unnamed) and the name of the
resource. If the resource name has a leading slash then it is dropped
before delegation.

A resource in a named module may be

encapsulated

so that
it cannot be located by code in other modules. Whether a resource can be
located or not is determined as follows:

- If the resource name ends with "

.class

" then it is not
encapsulated.
- A

package name

is derived from the resource name. If
the package name is a

package

in the
module then the resource can only be located by the caller of this
method when the package is

open

to at least the caller's module. If the resource is not in a
package in the module then the resource is not encapsulated.

In the above, the

package name

for a resource is derived
from the subsequence of characters that precedes the last

'/'

in
the name and then replacing each

'/'

character in the subsequence
with

'.'

. A leading slash is ignored when deriving the package
name. As an example, the package name derived for a resource named
"

a/b/c/foo.properties

" is "

a.b.c

". A resource name
with the name "

META-INF/MANIFEST.MF

" is never encapsulated
because "

META-INF

" is not a legal package name.

This method returns

null

if the resource is not in this
module, the resource is encapsulated and cannot be located by the caller,
or access to the resource is denied by the security manager.

**Parameters:** name

- The resource name
**Returns:** An input stream for reading the resource or

null
**Throws:** IOException

- If an I/O error occurs
**See Also:** Class.getResourceAsStream(String)

- toString

```java
public
String
toString()
```

Returns the string representation of this module. For a named module,
the representation is the string

"module"

, followed by a space,
and then the module name. For an unnamed module, the representation is
the string

"unnamed module"

, followed by a space, and then an
implementation specific string that identifies the unnamed module.

**Overrides:** toString

in class

Object
**Returns:** The string representation of this module

---

#### Method Detail

isNamed

```java
public boolean isNamed()
```

Returns

true

if this module is a named module.

**Returns:** true

if this is a named module
**See Also:** ClassLoader.getUnnamedModule()

---

#### isNamed

public boolean isNamed()

Returns

true

if this module is a named module.

getName

```java
public
String
getName()
```

Returns the module name or

null

if this module is an unnamed
module.

**Returns:** The module name

---

#### getName

public

String

getName()

Returns the module name or

null

if this module is an unnamed
module.

getClassLoader

```java
public
ClassLoader
getClassLoader()
```

Returns the

ClassLoader

for this module.

If there is a security manager then its

checkPermission

method if first called with a

RuntimePermission("getClassLoader")

permission to check that the caller is allowed to get access to the
class loader.

**Returns:** The class loader for this module
**Throws:** SecurityException

- If denied by the security manager

---

#### getClassLoader

public

ClassLoader

getClassLoader()

Returns the

ClassLoader

for this module.

If there is a security manager then its

checkPermission

method if first called with a

RuntimePermission("getClassLoader")

permission to check that the caller is allowed to get access to the
class loader.

If there is a security manager then its

checkPermission

method if first called with a

RuntimePermission("getClassLoader")

permission to check that the caller is allowed to get access to the
class loader.

getDescriptor

```java
public
ModuleDescriptor
getDescriptor()
```

Returns the module descriptor for this module or

null

if this
module is an unnamed module.

**Returns:** The module descriptor for this module

---

#### getDescriptor

public

ModuleDescriptor

getDescriptor()

Returns the module descriptor for this module or

null

if this
module is an unnamed module.

getLayer

```java
public
ModuleLayer
getLayer()
```

Returns the module layer that contains this module or

null

if
this module is not in a module layer.

A module layer contains named modules and therefore this method always
returns

null

when invoked on an unnamed module.

Dynamic modules

are
named modules that are generated at runtime. A dynamic module may or may
not be in a module layer.

**Returns:** The module layer that contains this module
**See Also:** Proxy

---

#### getLayer

public

ModuleLayer

getLayer()

Returns the module layer that contains this module or

null

if
this module is not in a module layer.

A module layer contains named modules and therefore this method always
returns

null

when invoked on an unnamed module.

Dynamic modules

are
named modules that are generated at runtime. A dynamic module may or may
not be in a module layer.

Dynamic modules

are
named modules that are generated at runtime. A dynamic module may or may
not be in a module layer.

canRead

```java
public boolean canRead​(
Module
other)
```

Indicates if this module reads the given module. This method returns

true

if invoked to test if this module reads itself. It also
returns

true

if invoked on an unnamed module (as unnamed
modules read all modules).

**Parameters:** other

- The other module
**Returns:** true

if this module reads

other
**See Also:** addReads(Module)

---

#### canRead

public boolean canRead​(

Module

other)

Indicates if this module reads the given module. This method returns

true

if invoked to test if this module reads itself. It also
returns

true

if invoked on an unnamed module (as unnamed
modules read all modules).

addReads

```java
public
Module
addReads​(
Module
other)
```

If the caller's module is this module then update this module to read
the given module.

This method is a no-op if

other

is this module (all modules read
themselves), this module is an unnamed module (as unnamed modules read
all modules), or this module already reads

other

.

**Implementation Note:** Read edges

added by this method are

weak

and
do not prevent

other

from being GC'ed when this module is
strongly reachable.
**Parameters:** other

- The other module
**Returns:** this module
**Throws:** IllegalCallerException

- If this is a named module and the caller's module is not this
module
**See Also:** canRead(java.lang.Module)

---

#### addReads

public

Module

addReads​(

Module

other)

If the caller's module is this module then update this module to read
the given module.

This method is a no-op if

other

is this module (all modules read
themselves), this module is an unnamed module (as unnamed modules read
all modules), or this module already reads

other

.

isExported

```java
public boolean isExported​(
String
pn,

Module
other)
```

Returns

true

if this module exports the given package to at
least the given module.

This method returns

true

if invoked to test if a package in
this module is exported to itself. It always returns

true

when
invoked on an unnamed module. A package that is

open

to
the given module is considered exported to that module at run-time and
so this method returns

true

if the package is open to the given
module.

This method does not check if the given module reads this module.

**Parameters:** pn

- The package name
**Parameters:** other

- The other module
**Returns:** true

if this module exports the package to at least the
given module
**See Also:** ModuleDescriptor.exports()

,

addExports(String,Module)

---

#### isExported

public boolean isExported​(

String

pn,

Module

other)

Returns

true

if this module exports the given package to at
least the given module.

This method returns

true

if invoked to test if a package in
this module is exported to itself. It always returns

true

when
invoked on an unnamed module. A package that is

open

to
the given module is considered exported to that module at run-time and
so this method returns

true

if the package is open to the given
module.

This method does not check if the given module reads this module.

This method returns

true

if invoked to test if a package in
this module is exported to itself. It always returns

true

when
invoked on an unnamed module. A package that is

open

to
the given module is considered exported to that module at run-time and
so this method returns

true

if the package is open to the given
module.

This method does not check if the given module reads this module.

isOpen

```java
public boolean isOpen​(
String
pn,

Module
other)
```

Returns

true

if this module has

opened

a package to at
least the given module.

This method returns

true

if invoked to test if a package in
this module is open to itself. It returns

true

when invoked on an

open

module with a package in the module.
It always returns

true

when invoked on an unnamed module.

This method does not check if the given module reads this module.

**Parameters:** pn

- The package name
**Parameters:** other

- The other module
**Returns:** true

if this module has

opened

the package
to at least the given module
**See Also:** ModuleDescriptor.opens()

,

addOpens(String,Module)

,

AccessibleObject.setAccessible(boolean)

,

MethodHandles.privateLookupIn(java.lang.Class<?>, java.lang.invoke.MethodHandles.Lookup)

---

#### isOpen

public boolean isOpen​(

String

pn,

Module

other)

Returns

true

if this module has

opened

a package to at
least the given module.

This method returns

true

if invoked to test if a package in
this module is open to itself. It returns

true

when invoked on an

open

module with a package in the module.
It always returns

true

when invoked on an unnamed module.

This method does not check if the given module reads this module.

This method returns

true

if invoked to test if a package in
this module is open to itself. It returns

true

when invoked on an

open

module with a package in the module.
It always returns

true

when invoked on an unnamed module.

This method does not check if the given module reads this module.

isExported

```java
public boolean isExported​(
String
pn)
```

Returns

true

if this module exports the given package
unconditionally.

This method always returns

true

when invoked on an unnamed
module. A package that is

opened

unconditionally
is considered exported unconditionally at run-time and so this method
returns

true

if the package is opened unconditionally.

This method does not check if the given module reads this module.

**Parameters:** pn

- The package name
**Returns:** true

if this module exports the package unconditionally
**See Also:** ModuleDescriptor.exports()

---

#### isExported

public boolean isExported​(

String

pn)

Returns

true

if this module exports the given package
unconditionally.

This method always returns

true

when invoked on an unnamed
module. A package that is

opened

unconditionally
is considered exported unconditionally at run-time and so this method
returns

true

if the package is opened unconditionally.

This method does not check if the given module reads this module.

This method always returns

true

when invoked on an unnamed
module. A package that is

opened

unconditionally
is considered exported unconditionally at run-time and so this method
returns

true

if the package is opened unconditionally.

This method does not check if the given module reads this module.

isOpen

```java
public boolean isOpen​(
String
pn)
```

Returns

true

if this module has

opened

a package
unconditionally.

This method always returns

true

when invoked on an unnamed
module. Additionally, it always returns

true

when invoked on an

open

module with a package in the
module.

This method does not check if the given module reads this module.

**Parameters:** pn

- The package name
**Returns:** true

if this module has

opened

the package
unconditionally
**See Also:** ModuleDescriptor.opens()

---

#### isOpen

public boolean isOpen​(

String

pn)

Returns

true

if this module has

opened

a package
unconditionally.

This method always returns

true

when invoked on an unnamed
module. Additionally, it always returns

true

when invoked on an

open

module with a package in the
module.

This method does not check if the given module reads this module.

This method always returns

true

when invoked on an unnamed
module. Additionally, it always returns

true

when invoked on an

open

module with a package in the
module.

This method does not check if the given module reads this module.

addExports

```java
public
Module
addExports​(
String
pn,

Module
other)
```

If the caller's module is this module then update this module to export
the given package to the given module.

This method has no effect if the package is already exported (or

open

) to the given module.

**API Note:** As specified in section 5.4.3 of the

The Java™
Virtual Machine Specification

, if an attempt to resolve a
symbolic reference fails because of a linkage error, then subsequent
attempts to resolve the reference always fail with the same error that
was thrown as a result of the initial resolution attempt.
**Parameters:** pn

- The package name
**Parameters:** other

- The module
**Returns:** this module
**Throws:** IllegalArgumentException

- If

pn

is

null

, or this is a named module and the
package

pn

is not a package in this module
**Throws:** IllegalCallerException

- If this is a named module and the caller's module is not this
module
**See Also:** isExported(String,Module)
**See The Java™ Virtual Machine Specification :** 5.4.3 Resolution

---

#### addExports

public

Module

addExports​(

String

pn,

Module

other)

If the caller's module is this module then update this module to export
the given package to the given module.

This method has no effect if the package is already exported (or

open

) to the given module.

This method has no effect if the package is already exported (or

open

) to the given module.

addOpens

```java
public
Module
addOpens​(
String
pn,

Module
other)
```

If this module has

opened

a package to at least the caller
module then update this module to open the package to the given module.
Opening a package with this method allows all types in the package,
and all their members, not just public types and their public members,
to be reflected on by the given module when using APIs that support
private access or a way to bypass or suppress default Java language
access control checks.

This method has no effect if the package is already

open

to the given module.

**API Note:** This method can be used for cases where a

consumer
module

uses a qualified opens to open a package to an

API
module

but where the reflective access to the members of classes in
the consumer module is delegated to code in another module. Code in the
API module can use this method to open the package in the consumer module
to the other module.
**Parameters:** pn

- The package name
**Parameters:** other

- The module
**Returns:** this module
**Throws:** IllegalArgumentException

- If

pn

is

null

, or this is a named module and the
package

pn

is not a package in this module
**Throws:** IllegalCallerException

- If this is a named module and this module has not opened the
package to at least the caller's module
**See Also:** isOpen(String,Module)

,

AccessibleObject.setAccessible(boolean)

,

MethodHandles.privateLookupIn(java.lang.Class<?>, java.lang.invoke.MethodHandles.Lookup)

---

#### addOpens

public

Module

addOpens​(

String

pn,

Module

other)

If this module has

opened

a package to at least the caller
module then update this module to open the package to the given module.
Opening a package with this method allows all types in the package,
and all their members, not just public types and their public members,
to be reflected on by the given module when using APIs that support
private access or a way to bypass or suppress default Java language
access control checks.

This method has no effect if the package is already

open

to the given module.

This method has no effect if the package is already

open

to the given module.

addUses

```java
public
Module
addUses​(
Class
<?> service)
```

If the caller's module is this module then update this module to add a
service dependence on the given service type. This method is intended
for use by frameworks that invoke

ServiceLoader

on behalf of other modules or where the framework is
passed a reference to the service type by other code. This method is
a no-op when invoked on an unnamed module or an automatic module.

This method does not cause

resolveAndBind

to be re-run.

**Parameters:** service

- The service type
**Returns:** this module
**Throws:** IllegalCallerException

- If this is a named module and the caller's module is not this
module
**See Also:** canUse(Class)

,

ModuleDescriptor.uses()

---

#### addUses

public

Module

addUses​(

Class

<?> service)

If the caller's module is this module then update this module to add a
service dependence on the given service type. This method is intended
for use by frameworks that invoke

ServiceLoader

on behalf of other modules or where the framework is
passed a reference to the service type by other code. This method is
a no-op when invoked on an unnamed module or an automatic module.

This method does not cause

resolveAndBind

to be re-run.

This method does not cause

resolveAndBind

to be re-run.

canUse

```java
public boolean canUse​(
Class
<?> service)
```

Indicates if this module has a service dependence on the given service
type. This method always returns

true

when invoked on an unnamed
module or an automatic module.

**Parameters:** service

- The service type
**Returns:** true

if this module uses service type

st
**See Also:** addUses(Class)

---

#### canUse

public boolean canUse​(

Class

<?> service)

Indicates if this module has a service dependence on the given service
type. This method always returns

true

when invoked on an unnamed
module or an automatic module.

getPackages

```java
public
Set
<
String
> getPackages()
```

Returns the set of package names for the packages in this module.

For named modules, the returned set contains an element for each
package in the module.

For unnamed modules, this method is the equivalent to invoking the

getDefinedPackages

method of
this module's class loader and returning the set of package names.

**Returns:** the set of the package names of the packages in this module

---

#### getPackages

public

Set

<

String

> getPackages()

Returns the set of package names for the packages in this module.

For named modules, the returned set contains an element for each
package in the module.

For unnamed modules, this method is the equivalent to invoking the

getDefinedPackages

method of
this module's class loader and returning the set of package names.

For named modules, the returned set contains an element for each
package in the module.

For unnamed modules, this method is the equivalent to invoking the

getDefinedPackages

method of
this module's class loader and returning the set of package names.

getAnnotation

```java
public <T extends
Annotation
> T getAnnotation​(
Class
<T> annotationClass)
```

Returns this element's annotation for the specified type if
such an annotation is

present

, else null.
This method returns

null

when invoked on an unnamed module.

**Specified by:** getAnnotation

in interface

AnnotatedElement
**Type Parameters:** T

- the type of the annotation to query for and return if present
**Parameters:** annotationClass

- the Class object corresponding to the
annotation type
**Returns:** this element's annotation for the specified annotation type if
present on this element, else null

---

#### getAnnotation

public <T extends

Annotation

> T getAnnotation​(

Class

<T> annotationClass)

Returns this element's annotation for the specified type if
such an annotation is

present

, else null.
This method returns

null

when invoked on an unnamed module.

getAnnotations

```java
public
Annotation
[] getAnnotations()
```

Returns annotations that are

present

on this element.

If there are no annotations

present

on this element, the return
value is an array of length 0.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.
This method returns an empty array when invoked on an unnamed module.

**Specified by:** getAnnotations

in interface

AnnotatedElement
**Returns:** annotations present on this element

---

#### getAnnotations

public

Annotation

[] getAnnotations()

Returns annotations that are

present

on this element.

If there are no annotations

present

on this element, the return
value is an array of length 0.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.
This method returns an empty array when invoked on an unnamed module.

getDeclaredAnnotations

```java
public
Annotation
[] getDeclaredAnnotations()
```

Returns annotations that are

directly present

on this element.
This method ignores inherited annotations.

If there are no annotations

directly present

on this element,
the return value is an array of length 0.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.
This method returns an empty array when invoked on an unnamed module.

**Specified by:** getDeclaredAnnotations

in interface

AnnotatedElement
**Returns:** annotations directly present on this element

---

#### getDeclaredAnnotations

public

Annotation

[] getDeclaredAnnotations()

Returns annotations that are

directly present

on this element.
This method ignores inherited annotations.

If there are no annotations

directly present

on this element,
the return value is an array of length 0.

The caller of this method is free to modify the returned array; it will
have no effect on the arrays returned to other callers.
This method returns an empty array when invoked on an unnamed module.

getResourceAsStream

```java
public
InputStream
getResourceAsStream​(
String
name)
throws
IOException
```

Returns an input stream for reading a resource in this module.
The

name

parameter is a

'/'

-separated path name that
identifies the resource. As with

Class.getResourceAsStream

, this method delegates to the module's class
loader

findResource(String,String)

method, invoking it with the module name
(or

null

when the module is unnamed) and the name of the
resource. If the resource name has a leading slash then it is dropped
before delegation.

A resource in a named module may be

encapsulated

so that
it cannot be located by code in other modules. Whether a resource can be
located or not is determined as follows:

- If the resource name ends with "

.class

" then it is not
encapsulated.
- A

package name

is derived from the resource name. If
the package name is a

package

in the
module then the resource can only be located by the caller of this
method when the package is

open

to at least the caller's module. If the resource is not in a
package in the module then the resource is not encapsulated.

In the above, the

package name

for a resource is derived
from the subsequence of characters that precedes the last

'/'

in
the name and then replacing each

'/'

character in the subsequence
with

'.'

. A leading slash is ignored when deriving the package
name. As an example, the package name derived for a resource named
"

a/b/c/foo.properties

" is "

a.b.c

". A resource name
with the name "

META-INF/MANIFEST.MF

" is never encapsulated
because "

META-INF

" is not a legal package name.

This method returns

null

if the resource is not in this
module, the resource is encapsulated and cannot be located by the caller,
or access to the resource is denied by the security manager.

**Parameters:** name

- The resource name
**Returns:** An input stream for reading the resource or

null
**Throws:** IOException

- If an I/O error occurs
**See Also:** Class.getResourceAsStream(String)

---

#### getResourceAsStream

public

InputStream

getResourceAsStream​(

String

name)
throws

IOException

Returns an input stream for reading a resource in this module.
The

name

parameter is a

'/'

-separated path name that
identifies the resource. As with

Class.getResourceAsStream

, this method delegates to the module's class
loader

findResource(String,String)

method, invoking it with the module name
(or

null

when the module is unnamed) and the name of the
resource. If the resource name has a leading slash then it is dropped
before delegation.

A resource in a named module may be

encapsulated

so that
it cannot be located by code in other modules. Whether a resource can be
located or not is determined as follows:

- If the resource name ends with "

.class

" then it is not
encapsulated.
- A

package name

is derived from the resource name. If
the package name is a

package

in the
module then the resource can only be located by the caller of this
method when the package is

open

to at least the caller's module. If the resource is not in a
package in the module then the resource is not encapsulated.

In the above, the

package name

for a resource is derived
from the subsequence of characters that precedes the last

'/'

in
the name and then replacing each

'/'

character in the subsequence
with

'.'

. A leading slash is ignored when deriving the package
name. As an example, the package name derived for a resource named
"

a/b/c/foo.properties

" is "

a.b.c

". A resource name
with the name "

META-INF/MANIFEST.MF

" is never encapsulated
because "

META-INF

" is not a legal package name.

This method returns

null

if the resource is not in this
module, the resource is encapsulated and cannot be located by the caller,
or access to the resource is denied by the security manager.

A resource in a named module may be

encapsulated

so that
it cannot be located by code in other modules. Whether a resource can be
located or not is determined as follows:

If the resource name ends with "

.class

" then it is not
encapsulated.

A

package name

is derived from the resource name. If
the package name is a

package

in the
module then the resource can only be located by the caller of this
method when the package is

open

to at least the caller's module. If the resource is not in a
package in the module then the resource is not encapsulated.

In the above, the

package name

for a resource is derived
from the subsequence of characters that precedes the last

'/'

in
the name and then replacing each

'/'

character in the subsequence
with

'.'

. A leading slash is ignored when deriving the package
name. As an example, the package name derived for a resource named
"

a/b/c/foo.properties

" is "

a.b.c

". A resource name
with the name "

META-INF/MANIFEST.MF

" is never encapsulated
because "

META-INF

" is not a legal package name.

This method returns

null

if the resource is not in this
module, the resource is encapsulated and cannot be located by the caller,
or access to the resource is denied by the security manager.

toString

```java
public
String
toString()
```

Returns the string representation of this module. For a named module,
the representation is the string

"module"

, followed by a space,
and then the module name. For an unnamed module, the representation is
the string

"unnamed module"

, followed by a space, and then an
implementation specific string that identifies the unnamed module.

**Overrides:** toString

in class

Object
**Returns:** The string representation of this module

---

#### toString

public

String

toString()

Returns the string representation of this module. For a named module,
the representation is the string

"module"

, followed by a space,
and then the module name. For an unnamed module, the representation is
the string

"unnamed module"

, followed by a space, and then an
implementation specific string that identifies the unnamed module.

---

