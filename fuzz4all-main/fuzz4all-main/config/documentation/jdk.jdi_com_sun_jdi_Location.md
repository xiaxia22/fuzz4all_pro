# Interface Location

**Source:** `jdk.jdi\com\sun\jdi\Location.html`

### Class Description

```java
public interface
Location

extends
Mirror
,
Comparable
<
Location
>
```

A point within the executing code of the target VM.
Locations are used to identify the current position of
a suspended thread (analogous to an instruction pointer or
program counter register in native programs). They are also used
to identify the position at which to set a breakpoint.

The availability of a line number for a location will
depend on the level of debugging information available from the
target VM.

Several mirror interfaces have locations. Each such mirror
extends a

Locatable

interface.

Strata

The source information for a Location is dependent on the

stratum

which is used. A stratum is a source code
level within a sequence of translations. For example,
say the baz program is written in the programming language
"Foo" then translated to the language "Bar" and finally
translated into the Java programming language. The
Java programming language stratum is named

"Java"

, let's say the other strata are named
"Foo" and "Bar". A given location (as viewed by the

sourceName()

and

lineNumber()

methods)
might be at line 14 of "baz.foo" in the

"Foo"

stratum, line 23 of "baz.bar" in the

"Bar"

stratum and line 71 of the

"Java"

stratum.
Note that while the Java programming language may have
only one source file for a reference type, this restriction
does not apply to other strata - thus each Location should
be consulted to determine its source path.
Queries which do not specify a stratum
(

sourceName()

,

sourcePath()

and

lineNumber()

) use the VM's default stratum
(

VirtualMachine.getDefaultStratum()

).
If the specified stratum (whether explicitly specified
by a method parameter or implicitly as the VM's default)
is

null

or is not available in the declaring
type, the declaring type's default stratum is used
(

declaringType()

.

defaultStratum()

). Note that in the normal case, of code
that originates as Java programming language source, there
will be only one stratum (

"Java"

) and it will be
returned as the default. To determine the available strata
use

ReferenceType.availableStrata()

.

**All Superinterfaces:** Comparable

<

Location

>

,

Mirror

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ReferenceType
declaringType()

Gets the type to which this Location belongs. Normally
the declaring type is a

ClassType

, but executable
locations also may exist within the static initializer of an

InterfaceType

.

**Returns:**
- the

ReferenceType

containing this Location.

---

#### Method
method()

Gets the method containing this Location.

**Returns:**
- the location's

Method

.

---

#### long codeIndex()

Gets the code position within this location's method.

**Returns:**
- the long representing the position within the method
or -1 if location is within a native method.

---

#### String
sourceName()
throws
AbsentInformationException

Gets an identifing name for the source corresponding to
this location.

This method is equivalent to

sourceName(vm.getDefaultStratum())

-
see

sourceName(String)

for more information.

**Returns:**
- a string specifying the source

**Throws:**
- AbsentInformationException

- if the source name is not
known

---

#### String
sourceName​(
String
stratum)
throws
AbsentInformationException

Gets an identifing name for the source corresponding to
this location. Interpretation of this string is the
responsibility of the source repository mechanism.

Returned name is for the specified

stratum

(see the

class comment

for a
description of strata).

The returned string is the unqualified name of the source
file for this Location. For example,

java.lang.Thread

would return

"Thread.java"

.

**Parameters:**
- stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.

**Returns:**
- a string specifying the source

**Throws:**
- AbsentInformationException

- if the source name is not
known

**Since:**
- 1.4

---

#### String
sourcePath()
throws
AbsentInformationException

Gets the path to the source corresponding to this
location.

This method is equivalent to

sourcePath(vm.getDefaultStratum())

-
see

sourcePath(String)

for more information.

**Returns:**
- a string specifying the source

**Throws:**
- AbsentInformationException

- if the source name is not
known

---

#### String
sourcePath​(
String
stratum)
throws
AbsentInformationException

Gets the path to the source corresponding to this
location. Interpretation of this string is the
responsibility of the source repository mechanism.

Returned path is for the specified

stratum

(see the

class comment

for a
description of strata).

In the reference implementation, for strata which
do not explicitly specify source path (the Java
programming language stratum never does), the returned
string is the package name of

declaringType()

converted to a platform dependent path followed by the
unqualified name of the source file for this Location
(

sourceName(stratum)

).
For example, on a
Windows platform,

java.lang.Thread

would return

"java\lang\Thread.java"

.

**Parameters:**
- stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.

**Returns:**
- a string specifying the source

**Throws:**
- AbsentInformationException

- if the source name is not
known

**Since:**
- 1.4

---

#### int lineNumber()

Gets the line number of this Location.

This method is equivalent to

lineNumber(vm.getDefaultStratum())

-
see

lineNumber(String)

for more information.

**Returns:**
- an int specifying the line in the source, returns
-1 if the information is not available; specifically, always
returns -1 for native methods.

---

#### int lineNumber​(
String
stratum)

The line number of this Location. The line number is
relative to the source specified by

sourceName(stratum)

.

Returned line number is for the specified

stratum

(see the

class comment

for a
description of strata).

**Parameters:**
- stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.

**Returns:**
- an int specifying the line in the source, returns
-1 if the information is not available; specifically, always
returns -1 for native methods.

**Since:**
- 1.4

---

#### boolean equals​(
Object
obj)

Compares the specified Object with this Location for equality.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true if the Object is a Location and if it refers to
the same point in the same VM as this Location.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this Location.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the integer hash code

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Interface Location

**All Superinterfaces:** Comparable

<

Location

>

,

Mirror

```java
public interface
Location

extends
Mirror
,
Comparable
<
Location
>
```

A point within the executing code of the target VM.
Locations are used to identify the current position of
a suspended thread (analogous to an instruction pointer or
program counter register in native programs). They are also used
to identify the position at which to set a breakpoint.

The availability of a line number for a location will
depend on the level of debugging information available from the
target VM.

Several mirror interfaces have locations. Each such mirror
extends a

Locatable

interface.

Strata

The source information for a Location is dependent on the

stratum

which is used. A stratum is a source code
level within a sequence of translations. For example,
say the baz program is written in the programming language
"Foo" then translated to the language "Bar" and finally
translated into the Java programming language. The
Java programming language stratum is named

"Java"

, let's say the other strata are named
"Foo" and "Bar". A given location (as viewed by the

sourceName()

and

lineNumber()

methods)
might be at line 14 of "baz.foo" in the

"Foo"

stratum, line 23 of "baz.bar" in the

"Bar"

stratum and line 71 of the

"Java"

stratum.
Note that while the Java programming language may have
only one source file for a reference type, this restriction
does not apply to other strata - thus each Location should
be consulted to determine its source path.
Queries which do not specify a stratum
(

sourceName()

,

sourcePath()

and

lineNumber()

) use the VM's default stratum
(

VirtualMachine.getDefaultStratum()

).
If the specified stratum (whether explicitly specified
by a method parameter or implicitly as the VM's default)
is

null

or is not available in the declaring
type, the declaring type's default stratum is used
(

declaringType()

.

defaultStratum()

). Note that in the normal case, of code
that originates as Java programming language source, there
will be only one stratum (

"Java"

) and it will be
returned as the default. To determine the available strata
use

ReferenceType.availableStrata()

.

**Since:** 1.3
**See Also:** EventRequestManager

,

StackFrame

,

BreakpointEvent

,

ExceptionEvent

,

Locatable

public interface

Location

extends

Mirror

,

Comparable

<

Location

>

A point within the executing code of the target VM.
Locations are used to identify the current position of
a suspended thread (analogous to an instruction pointer or
program counter register in native programs). They are also used
to identify the position at which to set a breakpoint.

The availability of a line number for a location will
depend on the level of debugging information available from the
target VM.

Several mirror interfaces have locations. Each such mirror
extends a

Locatable

interface.

Strata

The source information for a Location is dependent on the

stratum

which is used. A stratum is a source code
level within a sequence of translations. For example,
say the baz program is written in the programming language
"Foo" then translated to the language "Bar" and finally
translated into the Java programming language. The
Java programming language stratum is named

"Java"

, let's say the other strata are named
"Foo" and "Bar". A given location (as viewed by the

sourceName()

and

lineNumber()

methods)
might be at line 14 of "baz.foo" in the

"Foo"

stratum, line 23 of "baz.bar" in the

"Bar"

stratum and line 71 of the

"Java"

stratum.
Note that while the Java programming language may have
only one source file for a reference type, this restriction
does not apply to other strata - thus each Location should
be consulted to determine its source path.
Queries which do not specify a stratum
(

sourceName()

,

sourcePath()

and

lineNumber()

) use the VM's default stratum
(

VirtualMachine.getDefaultStratum()

).
If the specified stratum (whether explicitly specified
by a method parameter or implicitly as the VM's default)
is

null

or is not available in the declaring
type, the declaring type's default stratum is used
(

declaringType()

.

defaultStratum()

). Note that in the normal case, of code
that originates as Java programming language source, there
will be only one stratum (

"Java"

) and it will be
returned as the default. To determine the available strata
use

ReferenceType.availableStrata()

.

The availability of a line number for a location will
depend on the level of debugging information available from the
target VM.

Several mirror interfaces have locations. Each such mirror
extends a

Locatable

interface.

Strata

The source information for a Location is dependent on the

stratum

which is used. A stratum is a source code
level within a sequence of translations. For example,
say the baz program is written in the programming language
"Foo" then translated to the language "Bar" and finally
translated into the Java programming language. The
Java programming language stratum is named

"Java"

, let's say the other strata are named
"Foo" and "Bar". A given location (as viewed by the

sourceName()

and

lineNumber()

methods)
might be at line 14 of "baz.foo" in the

"Foo"

stratum, line 23 of "baz.bar" in the

"Bar"

stratum and line 71 of the

"Java"

stratum.
Note that while the Java programming language may have
only one source file for a reference type, this restriction
does not apply to other strata - thus each Location should
be consulted to determine its source path.
Queries which do not specify a stratum
(

sourceName()

,

sourcePath()

and

lineNumber()

) use the VM's default stratum
(

VirtualMachine.getDefaultStratum()

).
If the specified stratum (whether explicitly specified
by a method parameter or implicitly as the VM's default)
is

null

or is not available in the declaring
type, the declaring type's default stratum is used
(

declaringType()

.

defaultStratum()

). Note that in the normal case, of code
that originates as Java programming language source, there
will be only one stratum (

"Java"

) and it will be
returned as the default. To determine the available strata
use

ReferenceType.availableStrata()

.

Several mirror interfaces have locations. Each such mirror
extends a

Locatable

interface.

Strata

The source information for a Location is dependent on the

stratum

which is used. A stratum is a source code
level within a sequence of translations. For example,
say the baz program is written in the programming language
"Foo" then translated to the language "Bar" and finally
translated into the Java programming language. The
Java programming language stratum is named

"Java"

, let's say the other strata are named
"Foo" and "Bar". A given location (as viewed by the

sourceName()

and

lineNumber()

methods)
might be at line 14 of "baz.foo" in the

"Foo"

stratum, line 23 of "baz.bar" in the

"Bar"

stratum and line 71 of the

"Java"

stratum.
Note that while the Java programming language may have
only one source file for a reference type, this restriction
does not apply to other strata - thus each Location should
be consulted to determine its source path.
Queries which do not specify a stratum
(

sourceName()

,

sourcePath()

and

lineNumber()

) use the VM's default stratum
(

VirtualMachine.getDefaultStratum()

).
If the specified stratum (whether explicitly specified
by a method parameter or implicitly as the VM's default)
is

null

or is not available in the declaring
type, the declaring type's default stratum is used
(

declaringType()

.

defaultStratum()

). Note that in the normal case, of code
that originates as Java programming language source, there
will be only one stratum (

"Java"

) and it will be
returned as the default. To determine the available strata
use

ReferenceType.availableStrata()

.

Strata

The source information for a Location is dependent on the

stratum

which is used. A stratum is a source code
level within a sequence of translations. For example,
say the baz program is written in the programming language
"Foo" then translated to the language "Bar" and finally
translated into the Java programming language. The
Java programming language stratum is named

"Java"

, let's say the other strata are named
"Foo" and "Bar". A given location (as viewed by the

sourceName()

and

lineNumber()

methods)
might be at line 14 of "baz.foo" in the

"Foo"

stratum, line 23 of "baz.bar" in the

"Bar"

stratum and line 71 of the

"Java"

stratum.
Note that while the Java programming language may have
only one source file for a reference type, this restriction
does not apply to other strata - thus each Location should
be consulted to determine its source path.
Queries which do not specify a stratum
(

sourceName()

,

sourcePath()

and

lineNumber()

) use the VM's default stratum
(

VirtualMachine.getDefaultStratum()

).
If the specified stratum (whether explicitly specified
by a method parameter or implicitly as the VM's default)
is

null

or is not available in the declaring
type, the declaring type's default stratum is used
(

declaringType()

.

defaultStratum()

). Note that in the normal case, of code
that originates as Java programming language source, there
will be only one stratum (

"Java"

) and it will be
returned as the default. To determine the available strata
use

ReferenceType.availableStrata()

.

The source information for a Location is dependent on the

stratum

which is used. A stratum is a source code
level within a sequence of translations. For example,
say the baz program is written in the programming language
"Foo" then translated to the language "Bar" and finally
translated into the Java programming language. The
Java programming language stratum is named

"Java"

, let's say the other strata are named
"Foo" and "Bar". A given location (as viewed by the

sourceName()

and

lineNumber()

methods)
might be at line 14 of "baz.foo" in the

"Foo"

stratum, line 23 of "baz.bar" in the

"Bar"

stratum and line 71 of the

"Java"

stratum.
Note that while the Java programming language may have
only one source file for a reference type, this restriction
does not apply to other strata - thus each Location should
be consulted to determine its source path.
Queries which do not specify a stratum
(

sourceName()

,

sourcePath()

and

lineNumber()

) use the VM's default stratum
(

VirtualMachine.getDefaultStratum()

).
If the specified stratum (whether explicitly specified
by a method parameter or implicitly as the VM's default)
is

null

or is not available in the declaring
type, the declaring type's default stratum is used
(

declaringType()

.

defaultStratum()

). Note that in the normal case, of code
that originates as Java programming language source, there
will be only one stratum (

"Java"

) and it will be
returned as the default. To determine the available strata
use

ReferenceType.availableStrata()

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

long

codeIndex

()

Gets the code position within this location's method.

ReferenceType

declaringType

()

Gets the type to which this Location belongs.

boolean

equals

​(

Object

obj)

Compares the specified Object with this Location for equality.

int

hashCode

()

Returns the hash code value for this Location.

int

lineNumber

()

Gets the line number of this Location.

int

lineNumber

​(

String

stratum)

The line number of this Location.

Method

method

()

Gets the method containing this Location.

String

sourceName

()

Gets an identifing name for the source corresponding to
this location.

String

sourceName

​(

String

stratum)

Gets an identifing name for the source corresponding to
this location.

String

sourcePath

()

Gets the path to the source corresponding to this
location.

String

sourcePath

​(

String

stratum)

Gets the path to the source corresponding to this
location.

- Methods declared in interface java.lang.

Comparable

compareTo

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

long

codeIndex

()

Gets the code position within this location's method.

ReferenceType

declaringType

()

Gets the type to which this Location belongs.

boolean

equals

​(

Object

obj)

Compares the specified Object with this Location for equality.

int

hashCode

()

Returns the hash code value for this Location.

int

lineNumber

()

Gets the line number of this Location.

int

lineNumber

​(

String

stratum)

The line number of this Location.

Method

method

()

Gets the method containing this Location.

String

sourceName

()

Gets an identifing name for the source corresponding to
this location.

String

sourceName

​(

String

stratum)

Gets an identifing name for the source corresponding to
this location.

String

sourcePath

()

Gets the path to the source corresponding to this
location.

String

sourcePath

​(

String

stratum)

Gets the path to the source corresponding to this
location.

- Methods declared in interface java.lang.

Comparable

compareTo

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Method Summary

Gets the code position within this location's method.

Gets the type to which this Location belongs.

Compares the specified Object with this Location for equality.

Returns the hash code value for this Location.

Gets the line number of this Location.

The line number of this Location.

Gets the method containing this Location.

Gets an identifing name for the source corresponding to
this location.

Gets the path to the source corresponding to this
location.

Methods declared in interface java.lang.

Comparable

compareTo

---

#### Methods declared in interface java.lang. Comparable

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

============ METHOD DETAIL ==========

- Method Detail

- declaringType

```java
ReferenceType
declaringType()
```

Gets the type to which this Location belongs. Normally
the declaring type is a

ClassType

, but executable
locations also may exist within the static initializer of an

InterfaceType

.

**Returns:** the

ReferenceType

containing this Location.

- method

```java
Method
method()
```

Gets the method containing this Location.

**Returns:** the location's

Method

.

- codeIndex

```java
long codeIndex()
```

Gets the code position within this location's method.

**Returns:** the long representing the position within the method
or -1 if location is within a native method.

- sourceName

```java
String
sourceName()
throws
AbsentInformationException
```

Gets an identifing name for the source corresponding to
this location.

This method is equivalent to

sourceName(vm.getDefaultStratum())

-
see

sourceName(String)

for more information.

**Returns:** a string specifying the source
**Throws:** AbsentInformationException

- if the source name is not
known

- sourceName

```java
String
sourceName​(
String
stratum)
throws
AbsentInformationException
```

Gets an identifing name for the source corresponding to
this location. Interpretation of this string is the
responsibility of the source repository mechanism.

Returned name is for the specified

stratum

(see the

class comment

for a
description of strata).

The returned string is the unqualified name of the source
file for this Location. For example,

java.lang.Thread

would return

"Thread.java"

.

**Parameters:** stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.
**Returns:** a string specifying the source
**Throws:** AbsentInformationException

- if the source name is not
known
**Since:** 1.4

- sourcePath

```java
String
sourcePath()
throws
AbsentInformationException
```

Gets the path to the source corresponding to this
location.

This method is equivalent to

sourcePath(vm.getDefaultStratum())

-
see

sourcePath(String)

for more information.

**Returns:** a string specifying the source
**Throws:** AbsentInformationException

- if the source name is not
known

- sourcePath

```java
String
sourcePath​(
String
stratum)
throws
AbsentInformationException
```

Gets the path to the source corresponding to this
location. Interpretation of this string is the
responsibility of the source repository mechanism.

Returned path is for the specified

stratum

(see the

class comment

for a
description of strata).

In the reference implementation, for strata which
do not explicitly specify source path (the Java
programming language stratum never does), the returned
string is the package name of

declaringType()

converted to a platform dependent path followed by the
unqualified name of the source file for this Location
(

sourceName(stratum)

).
For example, on a
Windows platform,

java.lang.Thread

would return

"java\lang\Thread.java"

.

**Parameters:** stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.
**Returns:** a string specifying the source
**Throws:** AbsentInformationException

- if the source name is not
known
**Since:** 1.4

- lineNumber

```java
int lineNumber()
```

Gets the line number of this Location.

This method is equivalent to

lineNumber(vm.getDefaultStratum())

-
see

lineNumber(String)

for more information.

**Returns:** an int specifying the line in the source, returns
-1 if the information is not available; specifically, always
returns -1 for native methods.

- lineNumber

```java
int lineNumber​(
String
stratum)
```

The line number of this Location. The line number is
relative to the source specified by

sourceName(stratum)

.

Returned line number is for the specified

stratum

(see the

class comment

for a
description of strata).

**Parameters:** stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.
**Returns:** an int specifying the line in the source, returns
-1 if the information is not available; specifically, always
returns -1 for native methods.
**Since:** 1.4

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this Location for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a Location and if it refers to
the same point in the same VM as this Location.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this Location.

**Overrides:** hashCode

in class

Object
**Returns:** the integer hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Method Detail

- declaringType

```java
ReferenceType
declaringType()
```

Gets the type to which this Location belongs. Normally
the declaring type is a

ClassType

, but executable
locations also may exist within the static initializer of an

InterfaceType

.

**Returns:** the

ReferenceType

containing this Location.

- method

```java
Method
method()
```

Gets the method containing this Location.

**Returns:** the location's

Method

.

- codeIndex

```java
long codeIndex()
```

Gets the code position within this location's method.

**Returns:** the long representing the position within the method
or -1 if location is within a native method.

- sourceName

```java
String
sourceName()
throws
AbsentInformationException
```

Gets an identifing name for the source corresponding to
this location.

This method is equivalent to

sourceName(vm.getDefaultStratum())

-
see

sourceName(String)

for more information.

**Returns:** a string specifying the source
**Throws:** AbsentInformationException

- if the source name is not
known

- sourceName

```java
String
sourceName​(
String
stratum)
throws
AbsentInformationException
```

Gets an identifing name for the source corresponding to
this location. Interpretation of this string is the
responsibility of the source repository mechanism.

Returned name is for the specified

stratum

(see the

class comment

for a
description of strata).

The returned string is the unqualified name of the source
file for this Location. For example,

java.lang.Thread

would return

"Thread.java"

.

**Parameters:** stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.
**Returns:** a string specifying the source
**Throws:** AbsentInformationException

- if the source name is not
known
**Since:** 1.4

- sourcePath

```java
String
sourcePath()
throws
AbsentInformationException
```

Gets the path to the source corresponding to this
location.

This method is equivalent to

sourcePath(vm.getDefaultStratum())

-
see

sourcePath(String)

for more information.

**Returns:** a string specifying the source
**Throws:** AbsentInformationException

- if the source name is not
known

- sourcePath

```java
String
sourcePath​(
String
stratum)
throws
AbsentInformationException
```

Gets the path to the source corresponding to this
location. Interpretation of this string is the
responsibility of the source repository mechanism.

Returned path is for the specified

stratum

(see the

class comment

for a
description of strata).

In the reference implementation, for strata which
do not explicitly specify source path (the Java
programming language stratum never does), the returned
string is the package name of

declaringType()

converted to a platform dependent path followed by the
unqualified name of the source file for this Location
(

sourceName(stratum)

).
For example, on a
Windows platform,

java.lang.Thread

would return

"java\lang\Thread.java"

.

**Parameters:** stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.
**Returns:** a string specifying the source
**Throws:** AbsentInformationException

- if the source name is not
known
**Since:** 1.4

- lineNumber

```java
int lineNumber()
```

Gets the line number of this Location.

This method is equivalent to

lineNumber(vm.getDefaultStratum())

-
see

lineNumber(String)

for more information.

**Returns:** an int specifying the line in the source, returns
-1 if the information is not available; specifically, always
returns -1 for native methods.

- lineNumber

```java
int lineNumber​(
String
stratum)
```

The line number of this Location. The line number is
relative to the source specified by

sourceName(stratum)

.

Returned line number is for the specified

stratum

(see the

class comment

for a
description of strata).

**Parameters:** stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.
**Returns:** an int specifying the line in the source, returns
-1 if the information is not available; specifically, always
returns -1 for native methods.
**Since:** 1.4

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this Location for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a Location and if it refers to
the same point in the same VM as this Location.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this Location.

**Overrides:** hashCode

in class

Object
**Returns:** the integer hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

declaringType

```java
ReferenceType
declaringType()
```

Gets the type to which this Location belongs. Normally
the declaring type is a

ClassType

, but executable
locations also may exist within the static initializer of an

InterfaceType

.

**Returns:** the

ReferenceType

containing this Location.

---

#### declaringType

ReferenceType

declaringType()

Gets the type to which this Location belongs. Normally
the declaring type is a

ClassType

, but executable
locations also may exist within the static initializer of an

InterfaceType

.

method

```java
Method
method()
```

Gets the method containing this Location.

**Returns:** the location's

Method

.

---

#### method

Method

method()

Gets the method containing this Location.

codeIndex

```java
long codeIndex()
```

Gets the code position within this location's method.

**Returns:** the long representing the position within the method
or -1 if location is within a native method.

---

#### codeIndex

long codeIndex()

Gets the code position within this location's method.

sourceName

```java
String
sourceName()
throws
AbsentInformationException
```

Gets an identifing name for the source corresponding to
this location.

This method is equivalent to

sourceName(vm.getDefaultStratum())

-
see

sourceName(String)

for more information.

**Returns:** a string specifying the source
**Throws:** AbsentInformationException

- if the source name is not
known

---

#### sourceName

String

sourceName()
throws

AbsentInformationException

Gets an identifing name for the source corresponding to
this location.

This method is equivalent to

sourceName(vm.getDefaultStratum())

-
see

sourceName(String)

for more information.

This method is equivalent to

sourceName(vm.getDefaultStratum())

-
see

sourceName(String)

for more information.

sourceName

```java
String
sourceName​(
String
stratum)
throws
AbsentInformationException
```

Gets an identifing name for the source corresponding to
this location. Interpretation of this string is the
responsibility of the source repository mechanism.

Returned name is for the specified

stratum

(see the

class comment

for a
description of strata).

The returned string is the unqualified name of the source
file for this Location. For example,

java.lang.Thread

would return

"Thread.java"

.

**Parameters:** stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.
**Returns:** a string specifying the source
**Throws:** AbsentInformationException

- if the source name is not
known
**Since:** 1.4

---

#### sourceName

String

sourceName​(

String

stratum)
throws

AbsentInformationException

Gets an identifing name for the source corresponding to
this location. Interpretation of this string is the
responsibility of the source repository mechanism.

Returned name is for the specified

stratum

(see the

class comment

for a
description of strata).

The returned string is the unqualified name of the source
file for this Location. For example,

java.lang.Thread

would return

"Thread.java"

.

Returned name is for the specified

stratum

(see the

class comment

for a
description of strata).

The returned string is the unqualified name of the source
file for this Location. For example,

java.lang.Thread

would return

"Thread.java"

.

The returned string is the unqualified name of the source
file for this Location. For example,

java.lang.Thread

would return

"Thread.java"

.

sourcePath

```java
String
sourcePath()
throws
AbsentInformationException
```

Gets the path to the source corresponding to this
location.

This method is equivalent to

sourcePath(vm.getDefaultStratum())

-
see

sourcePath(String)

for more information.

**Returns:** a string specifying the source
**Throws:** AbsentInformationException

- if the source name is not
known

---

#### sourcePath

String

sourcePath()
throws

AbsentInformationException

Gets the path to the source corresponding to this
location.

This method is equivalent to

sourcePath(vm.getDefaultStratum())

-
see

sourcePath(String)

for more information.

This method is equivalent to

sourcePath(vm.getDefaultStratum())

-
see

sourcePath(String)

for more information.

sourcePath

```java
String
sourcePath​(
String
stratum)
throws
AbsentInformationException
```

Gets the path to the source corresponding to this
location. Interpretation of this string is the
responsibility of the source repository mechanism.

Returned path is for the specified

stratum

(see the

class comment

for a
description of strata).

In the reference implementation, for strata which
do not explicitly specify source path (the Java
programming language stratum never does), the returned
string is the package name of

declaringType()

converted to a platform dependent path followed by the
unqualified name of the source file for this Location
(

sourceName(stratum)

).
For example, on a
Windows platform,

java.lang.Thread

would return

"java\lang\Thread.java"

.

**Parameters:** stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.
**Returns:** a string specifying the source
**Throws:** AbsentInformationException

- if the source name is not
known
**Since:** 1.4

---

#### sourcePath

String

sourcePath​(

String

stratum)
throws

AbsentInformationException

Gets the path to the source corresponding to this
location. Interpretation of this string is the
responsibility of the source repository mechanism.

Returned path is for the specified

stratum

(see the

class comment

for a
description of strata).

In the reference implementation, for strata which
do not explicitly specify source path (the Java
programming language stratum never does), the returned
string is the package name of

declaringType()

converted to a platform dependent path followed by the
unqualified name of the source file for this Location
(

sourceName(stratum)

).
For example, on a
Windows platform,

java.lang.Thread

would return

"java\lang\Thread.java"

.

Returned path is for the specified

stratum

(see the

class comment

for a
description of strata).

In the reference implementation, for strata which
do not explicitly specify source path (the Java
programming language stratum never does), the returned
string is the package name of

declaringType()

converted to a platform dependent path followed by the
unqualified name of the source file for this Location
(

sourceName(stratum)

).
For example, on a
Windows platform,

java.lang.Thread

would return

"java\lang\Thread.java"

.

In the reference implementation, for strata which
do not explicitly specify source path (the Java
programming language stratum never does), the returned
string is the package name of

declaringType()

converted to a platform dependent path followed by the
unqualified name of the source file for this Location
(

sourceName(stratum)

).
For example, on a
Windows platform,

java.lang.Thread

would return

"java\lang\Thread.java"

.

lineNumber

```java
int lineNumber()
```

Gets the line number of this Location.

This method is equivalent to

lineNumber(vm.getDefaultStratum())

-
see

lineNumber(String)

for more information.

**Returns:** an int specifying the line in the source, returns
-1 if the information is not available; specifically, always
returns -1 for native methods.

---

#### lineNumber

int lineNumber()

Gets the line number of this Location.

This method is equivalent to

lineNumber(vm.getDefaultStratum())

-
see

lineNumber(String)

for more information.

This method is equivalent to

lineNumber(vm.getDefaultStratum())

-
see

lineNumber(String)

for more information.

lineNumber

```java
int lineNumber​(
String
stratum)
```

The line number of this Location. The line number is
relative to the source specified by

sourceName(stratum)

.

Returned line number is for the specified

stratum

(see the

class comment

for a
description of strata).

**Parameters:** stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.
**Returns:** an int specifying the line in the source, returns
-1 if the information is not available; specifically, always
returns -1 for native methods.
**Since:** 1.4

---

#### lineNumber

int lineNumber​(

String

stratum)

The line number of this Location. The line number is
relative to the source specified by

sourceName(stratum)

.

Returned line number is for the specified

stratum

(see the

class comment

for a
description of strata).

Returned line number is for the specified

stratum

(see the

class comment

for a
description of strata).

equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this Location for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a Location and if it refers to
the same point in the same VM as this Location.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

boolean equals​(

Object

obj)

Compares the specified Object with this Location for equality.

hashCode

```java
int hashCode()
```

Returns the hash code value for this Location.

**Overrides:** hashCode

in class

Object
**Returns:** the integer hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

int hashCode()

Returns the hash code value for this Location.

---

