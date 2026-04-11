# Interface ReferenceType

**Source:** `jdk.jdi\com\sun\jdi\ReferenceType.html`

### Class Description

```java
public interface
ReferenceType

extends
Type
,
Comparable
<
ReferenceType
>,
Accessible
```

The type of an object in a target VM. ReferenceType encompasses
classes, interfaces, and array types as defined in

The Java™ Language Specification

.
All ReferenceType objects belong to one of the following
subinterfaces:

ClassType

for classes,

InterfaceType

for interfaces, and

ArrayType

for arrays.
Note that primitive classes (for example, the

reflected type

of

Integer.TYPE

)
are represented as ClassType.
The VM creates Class objects for all three, so from the VM perspective,
each ReferenceType maps to a distinct Class object.

ReferenceTypes can
be obtained by querying a particular

ObjectReference

for its
type or by getting a list of all reference types from the

VirtualMachine

.

ReferenceType provides access to static type information such as
methods and fields and provides access to dynamic type
information such as the corresponding Class object and the classloader.

Any method on

ReferenceType

which directly or
indirectly takes

ReferenceType

as an parameter may throw

VMDisconnectedException

if the target VM is
disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

ReferenceType

which directly or
indirectly takes

ReferenceType

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

Any method on

ReferenceType

or which directly or indirectly takes

ReferenceType

as parameter may throw

ObjectCollectedException

if the mirrored type has been unloaded.

**All Superinterfaces:** Accessible

,

Comparable

<

ReferenceType

>

,

Mirror

,

Type

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
name()

Gets the fully qualified name of this type. The returned name
is formatted as it might appear in a Java programming langauge
declaration for objects of this type.

For primitive classes
the returned name is the name of the corresponding primitive
type; for example, "int" is returned as the name of the class
represented by

Integer.TYPE

.

**Specified by:**
- name

in interface

Type

**Returns:**
- a string containing the type name.

---

#### String
genericSignature()

Gets the generic signature for this type if there is one.
Generic signatures are described in the

The Java™ Virtual Machine Specification

.

**Returns:**
- a string containing the generic signature, or

null

if there is no generic signature.

**Since:**
- 1.5

---

#### ClassLoaderReference
classLoader()

Gets the classloader object which loaded the class corresponding
to this type.

**Returns:**
- a

ClassLoaderReference

which mirrors the classloader,
or

null

if the class was loaded through the bootstrap class
loader.

---

#### default
ModuleReference
module()

Gets the module object which contains the class corresponding
to this type.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetModuleInfo()

to determine if the operation is supported.

**Returns:**
- a

ModuleReference

which mirrors the module in the target VM.

**Throws:**
- UnsupportedOperationException

- if
the target virtual machine does not support this
operation.

**Since:**
- 9

**Implementation Requirements:**
- The default implementation throws

UnsupportedOperationException

.

---

#### String
sourceName()
throws
AbsentInformationException

Gets an identifying name for the source corresponding to the
declaration of this type. Interpretation of this string is
the responsibility of the source repository mechanism.

The returned name is dependent on VM's default stratum
(

VirtualMachine.getDefaultStratum()

).
In the reference implementation, when using the base stratum,
the returned string is the
unqualified name of the source file containing the declaration
of this type. In other strata the returned source name is
the first source name for that stratum. Since other languages
may have more than one source name for a reference type,
the use of

Location.sourceName()

or

sourceNames(String)

is preferred.

For arrays (

ArrayType

) and primitive classes,
AbsentInformationException is always thrown.

**Returns:**
- the string source file name

**Throws:**
- AbsentInformationException

- if the source name is not
known

---

#### List
<
String
> sourceNames​(
String
stratum)
throws
AbsentInformationException

Gets the identifying names for all the source corresponding to the
declaration of this type. Interpretation of these names is
the responsibility of the source repository mechanism.

The returned names are for the specified stratum
(see

Location

for a description of strata).
In the reference implementation, when using the Java
programming language stratum,
the returned List contains one element: a String which is the
unqualified name of the source file containing the declaration
of this type. In other strata the returned source names are
all the source names defined for that stratum.

**Parameters:**
- stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.

**Returns:**
- a List of String objects each representing a source name

**Throws:**
- AbsentInformationException

- if the source names are not
known.

For arrays (

ArrayType

) and primitive classes,
AbsentInformationException is always thrown.

**Since:**
- 1.4

---

#### List
<
String
> sourcePaths​(
String
stratum)
throws
AbsentInformationException

Gets the paths to the source corresponding to the
declaration of this type. Interpretation of these paths is
the responsibility of the source repository mechanism.

The returned paths are for the specified stratum
(see

Location

for a description of strata).
In the reference implementation, for strata which
do not explicitly specify source path (the Java
programming language stratum never does), the returned
strings are the

sourceNames(String)

prefixed by
the package name of this ReferenceType
converted to a platform dependent path.
For example, on a Windows platform,

java.lang.Thread

would return a List containing one element:

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
- a List of String objects each representing a source path

**Throws:**
- AbsentInformationException

- if the source names are not
known.

For arrays (

ArrayType

) and primitive classes,
AbsentInformationException is always thrown.

**Since:**
- 1.4

---

#### String
sourceDebugExtension()
throws
AbsentInformationException

Get the source debug extension of this type.

Not all target virtual machines support this operation.
Use

canGetSourceDebugExtension()

to determine if the operation is supported.

**Returns:**
- as a string the source debug extension attribute

**Throws:**
- AbsentInformationException

- if the extension is not
specified
- UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetSourceDebugExtension()

,

---

#### boolean isStatic()

Determines if this type was declared static. Only nested types,
can be declared static, so

false

is returned
for any package-level type, array type, or primitive class.

**Returns:**
- true

if this type is static; false otherwise.

---

#### boolean isAbstract()

Determines if this type was declared abstract.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:**
- true

if this type is abstract; false otherwise.

---

#### boolean isFinal()

Determines if this type was declared final.

For arrays (

ArrayType

) and primitive classes,
the return value is always true.

**Returns:**
- true

if this type is final; false otherwise.

---

#### boolean isPrepared()

Determines if this type has been prepared. See the JVM
specification for a definition of class preparation.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:**
- true

if this type is prepared; false otherwise.

---

#### boolean isVerified()

Determines if this type has been verified. See the JVM
specification for a definition of class verification.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:**
- true

if this type is verified; false otherwise.

---

#### boolean isInitialized()

Determines if this type has been initialized. See the JVM
specification for a definition of class verification.
For

InterfaceType

, this method always returns the
same value as

isPrepared()

.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:**
- true

if this type is initialized; false otherwise.

---

#### boolean failedToInitialize()

Determines if initialization failed for this class. See the JVM
specification for details on class initialization.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:**
- true

if initialization was attempted and
failed; false otherwise.

---

#### List
<
Field
> fields()

Returns a list containing each

Field

declared in this type.
Inherited fields are not included. Any synthetic fields created
by the compiler are included in the list.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:**
- a list

Field

objects; the list has length 0
if no fields exist.

**Throws:**
- ClassNotPreparedException

- if this class not yet been
prepared.

---

#### List
<
Field
> visibleFields()

Returns a list containing each unhidden and unambiguous

Field

in this type.
Each field that can be accessed from the class
or its instances with its simple name is included. Fields that
are ambiguously multiply inherited or fields that are hidden by
fields with the same name in a more recently inherited class
cannot be accessed
by their simple names and are not included in the returned
list. All other inherited fields are included.
See JLS section 8.3 for details.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:**
- a List of

Field

objects; the list has length
0 if no visible fields exist.

**Throws:**
- ClassNotPreparedException

- if this class not yet been
prepared.

---

#### List
<
Field
> allFields()

Returns a list containing each

Field

declared in this type,
and its superclasses, implemented interfaces, and/or superinterfaces.
All declared and inherited
fields are included, regardless of whether they are hidden or
multiply inherited.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:**
- a List of

Field

objects; the list has length
0 if no fields exist.

**Throws:**
- ClassNotPreparedException

- if this class not yet been
prepared.

---

#### Field
fieldByName​(
String
fieldName)

Finds the visible

Field

with the given
non-ambiguous name. This method follows the
inheritance rules specified in the JLS (8.3.3) to determine
visibility.

For arrays (

ArrayType

) and primitive classes, the returned
value is always null.

**Parameters:**
- fieldName

- a String containing the name of desired field.

**Returns:**
- a

Field

object which mirrors the found field, or
null if there is no field with the given name or if the given
name is ambiguous.

**Throws:**
- ClassNotPreparedException

- if this class not yet been
prepared.

---

#### List
<
Method
> methods()

Returns a list containing each

Method

declared
directly in this type.
Inherited methods are not included. Constructors,
the initialization method if any, and any synthetic methods created
by the compiler are included in the list.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:**
- a list

Method

objects; the list has length 0
if no methods exist.

**Throws:**
- ClassNotPreparedException

- if this class not yet been
prepared.

---

#### List
<
Method
> visibleMethods()

Returns a list containing each

Method

declared or inherited by this type. Methods from superclasses
or superinterfaces that that have been hidden or overridden
are not included.

Note that despite this exclusion, multiple inherited methods
with the same signature can be present in the returned list, but
at most one can be a member of a

ClassType

.
See JLS section 8.4.6 for details.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:**
- a List of

Method

objects; the list has length
0 if no visible methods exist.

**Throws:**
- ClassNotPreparedException

- if this class not yet been
prepared.

---

#### List
<
Method
> allMethods()

Returns a list containing each

Method

declared in this type,
and its superclasses, implemented interfaces, and/or superinterfaces.
All declared and inherited
methods are included, regardless of whether they are hidden or
overridden.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:**
- a List of

Method

objects; the list has length
0 if no methods exist.

**Throws:**
- ClassNotPreparedException

- if this class not yet been
prepared.

---

#### List
<
Method
> methodsByName​(
String
name)

Returns a List containing each visible

Method

that
has the given name. This is most commonly used to
find overloaded methods.

Overridden and hidden methods are not included.
See JLS (8.4.6) for details.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Parameters:**
- name

- the name of the method to find.

**Returns:**
- a List of

Method

objects that match the given
name; the list has length 0 if no matching methods are found.

**Throws:**
- ClassNotPreparedException

- if this class not yet been
prepared.

---

#### List
<
Method
> methodsByName​(
String
name,

String
signature)

Returns a List containing each visible

Method

that
has the given name and signature.
The signature string is the
JNI signature for the target method:

- ()V

([Ljava/lang/String;)V

(IIII)Z

This method follows the inheritance rules specified
in the JLS (8.4.6) to determine visibility.

At most one method in the list is a concrete method and a
component of

ClassType

; any other methods in the list
are abstract. Use

ClassType.concreteMethodByName(java.lang.String, java.lang.String)

to
retrieve only the matching concrete method.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Parameters:**
- name

- the name of the method to find.
- signature

- the signature of the method to find

**Returns:**
- a List of

Method

objects that match the given
name and signature; the list has length 0 if no matching methods
are found.

**Throws:**
- ClassNotPreparedException

- if this class not yet been
prepared.

---

#### List
<
ReferenceType
> nestedTypes()

Returns a List containing

ReferenceType

objects that are
declared within this type and are currently loaded into the Virtual
Machine. Both static nested types and non-static nested
types (that is, inner types) are included. Local inner types
(declared within a code block somewhere in this reference type) are
also included in the returned list.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:**
- a List of nested

ReferenceType

objects; the list
has 0 length if there are no nested types.

---

#### Value
getValue​(
Field
field)

Gets the

Value

of a given static

Field

in this type.
The Field must be valid for this type;
that is, it must be declared in this type, a superclass, a
superinterface, or an implemented interface.

**Parameters:**
- field

- the field containing the requested value

**Returns:**
- the

Value

of the instance field.

**Throws:**
- IllegalArgumentException

- if the field is not valid for
this object's class.

---

#### Map
<
Field
,​
Value
> getValues​(
List
<? extends
Field
> fields)

Returns a map containing the

Value

of each
static

Field

in the given list.
The Fields must be valid for this type;
that is, they must be declared in this type, a superclass, a
superinterface, or an implemented interface.

**Parameters:**
- fields

- a list of

Field

objects containing the
requested values.

**Returns:**
- a Map of the requested

Field

objects with
their

Value

.

**Throws:**
- IllegalArgumentException

- if any field is not valid for
this object's class.
- VMMismatchException

- if a

Mirror

argument and this mirror
do not belong to the same

VirtualMachine

.

---

#### ClassObjectReference
classObject()

Returns the class object that corresponds to this type in the
target VM. The VM creates class objects for every kind of
ReferenceType: classes, interfaces, and array types.

**Returns:**
- the

ClassObjectReference

for this reference type
in the target VM.

---

#### List
<
Location
> allLineLocations()
throws
AbsentInformationException

Returns a list containing a

Location

object
for each executable source line in this reference type.

This method is equivalent to

allLineLocations(vm.getDefaultStratum(),null)

-
see

allLineLocations(String,String)

for more information.

**Throws:**
- AbsentInformationException

- if there is no line
number information for this class and there are non-native,
non-abstract executable members of this class.
- ClassNotPreparedException

- if this class not yet
been prepared.

---

#### List
<
Location
> allLineLocations​(
String
stratum,

String
sourceName)
throws
AbsentInformationException

Returns a list containing a

Location

object
for each executable source line in this reference type.
Each location maps a source line to a range of code
indices.
The beginning of the range can be determined through

Location.codeIndex()

. The returned list may contain
multiple locations for a particular line number, if the
compiler and/or VM has mapped that line to two or more
disjoint code index ranges. Note that it is possible for
the same source line to represent different code index
ranges in

different

methods.

For arrays (

ArrayType

) and primitive classes, the
returned list is always empty. For interfaces (

InterfaceType

), the returned list will be non-empty only
if the interface has executable code in its class
initialization.

Returned list is for the specified

stratum

(see

Location

for a description of strata).

**Parameters:**
- stratum

- The stratum to retrieve information from
or

null

for the

defaultStratum()

.
- sourceName

- Return locations only within this
source file or

null

to return locations.

**Returns:**
- a List of all source line

Location

objects.

**Throws:**
- AbsentInformationException

- if there is no line
number information for this class and there are non-native,
non-abstract executable members of this class.
Or if

sourceName

is non-

null

and source name information is not present.
- ClassNotPreparedException

- if this class not yet
been prepared.

**Since:**
- 1.4

---

#### List
<
Location
> locationsOfLine​(int lineNumber)
throws
AbsentInformationException

Returns a List containing all

Location

objects
that map to the given line number.

This method is equivalent to

locationsOfLine(vm.getDefaultStratum(), null,
lineNumber)

-
see

locationsOfLine(java.lang.String,java.lang.String,int)

for more information.

**Parameters:**
- lineNumber

- the line number

**Returns:**
- a List of all

Location

objects that map to
the given line.

**Throws:**
- AbsentInformationException

- if there is no line
number information for this class.
- ClassNotPreparedException

- if this class not yet
been prepared.

**See Also:**
- VirtualMachine.getDefaultStratum()

---

#### List
<
Location
> locationsOfLine​(
String
stratum,

String
sourceName,
int lineNumber)
throws
AbsentInformationException

Returns a List containing all

Location

objects
that map to the given line number.

For arrays (

ArrayType

) and primitive classes, the
returned list is always empty.
For interfaces (

InterfaceType

), the returned list
will be non-empty only if the interface has executable code
in its class initialization at the specified line number.
An empty list will be returned if there is no executable
code at the specified line number.

Returned list is for the specified

stratum

(see

Location

for a description of strata).

**Parameters:**
- stratum

- the stratum to use for comparing line number
and source name, or

null

to
use the

defaultStratum()

.
- sourceName

- the source name containing the line
number, or

null

to match
all source names
- lineNumber

- the line number

**Returns:**
- a List of all

Location

objects that map
to the given line.

**Throws:**
- AbsentInformationException

- if there is no line
number information for this class.
Or if

sourceName

is non-

null

and source name information is not present.
- ClassNotPreparedException

- if this class not yet
been prepared.

**Since:**
- 1.4

---

#### List
<
String
> availableStrata()

Return the available strata for this reference type.

See the

Location

for a description of strata.

**Returns:**
- List of

java.lang.String

, each
representing a stratum

**Since:**
- 1.4

---

#### String
defaultStratum()

Returns the default stratum for this reference type.
This value is specified in the class file and cannot
be set by the user. If the class file does not
specify a default stratum the base stratum
(

"Java"

) will be returned.

See the

Location

for a description of strata.

**Since:**
- 1.4

---

#### List
<
ObjectReference
> instances​(long maxInstances)

Returns instances of this ReferenceType.
Only instances that are reachable for the purposes of garbage collection
are returned.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetInstanceInfo()

to determine if the operation is supported.

**Parameters:**
- maxInstances

- the maximum number of instances to return.
Must be non-negative. If zero, all instances are returned.

**Returns:**
- a List of

ObjectReference

objects. If there are
no instances of this ReferenceType, a zero-length list is returned.

**Throws:**
- UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetInstanceInfo()
- IllegalArgumentException

- if maxInstances is less
than zero.

**See Also:**
- VirtualMachine.instanceCounts(List)

,

ObjectReference.referringObjects(long)

**Since:**
- 1.6

---

#### boolean equals​(
Object
obj)

Compares the specified Object with this ReferenceType for equality.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true if the Object is a

ReferenceType

, if the
ReferenceTypes belong to the same VM, and if they mirror classes
which correspond to the same instance of java.lang.Class in that VM.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this ObjectReference.

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

#### int majorVersion()

Returns the class major version number, as defined in the class file format
of the Java Virtual Machine Specification.

For arrays (

ArrayType

) and primitive classes,
the returned major version number value is zero.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetClassFileVersion()

to determine if the operation is supported.

**Returns:**
- the major version number of the class.

**Throws:**
- UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetClassFileVersion()

**Since:**
- 1.6

---

#### int minorVersion()

Returns the class minor version number, as defined in the class file format
of the Java Virtual Machine Specification.

For arrays (

ArrayType

) and primitive classes,
the returned minor version number value is zero.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetClassFileVersion()

to determine if the operation is supported.

**Returns:**
- the minor version number of the class.

**Throws:**
- UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetClassFileVersion()

**Since:**
- 1.6

---

#### int constantPoolCount()

Returns the number of entries in the constant pool plus one.
This corresponds to the constant_pool_count item of the Class File Format
in the Java Virtual Machine Specification.

For arrays (

ArrayType

) and primitive classes,
the returned constant pool count value is zero.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetConstantPool()

to determine if the operation is supported.

**Returns:**
- total number of constant pool entries for a class plus one.

**Throws:**
- UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetConstantPool()

**See Also:**
- constantPool()

**Since:**
- 1.6

---

#### byte[] constantPool()

Returns the raw bytes of the constant pool in the format of the
constant_pool item of the Class File Format in the Java Virtual
Machine Specification. The format of the constant pool may
differ between versions of the Class File Format, so, the
minor and major class version numbers should be checked for
compatibility.

For arrays (

ArrayType

) and primitive classes,
a zero length byte array is returned.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetConstantPool()

to determine if the operation is supported.

**Returns:**
- the raw bytes of constant pool.

**Throws:**
- UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetConstantPool()

**See Also:**
- constantPoolCount()

**Since:**
- 1.6

---

### Additional Sections

#### Interface ReferenceType

**All Superinterfaces:** Accessible

,

Comparable

<

ReferenceType

>

,

Mirror

,

Type

**All Known Subinterfaces:** ArrayType

,

ClassType

,

InterfaceType

```java
public interface
ReferenceType

extends
Type
,
Comparable
<
ReferenceType
>,
Accessible
```

The type of an object in a target VM. ReferenceType encompasses
classes, interfaces, and array types as defined in

The Java™ Language Specification

.
All ReferenceType objects belong to one of the following
subinterfaces:

ClassType

for classes,

InterfaceType

for interfaces, and

ArrayType

for arrays.
Note that primitive classes (for example, the

reflected type

of

Integer.TYPE

)
are represented as ClassType.
The VM creates Class objects for all three, so from the VM perspective,
each ReferenceType maps to a distinct Class object.

ReferenceTypes can
be obtained by querying a particular

ObjectReference

for its
type or by getting a list of all reference types from the

VirtualMachine

.

ReferenceType provides access to static type information such as
methods and fields and provides access to dynamic type
information such as the corresponding Class object and the classloader.

Any method on

ReferenceType

which directly or
indirectly takes

ReferenceType

as an parameter may throw

VMDisconnectedException

if the target VM is
disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

ReferenceType

which directly or
indirectly takes

ReferenceType

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

Any method on

ReferenceType

or which directly or indirectly takes

ReferenceType

as parameter may throw

ObjectCollectedException

if the mirrored type has been unloaded.

**Since:** 1.3
**See Also:** ObjectReference

,

ObjectReference.referenceType()

,

VirtualMachine

,

VirtualMachine.allClasses()

public interface

ReferenceType

extends

Type

,

Comparable

<

ReferenceType

>,

Accessible

The type of an object in a target VM. ReferenceType encompasses
classes, interfaces, and array types as defined in

The Java™ Language Specification

.
All ReferenceType objects belong to one of the following
subinterfaces:

ClassType

for classes,

InterfaceType

for interfaces, and

ArrayType

for arrays.
Note that primitive classes (for example, the

reflected type

of

Integer.TYPE

)
are represented as ClassType.
The VM creates Class objects for all three, so from the VM perspective,
each ReferenceType maps to a distinct Class object.

ReferenceTypes can
be obtained by querying a particular

ObjectReference

for its
type or by getting a list of all reference types from the

VirtualMachine

.

ReferenceType provides access to static type information such as
methods and fields and provides access to dynamic type
information such as the corresponding Class object and the classloader.

Any method on

ReferenceType

which directly or
indirectly takes

ReferenceType

as an parameter may throw

VMDisconnectedException

if the target VM is
disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

ReferenceType

which directly or
indirectly takes

ReferenceType

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

Any method on

ReferenceType

or which directly or indirectly takes

ReferenceType

as parameter may throw

ObjectCollectedException

if the mirrored type has been unloaded.

ReferenceTypes can
be obtained by querying a particular

ObjectReference

for its
type or by getting a list of all reference types from the

VirtualMachine

.

ReferenceType provides access to static type information such as
methods and fields and provides access to dynamic type
information such as the corresponding Class object and the classloader.

Any method on

ReferenceType

which directly or
indirectly takes

ReferenceType

as an parameter may throw

VMDisconnectedException

if the target VM is
disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

ReferenceType

which directly or
indirectly takes

ReferenceType

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

Any method on

ReferenceType

or which directly or indirectly takes

ReferenceType

as parameter may throw

ObjectCollectedException

if the mirrored type has been unloaded.

ReferenceType provides access to static type information such as
methods and fields and provides access to dynamic type
information such as the corresponding Class object and the classloader.

Any method on

ReferenceType

which directly or
indirectly takes

ReferenceType

as an parameter may throw

VMDisconnectedException

if the target VM is
disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

ReferenceType

which directly or
indirectly takes

ReferenceType

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

Any method on

ReferenceType

or which directly or indirectly takes

ReferenceType

as parameter may throw

ObjectCollectedException

if the mirrored type has been unloaded.

Any method on

ReferenceType

which directly or
indirectly takes

ReferenceType

as an parameter may throw

VMDisconnectedException

if the target VM is
disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

ReferenceType

which directly or
indirectly takes

ReferenceType

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

Any method on

ReferenceType

or which directly or indirectly takes

ReferenceType

as parameter may throw

ObjectCollectedException

if the mirrored type has been unloaded.

Any method on

ReferenceType

which directly or
indirectly takes

ReferenceType

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

Any method on

ReferenceType

or which directly or indirectly takes

ReferenceType

as parameter may throw

ObjectCollectedException

if the mirrored type has been unloaded.

Any method on

ReferenceType

or which directly or indirectly takes

ReferenceType

as parameter may throw

ObjectCollectedException

if the mirrored type has been unloaded.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

List

<

Field

>

allFields

()

Returns a list containing each

Field

declared in this type,
and its superclasses, implemented interfaces, and/or superinterfaces.

List

<

Location

>

allLineLocations

()

Returns a list containing a

Location

object
for each executable source line in this reference type.

List

<

Location

>

allLineLocations

​(

String

stratum,

String

sourceName)

Returns a list containing a

Location

object
for each executable source line in this reference type.

List

<

Method

>

allMethods

()

Returns a list containing each

Method

declared in this type,
and its superclasses, implemented interfaces, and/or superinterfaces.

List

<

String

>

availableStrata

()

Return the available strata for this reference type.

ClassLoaderReference

classLoader

()

Gets the classloader object which loaded the class corresponding
to this type.

ClassObjectReference

classObject

()

Returns the class object that corresponds to this type in the
target VM.

byte[]

constantPool

()

Returns the raw bytes of the constant pool in the format of the
constant_pool item of the Class File Format in the Java Virtual
Machine Specification.

int

constantPoolCount

()

Returns the number of entries in the constant pool plus one.

String

defaultStratum

()

Returns the default stratum for this reference type.

boolean

equals

​(

Object

obj)

Compares the specified Object with this ReferenceType for equality.

boolean

failedToInitialize

()

Determines if initialization failed for this class.

Field

fieldByName

​(

String

fieldName)

Finds the visible

Field

with the given
non-ambiguous name.

List

<

Field

>

fields

()

Returns a list containing each

Field

declared in this type.

String

genericSignature

()

Gets the generic signature for this type if there is one.

Value

getValue

​(

Field

field)

Gets the

Value

of a given static

Field

in this type.

Map

<

Field

,​

Value

>

getValues

​(

List

<? extends

Field

> fields)

Returns a map containing the

Value

of each
static

Field

in the given list.

int

hashCode

()

Returns the hash code value for this ObjectReference.

List

<

ObjectReference

>

instances

​(long maxInstances)

Returns instances of this ReferenceType.

boolean

isAbstract

()

Determines if this type was declared abstract.

boolean

isFinal

()

Determines if this type was declared final.

boolean

isInitialized

()

Determines if this type has been initialized.

boolean

isPrepared

()

Determines if this type has been prepared.

boolean

isStatic

()

Determines if this type was declared static.

boolean

isVerified

()

Determines if this type has been verified.

List

<

Location

>

locationsOfLine

​(int lineNumber)

Returns a List containing all

Location

objects
that map to the given line number.

List

<

Location

>

locationsOfLine

​(

String

stratum,

String

sourceName,
int lineNumber)

Returns a List containing all

Location

objects
that map to the given line number.

int

majorVersion

()

Returns the class major version number, as defined in the class file format
of the Java Virtual Machine Specification.

List

<

Method

>

methods

()

Returns a list containing each

Method

declared
directly in this type.

List

<

Method

>

methodsByName

​(

String

name)

Returns a List containing each visible

Method

that
has the given name.

List

<

Method

>

methodsByName

​(

String

name,

String

signature)

Returns a List containing each visible

Method

that
has the given name and signature.

int

minorVersion

()

Returns the class minor version number, as defined in the class file format
of the Java Virtual Machine Specification.

default

ModuleReference

module

()

Gets the module object which contains the class corresponding
to this type.

String

name

()

Gets the fully qualified name of this type.

List

<

ReferenceType

>

nestedTypes

()

Returns a List containing

ReferenceType

objects that are
declared within this type and are currently loaded into the Virtual
Machine.

String

sourceDebugExtension

()

Get the source debug extension of this type.

String

sourceName

()

Gets an identifying name for the source corresponding to the
declaration of this type.

List

<

String

>

sourceNames

​(

String

stratum)

Gets the identifying names for all the source corresponding to the
declaration of this type.

List

<

String

>

sourcePaths

​(

String

stratum)

Gets the paths to the source corresponding to the
declaration of this type.

List

<

Field

>

visibleFields

()

Returns a list containing each unhidden and unambiguous

Field

in this type.

List

<

Method

>

visibleMethods

()

Returns a list containing each

Method

declared or inherited by this type.

- Methods declared in interface com.sun.jdi.

Accessible

isPackagePrivate

,

isPrivate

,

isProtected

,

isPublic

,

modifiers

- Methods declared in interface java.lang.

Comparable

compareTo

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.

Type

signature

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

List

<

Field

>

allFields

()

Returns a list containing each

Field

declared in this type,
and its superclasses, implemented interfaces, and/or superinterfaces.

List

<

Location

>

allLineLocations

()

Returns a list containing a

Location

object
for each executable source line in this reference type.

List

<

Location

>

allLineLocations

​(

String

stratum,

String

sourceName)

Returns a list containing a

Location

object
for each executable source line in this reference type.

List

<

Method

>

allMethods

()

Returns a list containing each

Method

declared in this type,
and its superclasses, implemented interfaces, and/or superinterfaces.

List

<

String

>

availableStrata

()

Return the available strata for this reference type.

ClassLoaderReference

classLoader

()

Gets the classloader object which loaded the class corresponding
to this type.

ClassObjectReference

classObject

()

Returns the class object that corresponds to this type in the
target VM.

byte[]

constantPool

()

Returns the raw bytes of the constant pool in the format of the
constant_pool item of the Class File Format in the Java Virtual
Machine Specification.

int

constantPoolCount

()

Returns the number of entries in the constant pool plus one.

String

defaultStratum

()

Returns the default stratum for this reference type.

boolean

equals

​(

Object

obj)

Compares the specified Object with this ReferenceType for equality.

boolean

failedToInitialize

()

Determines if initialization failed for this class.

Field

fieldByName

​(

String

fieldName)

Finds the visible

Field

with the given
non-ambiguous name.

List

<

Field

>

fields

()

Returns a list containing each

Field

declared in this type.

String

genericSignature

()

Gets the generic signature for this type if there is one.

Value

getValue

​(

Field

field)

Gets the

Value

of a given static

Field

in this type.

Map

<

Field

,​

Value

>

getValues

​(

List

<? extends

Field

> fields)

Returns a map containing the

Value

of each
static

Field

in the given list.

int

hashCode

()

Returns the hash code value for this ObjectReference.

List

<

ObjectReference

>

instances

​(long maxInstances)

Returns instances of this ReferenceType.

boolean

isAbstract

()

Determines if this type was declared abstract.

boolean

isFinal

()

Determines if this type was declared final.

boolean

isInitialized

()

Determines if this type has been initialized.

boolean

isPrepared

()

Determines if this type has been prepared.

boolean

isStatic

()

Determines if this type was declared static.

boolean

isVerified

()

Determines if this type has been verified.

List

<

Location

>

locationsOfLine

​(int lineNumber)

Returns a List containing all

Location

objects
that map to the given line number.

List

<

Location

>

locationsOfLine

​(

String

stratum,

String

sourceName,
int lineNumber)

Returns a List containing all

Location

objects
that map to the given line number.

int

majorVersion

()

Returns the class major version number, as defined in the class file format
of the Java Virtual Machine Specification.

List

<

Method

>

methods

()

Returns a list containing each

Method

declared
directly in this type.

List

<

Method

>

methodsByName

​(

String

name)

Returns a List containing each visible

Method

that
has the given name.

List

<

Method

>

methodsByName

​(

String

name,

String

signature)

Returns a List containing each visible

Method

that
has the given name and signature.

int

minorVersion

()

Returns the class minor version number, as defined in the class file format
of the Java Virtual Machine Specification.

default

ModuleReference

module

()

Gets the module object which contains the class corresponding
to this type.

String

name

()

Gets the fully qualified name of this type.

List

<

ReferenceType

>

nestedTypes

()

Returns a List containing

ReferenceType

objects that are
declared within this type and are currently loaded into the Virtual
Machine.

String

sourceDebugExtension

()

Get the source debug extension of this type.

String

sourceName

()

Gets an identifying name for the source corresponding to the
declaration of this type.

List

<

String

>

sourceNames

​(

String

stratum)

Gets the identifying names for all the source corresponding to the
declaration of this type.

List

<

String

>

sourcePaths

​(

String

stratum)

Gets the paths to the source corresponding to the
declaration of this type.

List

<

Field

>

visibleFields

()

Returns a list containing each unhidden and unambiguous

Field

in this type.

List

<

Method

>

visibleMethods

()

Returns a list containing each

Method

declared or inherited by this type.

- Methods declared in interface com.sun.jdi.

Accessible

isPackagePrivate

,

isPrivate

,

isProtected

,

isPublic

,

modifiers

- Methods declared in interface java.lang.

Comparable

compareTo

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.

Type

signature

---

#### Method Summary

Returns a list containing each

Field

declared in this type,
and its superclasses, implemented interfaces, and/or superinterfaces.

Returns a list containing a

Location

object
for each executable source line in this reference type.

Returns a list containing each

Method

declared in this type,
and its superclasses, implemented interfaces, and/or superinterfaces.

Return the available strata for this reference type.

Gets the classloader object which loaded the class corresponding
to this type.

Returns the class object that corresponds to this type in the
target VM.

Returns the raw bytes of the constant pool in the format of the
constant_pool item of the Class File Format in the Java Virtual
Machine Specification.

Returns the number of entries in the constant pool plus one.

Returns the default stratum for this reference type.

Compares the specified Object with this ReferenceType for equality.

Determines if initialization failed for this class.

Finds the visible

Field

with the given
non-ambiguous name.

Returns a list containing each

Field

declared in this type.

Gets the generic signature for this type if there is one.

Gets the

Value

of a given static

Field

in this type.

Returns a map containing the

Value

of each
static

Field

in the given list.

Returns the hash code value for this ObjectReference.

Returns instances of this ReferenceType.

Determines if this type was declared abstract.

Determines if this type was declared final.

Determines if this type has been initialized.

Determines if this type has been prepared.

Determines if this type was declared static.

Determines if this type has been verified.

Returns a List containing all

Location

objects
that map to the given line number.

Returns the class major version number, as defined in the class file format
of the Java Virtual Machine Specification.

Returns a list containing each

Method

declared
directly in this type.

Returns a List containing each visible

Method

that
has the given name.

Returns a List containing each visible

Method

that
has the given name and signature.

Returns the class minor version number, as defined in the class file format
of the Java Virtual Machine Specification.

Gets the module object which contains the class corresponding
to this type.

Gets the fully qualified name of this type.

Returns a List containing

ReferenceType

objects that are
declared within this type and are currently loaded into the Virtual
Machine.

Get the source debug extension of this type.

Gets an identifying name for the source corresponding to the
declaration of this type.

Gets the identifying names for all the source corresponding to the
declaration of this type.

Gets the paths to the source corresponding to the
declaration of this type.

Returns a list containing each unhidden and unambiguous

Field

in this type.

Returns a list containing each

Method

declared or inherited by this type.

Methods declared in interface com.sun.jdi.

Accessible

isPackagePrivate

,

isPrivate

,

isProtected

,

isPublic

,

modifiers

---

#### Methods declared in interface com.sun.jdi. Accessible

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

Methods declared in interface com.sun.jdi.

Type

signature

---

#### Methods declared in interface com.sun.jdi. Type

============ METHOD DETAIL ==========

- Method Detail

- name

```java
String
name()
```

Gets the fully qualified name of this type. The returned name
is formatted as it might appear in a Java programming langauge
declaration for objects of this type.

For primitive classes
the returned name is the name of the corresponding primitive
type; for example, "int" is returned as the name of the class
represented by

Integer.TYPE

.

**Specified by:** name

in interface

Type
**Returns:** a string containing the type name.

- genericSignature

```java
String
genericSignature()
```

Gets the generic signature for this type if there is one.
Generic signatures are described in the

The Java™ Virtual Machine Specification

.

**Returns:** a string containing the generic signature, or

null

if there is no generic signature.
**Since:** 1.5

- classLoader

```java
ClassLoaderReference
classLoader()
```

Gets the classloader object which loaded the class corresponding
to this type.

**Returns:** a

ClassLoaderReference

which mirrors the classloader,
or

null

if the class was loaded through the bootstrap class
loader.

- module

```java
default
ModuleReference
module()
```

Gets the module object which contains the class corresponding
to this type.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetModuleInfo()

to determine if the operation is supported.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
**Returns:** a

ModuleReference

which mirrors the module in the target VM.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.
**Since:** 9

- sourceName

```java
String
sourceName()
throws
AbsentInformationException
```

Gets an identifying name for the source corresponding to the
declaration of this type. Interpretation of this string is
the responsibility of the source repository mechanism.

The returned name is dependent on VM's default stratum
(

VirtualMachine.getDefaultStratum()

).
In the reference implementation, when using the base stratum,
the returned string is the
unqualified name of the source file containing the declaration
of this type. In other strata the returned source name is
the first source name for that stratum. Since other languages
may have more than one source name for a reference type,
the use of

Location.sourceName()

or

sourceNames(String)

is preferred.

For arrays (

ArrayType

) and primitive classes,
AbsentInformationException is always thrown.

**Returns:** the string source file name
**Throws:** AbsentInformationException

- if the source name is not
known

- sourceNames

```java
List
<
String
> sourceNames​(
String
stratum)
throws
AbsentInformationException
```

Gets the identifying names for all the source corresponding to the
declaration of this type. Interpretation of these names is
the responsibility of the source repository mechanism.

The returned names are for the specified stratum
(see

Location

for a description of strata).
In the reference implementation, when using the Java
programming language stratum,
the returned List contains one element: a String which is the
unqualified name of the source file containing the declaration
of this type. In other strata the returned source names are
all the source names defined for that stratum.

**Parameters:** stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.
**Returns:** a List of String objects each representing a source name
**Throws:** AbsentInformationException

- if the source names are not
known.

For arrays (

ArrayType

) and primitive classes,
AbsentInformationException is always thrown.
**Since:** 1.4

- sourcePaths

```java
List
<
String
> sourcePaths​(
String
stratum)
throws
AbsentInformationException
```

Gets the paths to the source corresponding to the
declaration of this type. Interpretation of these paths is
the responsibility of the source repository mechanism.

The returned paths are for the specified stratum
(see

Location

for a description of strata).
In the reference implementation, for strata which
do not explicitly specify source path (the Java
programming language stratum never does), the returned
strings are the

sourceNames(String)

prefixed by
the package name of this ReferenceType
converted to a platform dependent path.
For example, on a Windows platform,

java.lang.Thread

would return a List containing one element:

"java\lang\Thread.java"

.

**Parameters:** stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.
**Returns:** a List of String objects each representing a source path
**Throws:** AbsentInformationException

- if the source names are not
known.

For arrays (

ArrayType

) and primitive classes,
AbsentInformationException is always thrown.
**Since:** 1.4

- sourceDebugExtension

```java
String
sourceDebugExtension()
throws
AbsentInformationException
```

Get the source debug extension of this type.

Not all target virtual machines support this operation.
Use

canGetSourceDebugExtension()

to determine if the operation is supported.

**Returns:** as a string the source debug extension attribute
**Throws:** AbsentInformationException

- if the extension is not
specified
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetSourceDebugExtension()

,

- isStatic

```java
boolean isStatic()
```

Determines if this type was declared static. Only nested types,
can be declared static, so

false

is returned
for any package-level type, array type, or primitive class.

**Returns:** true

if this type is static; false otherwise.

- isAbstract

```java
boolean isAbstract()
```

Determines if this type was declared abstract.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:** true

if this type is abstract; false otherwise.

- isFinal

```java
boolean isFinal()
```

Determines if this type was declared final.

For arrays (

ArrayType

) and primitive classes,
the return value is always true.

**Returns:** true

if this type is final; false otherwise.

- isPrepared

```java
boolean isPrepared()
```

Determines if this type has been prepared. See the JVM
specification for a definition of class preparation.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:** true

if this type is prepared; false otherwise.

- isVerified

```java
boolean isVerified()
```

Determines if this type has been verified. See the JVM
specification for a definition of class verification.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:** true

if this type is verified; false otherwise.

- isInitialized

```java
boolean isInitialized()
```

Determines if this type has been initialized. See the JVM
specification for a definition of class verification.
For

InterfaceType

, this method always returns the
same value as

isPrepared()

.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:** true

if this type is initialized; false otherwise.

- failedToInitialize

```java
boolean failedToInitialize()
```

Determines if initialization failed for this class. See the JVM
specification for details on class initialization.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:** true

if initialization was attempted and
failed; false otherwise.

- fields

```java
List
<
Field
> fields()
```

Returns a list containing each

Field

declared in this type.
Inherited fields are not included. Any synthetic fields created
by the compiler are included in the list.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a list

Field

objects; the list has length 0
if no fields exist.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

- visibleFields

```java
List
<
Field
> visibleFields()
```

Returns a list containing each unhidden and unambiguous

Field

in this type.
Each field that can be accessed from the class
or its instances with its simple name is included. Fields that
are ambiguously multiply inherited or fields that are hidden by
fields with the same name in a more recently inherited class
cannot be accessed
by their simple names and are not included in the returned
list. All other inherited fields are included.
See JLS section 8.3 for details.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a List of

Field

objects; the list has length
0 if no visible fields exist.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

- allFields

```java
List
<
Field
> allFields()
```

Returns a list containing each

Field

declared in this type,
and its superclasses, implemented interfaces, and/or superinterfaces.
All declared and inherited
fields are included, regardless of whether they are hidden or
multiply inherited.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a List of

Field

objects; the list has length
0 if no fields exist.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

- fieldByName

```java
Field
fieldByName​(
String
fieldName)
```

Finds the visible

Field

with the given
non-ambiguous name. This method follows the
inheritance rules specified in the JLS (8.3.3) to determine
visibility.

For arrays (

ArrayType

) and primitive classes, the returned
value is always null.

**Parameters:** fieldName

- a String containing the name of desired field.
**Returns:** a

Field

object which mirrors the found field, or
null if there is no field with the given name or if the given
name is ambiguous.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

- methods

```java
List
<
Method
> methods()
```

Returns a list containing each

Method

declared
directly in this type.
Inherited methods are not included. Constructors,
the initialization method if any, and any synthetic methods created
by the compiler are included in the list.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a list

Method

objects; the list has length 0
if no methods exist.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

- visibleMethods

```java
List
<
Method
> visibleMethods()
```

Returns a list containing each

Method

declared or inherited by this type. Methods from superclasses
or superinterfaces that that have been hidden or overridden
are not included.

Note that despite this exclusion, multiple inherited methods
with the same signature can be present in the returned list, but
at most one can be a member of a

ClassType

.
See JLS section 8.4.6 for details.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a List of

Method

objects; the list has length
0 if no visible methods exist.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

- allMethods

```java
List
<
Method
> allMethods()
```

Returns a list containing each

Method

declared in this type,
and its superclasses, implemented interfaces, and/or superinterfaces.
All declared and inherited
methods are included, regardless of whether they are hidden or
overridden.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a List of

Method

objects; the list has length
0 if no methods exist.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

- methodsByName

```java
List
<
Method
> methodsByName​(
String
name)
```

Returns a List containing each visible

Method

that
has the given name. This is most commonly used to
find overloaded methods.

Overridden and hidden methods are not included.
See JLS (8.4.6) for details.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Parameters:** name

- the name of the method to find.
**Returns:** a List of

Method

objects that match the given
name; the list has length 0 if no matching methods are found.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

- methodsByName

```java
List
<
Method
> methodsByName​(
String
name,

String
signature)
```

Returns a List containing each visible

Method

that
has the given name and signature.
The signature string is the
JNI signature for the target method:

- ()V

([Ljava/lang/String;)V

(IIII)Z

This method follows the inheritance rules specified
in the JLS (8.4.6) to determine visibility.

At most one method in the list is a concrete method and a
component of

ClassType

; any other methods in the list
are abstract. Use

ClassType.concreteMethodByName(java.lang.String, java.lang.String)

to
retrieve only the matching concrete method.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Parameters:** name

- the name of the method to find.
**Parameters:** signature

- the signature of the method to find
**Returns:** a List of

Method

objects that match the given
name and signature; the list has length 0 if no matching methods
are found.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

- nestedTypes

```java
List
<
ReferenceType
> nestedTypes()
```

Returns a List containing

ReferenceType

objects that are
declared within this type and are currently loaded into the Virtual
Machine. Both static nested types and non-static nested
types (that is, inner types) are included. Local inner types
(declared within a code block somewhere in this reference type) are
also included in the returned list.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a List of nested

ReferenceType

objects; the list
has 0 length if there are no nested types.

- getValue

```java
Value
getValue​(
Field
field)
```

Gets the

Value

of a given static

Field

in this type.
The Field must be valid for this type;
that is, it must be declared in this type, a superclass, a
superinterface, or an implemented interface.

**Parameters:** field

- the field containing the requested value
**Returns:** the

Value

of the instance field.
**Throws:** IllegalArgumentException

- if the field is not valid for
this object's class.

- getValues

```java
Map
<
Field
,​
Value
> getValues​(
List
<? extends
Field
> fields)
```

Returns a map containing the

Value

of each
static

Field

in the given list.
The Fields must be valid for this type;
that is, they must be declared in this type, a superclass, a
superinterface, or an implemented interface.

**Parameters:** fields

- a list of

Field

objects containing the
requested values.
**Returns:** a Map of the requested

Field

objects with
their

Value

.
**Throws:** IllegalArgumentException

- if any field is not valid for
this object's class.
**Throws:** VMMismatchException

- if a

Mirror

argument and this mirror
do not belong to the same

VirtualMachine

.

- classObject

```java
ClassObjectReference
classObject()
```

Returns the class object that corresponds to this type in the
target VM. The VM creates class objects for every kind of
ReferenceType: classes, interfaces, and array types.

**Returns:** the

ClassObjectReference

for this reference type
in the target VM.

- allLineLocations

```java
List
<
Location
> allLineLocations()
throws
AbsentInformationException
```

Returns a list containing a

Location

object
for each executable source line in this reference type.

This method is equivalent to

allLineLocations(vm.getDefaultStratum(),null)

-
see

allLineLocations(String,String)

for more information.

**Throws:** AbsentInformationException

- if there is no line
number information for this class and there are non-native,
non-abstract executable members of this class.
**Throws:** ClassNotPreparedException

- if this class not yet
been prepared.

- allLineLocations

```java
List
<
Location
> allLineLocations​(
String
stratum,

String
sourceName)
throws
AbsentInformationException
```

Returns a list containing a

Location

object
for each executable source line in this reference type.
Each location maps a source line to a range of code
indices.
The beginning of the range can be determined through

Location.codeIndex()

. The returned list may contain
multiple locations for a particular line number, if the
compiler and/or VM has mapped that line to two or more
disjoint code index ranges. Note that it is possible for
the same source line to represent different code index
ranges in

different

methods.

For arrays (

ArrayType

) and primitive classes, the
returned list is always empty. For interfaces (

InterfaceType

), the returned list will be non-empty only
if the interface has executable code in its class
initialization.

Returned list is for the specified

stratum

(see

Location

for a description of strata).

**Parameters:** stratum

- The stratum to retrieve information from
or

null

for the

defaultStratum()

.
**Parameters:** sourceName

- Return locations only within this
source file or

null

to return locations.
**Returns:** a List of all source line

Location

objects.
**Throws:** AbsentInformationException

- if there is no line
number information for this class and there are non-native,
non-abstract executable members of this class.
Or if

sourceName

is non-

null

and source name information is not present.
**Throws:** ClassNotPreparedException

- if this class not yet
been prepared.
**Since:** 1.4

- locationsOfLine

```java
List
<
Location
> locationsOfLine​(int lineNumber)
throws
AbsentInformationException
```

Returns a List containing all

Location

objects
that map to the given line number.

This method is equivalent to

locationsOfLine(vm.getDefaultStratum(), null,
lineNumber)

-
see

locationsOfLine(java.lang.String,java.lang.String,int)

for more information.

**Parameters:** lineNumber

- the line number
**Returns:** a List of all

Location

objects that map to
the given line.
**Throws:** AbsentInformationException

- if there is no line
number information for this class.
**Throws:** ClassNotPreparedException

- if this class not yet
been prepared.
**See Also:** VirtualMachine.getDefaultStratum()

- locationsOfLine

```java
List
<
Location
> locationsOfLine​(
String
stratum,

String
sourceName,
int lineNumber)
throws
AbsentInformationException
```

Returns a List containing all

Location

objects
that map to the given line number.

For arrays (

ArrayType

) and primitive classes, the
returned list is always empty.
For interfaces (

InterfaceType

), the returned list
will be non-empty only if the interface has executable code
in its class initialization at the specified line number.
An empty list will be returned if there is no executable
code at the specified line number.

Returned list is for the specified

stratum

(see

Location

for a description of strata).

**Parameters:** stratum

- the stratum to use for comparing line number
and source name, or

null

to
use the

defaultStratum()

.
**Parameters:** sourceName

- the source name containing the line
number, or

null

to match
all source names
**Parameters:** lineNumber

- the line number
**Returns:** a List of all

Location

objects that map
to the given line.
**Throws:** AbsentInformationException

- if there is no line
number information for this class.
Or if

sourceName

is non-

null

and source name information is not present.
**Throws:** ClassNotPreparedException

- if this class not yet
been prepared.
**Since:** 1.4

- availableStrata

```java
List
<
String
> availableStrata()
```

Return the available strata for this reference type.

See the

Location

for a description of strata.

**Returns:** List of

java.lang.String

, each
representing a stratum
**Since:** 1.4

- defaultStratum

```java
String
defaultStratum()
```

Returns the default stratum for this reference type.
This value is specified in the class file and cannot
be set by the user. If the class file does not
specify a default stratum the base stratum
(

"Java"

) will be returned.

See the

Location

for a description of strata.

**Since:** 1.4

- instances

```java
List
<
ObjectReference
> instances​(long maxInstances)
```

Returns instances of this ReferenceType.
Only instances that are reachable for the purposes of garbage collection
are returned.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetInstanceInfo()

to determine if the operation is supported.

**Parameters:** maxInstances

- the maximum number of instances to return.
Must be non-negative. If zero, all instances are returned.
**Returns:** a List of

ObjectReference

objects. If there are
no instances of this ReferenceType, a zero-length list is returned.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetInstanceInfo()
**Throws:** IllegalArgumentException

- if maxInstances is less
than zero.
**Since:** 1.6
**See Also:** VirtualMachine.instanceCounts(List)

,

ObjectReference.referringObjects(long)

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this ReferenceType for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a

ReferenceType

, if the
ReferenceTypes belong to the same VM, and if they mirror classes
which correspond to the same instance of java.lang.Class in that VM.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this ObjectReference.

**Overrides:** hashCode

in class

Object
**Returns:** the integer hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- majorVersion

```java
int majorVersion()
```

Returns the class major version number, as defined in the class file format
of the Java Virtual Machine Specification.

For arrays (

ArrayType

) and primitive classes,
the returned major version number value is zero.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetClassFileVersion()

to determine if the operation is supported.

**Returns:** the major version number of the class.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetClassFileVersion()
**Since:** 1.6

- minorVersion

```java
int minorVersion()
```

Returns the class minor version number, as defined in the class file format
of the Java Virtual Machine Specification.

For arrays (

ArrayType

) and primitive classes,
the returned minor version number value is zero.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetClassFileVersion()

to determine if the operation is supported.

**Returns:** the minor version number of the class.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetClassFileVersion()
**Since:** 1.6

- constantPoolCount

```java
int constantPoolCount()
```

Returns the number of entries in the constant pool plus one.
This corresponds to the constant_pool_count item of the Class File Format
in the Java Virtual Machine Specification.

For arrays (

ArrayType

) and primitive classes,
the returned constant pool count value is zero.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetConstantPool()

to determine if the operation is supported.

**Returns:** total number of constant pool entries for a class plus one.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetConstantPool()
**Since:** 1.6
**See Also:** constantPool()

- constantPool

```java
byte[] constantPool()
```

Returns the raw bytes of the constant pool in the format of the
constant_pool item of the Class File Format in the Java Virtual
Machine Specification. The format of the constant pool may
differ between versions of the Class File Format, so, the
minor and major class version numbers should be checked for
compatibility.

For arrays (

ArrayType

) and primitive classes,
a zero length byte array is returned.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetConstantPool()

to determine if the operation is supported.

**Returns:** the raw bytes of constant pool.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetConstantPool()
**Since:** 1.6
**See Also:** constantPoolCount()

Method Detail

- name

```java
String
name()
```

Gets the fully qualified name of this type. The returned name
is formatted as it might appear in a Java programming langauge
declaration for objects of this type.

For primitive classes
the returned name is the name of the corresponding primitive
type; for example, "int" is returned as the name of the class
represented by

Integer.TYPE

.

**Specified by:** name

in interface

Type
**Returns:** a string containing the type name.

- genericSignature

```java
String
genericSignature()
```

Gets the generic signature for this type if there is one.
Generic signatures are described in the

The Java™ Virtual Machine Specification

.

**Returns:** a string containing the generic signature, or

null

if there is no generic signature.
**Since:** 1.5

- classLoader

```java
ClassLoaderReference
classLoader()
```

Gets the classloader object which loaded the class corresponding
to this type.

**Returns:** a

ClassLoaderReference

which mirrors the classloader,
or

null

if the class was loaded through the bootstrap class
loader.

- module

```java
default
ModuleReference
module()
```

Gets the module object which contains the class corresponding
to this type.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetModuleInfo()

to determine if the operation is supported.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
**Returns:** a

ModuleReference

which mirrors the module in the target VM.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.
**Since:** 9

- sourceName

```java
String
sourceName()
throws
AbsentInformationException
```

Gets an identifying name for the source corresponding to the
declaration of this type. Interpretation of this string is
the responsibility of the source repository mechanism.

The returned name is dependent on VM's default stratum
(

VirtualMachine.getDefaultStratum()

).
In the reference implementation, when using the base stratum,
the returned string is the
unqualified name of the source file containing the declaration
of this type. In other strata the returned source name is
the first source name for that stratum. Since other languages
may have more than one source name for a reference type,
the use of

Location.sourceName()

or

sourceNames(String)

is preferred.

For arrays (

ArrayType

) and primitive classes,
AbsentInformationException is always thrown.

**Returns:** the string source file name
**Throws:** AbsentInformationException

- if the source name is not
known

- sourceNames

```java
List
<
String
> sourceNames​(
String
stratum)
throws
AbsentInformationException
```

Gets the identifying names for all the source corresponding to the
declaration of this type. Interpretation of these names is
the responsibility of the source repository mechanism.

The returned names are for the specified stratum
(see

Location

for a description of strata).
In the reference implementation, when using the Java
programming language stratum,
the returned List contains one element: a String which is the
unqualified name of the source file containing the declaration
of this type. In other strata the returned source names are
all the source names defined for that stratum.

**Parameters:** stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.
**Returns:** a List of String objects each representing a source name
**Throws:** AbsentInformationException

- if the source names are not
known.

For arrays (

ArrayType

) and primitive classes,
AbsentInformationException is always thrown.
**Since:** 1.4

- sourcePaths

```java
List
<
String
> sourcePaths​(
String
stratum)
throws
AbsentInformationException
```

Gets the paths to the source corresponding to the
declaration of this type. Interpretation of these paths is
the responsibility of the source repository mechanism.

The returned paths are for the specified stratum
(see

Location

for a description of strata).
In the reference implementation, for strata which
do not explicitly specify source path (the Java
programming language stratum never does), the returned
strings are the

sourceNames(String)

prefixed by
the package name of this ReferenceType
converted to a platform dependent path.
For example, on a Windows platform,

java.lang.Thread

would return a List containing one element:

"java\lang\Thread.java"

.

**Parameters:** stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.
**Returns:** a List of String objects each representing a source path
**Throws:** AbsentInformationException

- if the source names are not
known.

For arrays (

ArrayType

) and primitive classes,
AbsentInformationException is always thrown.
**Since:** 1.4

- sourceDebugExtension

```java
String
sourceDebugExtension()
throws
AbsentInformationException
```

Get the source debug extension of this type.

Not all target virtual machines support this operation.
Use

canGetSourceDebugExtension()

to determine if the operation is supported.

**Returns:** as a string the source debug extension attribute
**Throws:** AbsentInformationException

- if the extension is not
specified
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetSourceDebugExtension()

,

- isStatic

```java
boolean isStatic()
```

Determines if this type was declared static. Only nested types,
can be declared static, so

false

is returned
for any package-level type, array type, or primitive class.

**Returns:** true

if this type is static; false otherwise.

- isAbstract

```java
boolean isAbstract()
```

Determines if this type was declared abstract.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:** true

if this type is abstract; false otherwise.

- isFinal

```java
boolean isFinal()
```

Determines if this type was declared final.

For arrays (

ArrayType

) and primitive classes,
the return value is always true.

**Returns:** true

if this type is final; false otherwise.

- isPrepared

```java
boolean isPrepared()
```

Determines if this type has been prepared. See the JVM
specification for a definition of class preparation.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:** true

if this type is prepared; false otherwise.

- isVerified

```java
boolean isVerified()
```

Determines if this type has been verified. See the JVM
specification for a definition of class verification.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:** true

if this type is verified; false otherwise.

- isInitialized

```java
boolean isInitialized()
```

Determines if this type has been initialized. See the JVM
specification for a definition of class verification.
For

InterfaceType

, this method always returns the
same value as

isPrepared()

.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:** true

if this type is initialized; false otherwise.

- failedToInitialize

```java
boolean failedToInitialize()
```

Determines if initialization failed for this class. See the JVM
specification for details on class initialization.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:** true

if initialization was attempted and
failed; false otherwise.

- fields

```java
List
<
Field
> fields()
```

Returns a list containing each

Field

declared in this type.
Inherited fields are not included. Any synthetic fields created
by the compiler are included in the list.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a list

Field

objects; the list has length 0
if no fields exist.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

- visibleFields

```java
List
<
Field
> visibleFields()
```

Returns a list containing each unhidden and unambiguous

Field

in this type.
Each field that can be accessed from the class
or its instances with its simple name is included. Fields that
are ambiguously multiply inherited or fields that are hidden by
fields with the same name in a more recently inherited class
cannot be accessed
by their simple names and are not included in the returned
list. All other inherited fields are included.
See JLS section 8.3 for details.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a List of

Field

objects; the list has length
0 if no visible fields exist.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

- allFields

```java
List
<
Field
> allFields()
```

Returns a list containing each

Field

declared in this type,
and its superclasses, implemented interfaces, and/or superinterfaces.
All declared and inherited
fields are included, regardless of whether they are hidden or
multiply inherited.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a List of

Field

objects; the list has length
0 if no fields exist.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

- fieldByName

```java
Field
fieldByName​(
String
fieldName)
```

Finds the visible

Field

with the given
non-ambiguous name. This method follows the
inheritance rules specified in the JLS (8.3.3) to determine
visibility.

For arrays (

ArrayType

) and primitive classes, the returned
value is always null.

**Parameters:** fieldName

- a String containing the name of desired field.
**Returns:** a

Field

object which mirrors the found field, or
null if there is no field with the given name or if the given
name is ambiguous.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

- methods

```java
List
<
Method
> methods()
```

Returns a list containing each

Method

declared
directly in this type.
Inherited methods are not included. Constructors,
the initialization method if any, and any synthetic methods created
by the compiler are included in the list.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a list

Method

objects; the list has length 0
if no methods exist.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

- visibleMethods

```java
List
<
Method
> visibleMethods()
```

Returns a list containing each

Method

declared or inherited by this type. Methods from superclasses
or superinterfaces that that have been hidden or overridden
are not included.

Note that despite this exclusion, multiple inherited methods
with the same signature can be present in the returned list, but
at most one can be a member of a

ClassType

.
See JLS section 8.4.6 for details.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a List of

Method

objects; the list has length
0 if no visible methods exist.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

- allMethods

```java
List
<
Method
> allMethods()
```

Returns a list containing each

Method

declared in this type,
and its superclasses, implemented interfaces, and/or superinterfaces.
All declared and inherited
methods are included, regardless of whether they are hidden or
overridden.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a List of

Method

objects; the list has length
0 if no methods exist.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

- methodsByName

```java
List
<
Method
> methodsByName​(
String
name)
```

Returns a List containing each visible

Method

that
has the given name. This is most commonly used to
find overloaded methods.

Overridden and hidden methods are not included.
See JLS (8.4.6) for details.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Parameters:** name

- the name of the method to find.
**Returns:** a List of

Method

objects that match the given
name; the list has length 0 if no matching methods are found.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

- methodsByName

```java
List
<
Method
> methodsByName​(
String
name,

String
signature)
```

Returns a List containing each visible

Method

that
has the given name and signature.
The signature string is the
JNI signature for the target method:

- ()V

([Ljava/lang/String;)V

(IIII)Z

This method follows the inheritance rules specified
in the JLS (8.4.6) to determine visibility.

At most one method in the list is a concrete method and a
component of

ClassType

; any other methods in the list
are abstract. Use

ClassType.concreteMethodByName(java.lang.String, java.lang.String)

to
retrieve only the matching concrete method.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Parameters:** name

- the name of the method to find.
**Parameters:** signature

- the signature of the method to find
**Returns:** a List of

Method

objects that match the given
name and signature; the list has length 0 if no matching methods
are found.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

- nestedTypes

```java
List
<
ReferenceType
> nestedTypes()
```

Returns a List containing

ReferenceType

objects that are
declared within this type and are currently loaded into the Virtual
Machine. Both static nested types and non-static nested
types (that is, inner types) are included. Local inner types
(declared within a code block somewhere in this reference type) are
also included in the returned list.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a List of nested

ReferenceType

objects; the list
has 0 length if there are no nested types.

- getValue

```java
Value
getValue​(
Field
field)
```

Gets the

Value

of a given static

Field

in this type.
The Field must be valid for this type;
that is, it must be declared in this type, a superclass, a
superinterface, or an implemented interface.

**Parameters:** field

- the field containing the requested value
**Returns:** the

Value

of the instance field.
**Throws:** IllegalArgumentException

- if the field is not valid for
this object's class.

- getValues

```java
Map
<
Field
,​
Value
> getValues​(
List
<? extends
Field
> fields)
```

Returns a map containing the

Value

of each
static

Field

in the given list.
The Fields must be valid for this type;
that is, they must be declared in this type, a superclass, a
superinterface, or an implemented interface.

**Parameters:** fields

- a list of

Field

objects containing the
requested values.
**Returns:** a Map of the requested

Field

objects with
their

Value

.
**Throws:** IllegalArgumentException

- if any field is not valid for
this object's class.
**Throws:** VMMismatchException

- if a

Mirror

argument and this mirror
do not belong to the same

VirtualMachine

.

- classObject

```java
ClassObjectReference
classObject()
```

Returns the class object that corresponds to this type in the
target VM. The VM creates class objects for every kind of
ReferenceType: classes, interfaces, and array types.

**Returns:** the

ClassObjectReference

for this reference type
in the target VM.

- allLineLocations

```java
List
<
Location
> allLineLocations()
throws
AbsentInformationException
```

Returns a list containing a

Location

object
for each executable source line in this reference type.

This method is equivalent to

allLineLocations(vm.getDefaultStratum(),null)

-
see

allLineLocations(String,String)

for more information.

**Throws:** AbsentInformationException

- if there is no line
number information for this class and there are non-native,
non-abstract executable members of this class.
**Throws:** ClassNotPreparedException

- if this class not yet
been prepared.

- allLineLocations

```java
List
<
Location
> allLineLocations​(
String
stratum,

String
sourceName)
throws
AbsentInformationException
```

Returns a list containing a

Location

object
for each executable source line in this reference type.
Each location maps a source line to a range of code
indices.
The beginning of the range can be determined through

Location.codeIndex()

. The returned list may contain
multiple locations for a particular line number, if the
compiler and/or VM has mapped that line to two or more
disjoint code index ranges. Note that it is possible for
the same source line to represent different code index
ranges in

different

methods.

For arrays (

ArrayType

) and primitive classes, the
returned list is always empty. For interfaces (

InterfaceType

), the returned list will be non-empty only
if the interface has executable code in its class
initialization.

Returned list is for the specified

stratum

(see

Location

for a description of strata).

**Parameters:** stratum

- The stratum to retrieve information from
or

null

for the

defaultStratum()

.
**Parameters:** sourceName

- Return locations only within this
source file or

null

to return locations.
**Returns:** a List of all source line

Location

objects.
**Throws:** AbsentInformationException

- if there is no line
number information for this class and there are non-native,
non-abstract executable members of this class.
Or if

sourceName

is non-

null

and source name information is not present.
**Throws:** ClassNotPreparedException

- if this class not yet
been prepared.
**Since:** 1.4

- locationsOfLine

```java
List
<
Location
> locationsOfLine​(int lineNumber)
throws
AbsentInformationException
```

Returns a List containing all

Location

objects
that map to the given line number.

This method is equivalent to

locationsOfLine(vm.getDefaultStratum(), null,
lineNumber)

-
see

locationsOfLine(java.lang.String,java.lang.String,int)

for more information.

**Parameters:** lineNumber

- the line number
**Returns:** a List of all

Location

objects that map to
the given line.
**Throws:** AbsentInformationException

- if there is no line
number information for this class.
**Throws:** ClassNotPreparedException

- if this class not yet
been prepared.
**See Also:** VirtualMachine.getDefaultStratum()

- locationsOfLine

```java
List
<
Location
> locationsOfLine​(
String
stratum,

String
sourceName,
int lineNumber)
throws
AbsentInformationException
```

Returns a List containing all

Location

objects
that map to the given line number.

For arrays (

ArrayType

) and primitive classes, the
returned list is always empty.
For interfaces (

InterfaceType

), the returned list
will be non-empty only if the interface has executable code
in its class initialization at the specified line number.
An empty list will be returned if there is no executable
code at the specified line number.

Returned list is for the specified

stratum

(see

Location

for a description of strata).

**Parameters:** stratum

- the stratum to use for comparing line number
and source name, or

null

to
use the

defaultStratum()

.
**Parameters:** sourceName

- the source name containing the line
number, or

null

to match
all source names
**Parameters:** lineNumber

- the line number
**Returns:** a List of all

Location

objects that map
to the given line.
**Throws:** AbsentInformationException

- if there is no line
number information for this class.
Or if

sourceName

is non-

null

and source name information is not present.
**Throws:** ClassNotPreparedException

- if this class not yet
been prepared.
**Since:** 1.4

- availableStrata

```java
List
<
String
> availableStrata()
```

Return the available strata for this reference type.

See the

Location

for a description of strata.

**Returns:** List of

java.lang.String

, each
representing a stratum
**Since:** 1.4

- defaultStratum

```java
String
defaultStratum()
```

Returns the default stratum for this reference type.
This value is specified in the class file and cannot
be set by the user. If the class file does not
specify a default stratum the base stratum
(

"Java"

) will be returned.

See the

Location

for a description of strata.

**Since:** 1.4

- instances

```java
List
<
ObjectReference
> instances​(long maxInstances)
```

Returns instances of this ReferenceType.
Only instances that are reachable for the purposes of garbage collection
are returned.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetInstanceInfo()

to determine if the operation is supported.

**Parameters:** maxInstances

- the maximum number of instances to return.
Must be non-negative. If zero, all instances are returned.
**Returns:** a List of

ObjectReference

objects. If there are
no instances of this ReferenceType, a zero-length list is returned.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetInstanceInfo()
**Throws:** IllegalArgumentException

- if maxInstances is less
than zero.
**Since:** 1.6
**See Also:** VirtualMachine.instanceCounts(List)

,

ObjectReference.referringObjects(long)

- equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this ReferenceType for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a

ReferenceType

, if the
ReferenceTypes belong to the same VM, and if they mirror classes
which correspond to the same instance of java.lang.Class in that VM.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this ObjectReference.

**Overrides:** hashCode

in class

Object
**Returns:** the integer hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- majorVersion

```java
int majorVersion()
```

Returns the class major version number, as defined in the class file format
of the Java Virtual Machine Specification.

For arrays (

ArrayType

) and primitive classes,
the returned major version number value is zero.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetClassFileVersion()

to determine if the operation is supported.

**Returns:** the major version number of the class.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetClassFileVersion()
**Since:** 1.6

- minorVersion

```java
int minorVersion()
```

Returns the class minor version number, as defined in the class file format
of the Java Virtual Machine Specification.

For arrays (

ArrayType

) and primitive classes,
the returned minor version number value is zero.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetClassFileVersion()

to determine if the operation is supported.

**Returns:** the minor version number of the class.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetClassFileVersion()
**Since:** 1.6

- constantPoolCount

```java
int constantPoolCount()
```

Returns the number of entries in the constant pool plus one.
This corresponds to the constant_pool_count item of the Class File Format
in the Java Virtual Machine Specification.

For arrays (

ArrayType

) and primitive classes,
the returned constant pool count value is zero.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetConstantPool()

to determine if the operation is supported.

**Returns:** total number of constant pool entries for a class plus one.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetConstantPool()
**Since:** 1.6
**See Also:** constantPool()

- constantPool

```java
byte[] constantPool()
```

Returns the raw bytes of the constant pool in the format of the
constant_pool item of the Class File Format in the Java Virtual
Machine Specification. The format of the constant pool may
differ between versions of the Class File Format, so, the
minor and major class version numbers should be checked for
compatibility.

For arrays (

ArrayType

) and primitive classes,
a zero length byte array is returned.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetConstantPool()

to determine if the operation is supported.

**Returns:** the raw bytes of constant pool.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetConstantPool()
**Since:** 1.6
**See Also:** constantPoolCount()

---

#### Method Detail

name

```java
String
name()
```

Gets the fully qualified name of this type. The returned name
is formatted as it might appear in a Java programming langauge
declaration for objects of this type.

For primitive classes
the returned name is the name of the corresponding primitive
type; for example, "int" is returned as the name of the class
represented by

Integer.TYPE

.

**Specified by:** name

in interface

Type
**Returns:** a string containing the type name.

---

#### name

String

name()

Gets the fully qualified name of this type. The returned name
is formatted as it might appear in a Java programming langauge
declaration for objects of this type.

For primitive classes
the returned name is the name of the corresponding primitive
type; for example, "int" is returned as the name of the class
represented by

Integer.TYPE

.

For primitive classes
the returned name is the name of the corresponding primitive
type; for example, "int" is returned as the name of the class
represented by

Integer.TYPE

.

genericSignature

```java
String
genericSignature()
```

Gets the generic signature for this type if there is one.
Generic signatures are described in the

The Java™ Virtual Machine Specification

.

**Returns:** a string containing the generic signature, or

null

if there is no generic signature.
**Since:** 1.5

---

#### genericSignature

String

genericSignature()

Gets the generic signature for this type if there is one.
Generic signatures are described in the

The Java™ Virtual Machine Specification

.

classLoader

```java
ClassLoaderReference
classLoader()
```

Gets the classloader object which loaded the class corresponding
to this type.

**Returns:** a

ClassLoaderReference

which mirrors the classloader,
or

null

if the class was loaded through the bootstrap class
loader.

---

#### classLoader

ClassLoaderReference

classLoader()

Gets the classloader object which loaded the class corresponding
to this type.

module

```java
default
ModuleReference
module()
```

Gets the module object which contains the class corresponding
to this type.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetModuleInfo()

to determine if the operation is supported.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
**Returns:** a

ModuleReference

which mirrors the module in the target VM.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.
**Since:** 9

---

#### module

default

ModuleReference

module()

Gets the module object which contains the class corresponding
to this type.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetModuleInfo()

to determine if the operation is supported.

sourceName

```java
String
sourceName()
throws
AbsentInformationException
```

Gets an identifying name for the source corresponding to the
declaration of this type. Interpretation of this string is
the responsibility of the source repository mechanism.

The returned name is dependent on VM's default stratum
(

VirtualMachine.getDefaultStratum()

).
In the reference implementation, when using the base stratum,
the returned string is the
unqualified name of the source file containing the declaration
of this type. In other strata the returned source name is
the first source name for that stratum. Since other languages
may have more than one source name for a reference type,
the use of

Location.sourceName()

or

sourceNames(String)

is preferred.

For arrays (

ArrayType

) and primitive classes,
AbsentInformationException is always thrown.

**Returns:** the string source file name
**Throws:** AbsentInformationException

- if the source name is not
known

---

#### sourceName

String

sourceName()
throws

AbsentInformationException

Gets an identifying name for the source corresponding to the
declaration of this type. Interpretation of this string is
the responsibility of the source repository mechanism.

The returned name is dependent on VM's default stratum
(

VirtualMachine.getDefaultStratum()

).
In the reference implementation, when using the base stratum,
the returned string is the
unqualified name of the source file containing the declaration
of this type. In other strata the returned source name is
the first source name for that stratum. Since other languages
may have more than one source name for a reference type,
the use of

Location.sourceName()

or

sourceNames(String)

is preferred.

For arrays (

ArrayType

) and primitive classes,
AbsentInformationException is always thrown.

The returned name is dependent on VM's default stratum
(

VirtualMachine.getDefaultStratum()

).
In the reference implementation, when using the base stratum,
the returned string is the
unqualified name of the source file containing the declaration
of this type. In other strata the returned source name is
the first source name for that stratum. Since other languages
may have more than one source name for a reference type,
the use of

Location.sourceName()

or

sourceNames(String)

is preferred.

For arrays (

ArrayType

) and primitive classes,
AbsentInformationException is always thrown.

For arrays (

ArrayType

) and primitive classes,
AbsentInformationException is always thrown.

sourceNames

```java
List
<
String
> sourceNames​(
String
stratum)
throws
AbsentInformationException
```

Gets the identifying names for all the source corresponding to the
declaration of this type. Interpretation of these names is
the responsibility of the source repository mechanism.

The returned names are for the specified stratum
(see

Location

for a description of strata).
In the reference implementation, when using the Java
programming language stratum,
the returned List contains one element: a String which is the
unqualified name of the source file containing the declaration
of this type. In other strata the returned source names are
all the source names defined for that stratum.

**Parameters:** stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.
**Returns:** a List of String objects each representing a source name
**Throws:** AbsentInformationException

- if the source names are not
known.

For arrays (

ArrayType

) and primitive classes,
AbsentInformationException is always thrown.
**Since:** 1.4

---

#### sourceNames

List

<

String

> sourceNames​(

String

stratum)
throws

AbsentInformationException

Gets the identifying names for all the source corresponding to the
declaration of this type. Interpretation of these names is
the responsibility of the source repository mechanism.

The returned names are for the specified stratum
(see

Location

for a description of strata).
In the reference implementation, when using the Java
programming language stratum,
the returned List contains one element: a String which is the
unqualified name of the source file containing the declaration
of this type. In other strata the returned source names are
all the source names defined for that stratum.

The returned names are for the specified stratum
(see

Location

for a description of strata).
In the reference implementation, when using the Java
programming language stratum,
the returned List contains one element: a String which is the
unqualified name of the source file containing the declaration
of this type. In other strata the returned source names are
all the source names defined for that stratum.

For arrays (

ArrayType

) and primitive classes,
AbsentInformationException is always thrown.

sourcePaths

```java
List
<
String
> sourcePaths​(
String
stratum)
throws
AbsentInformationException
```

Gets the paths to the source corresponding to the
declaration of this type. Interpretation of these paths is
the responsibility of the source repository mechanism.

The returned paths are for the specified stratum
(see

Location

for a description of strata).
In the reference implementation, for strata which
do not explicitly specify source path (the Java
programming language stratum never does), the returned
strings are the

sourceNames(String)

prefixed by
the package name of this ReferenceType
converted to a platform dependent path.
For example, on a Windows platform,

java.lang.Thread

would return a List containing one element:

"java\lang\Thread.java"

.

**Parameters:** stratum

- The stratum to retrieve information from
or

null

for the declaring type's
default stratum.
**Returns:** a List of String objects each representing a source path
**Throws:** AbsentInformationException

- if the source names are not
known.

For arrays (

ArrayType

) and primitive classes,
AbsentInformationException is always thrown.
**Since:** 1.4

---

#### sourcePaths

List

<

String

> sourcePaths​(

String

stratum)
throws

AbsentInformationException

Gets the paths to the source corresponding to the
declaration of this type. Interpretation of these paths is
the responsibility of the source repository mechanism.

The returned paths are for the specified stratum
(see

Location

for a description of strata).
In the reference implementation, for strata which
do not explicitly specify source path (the Java
programming language stratum never does), the returned
strings are the

sourceNames(String)

prefixed by
the package name of this ReferenceType
converted to a platform dependent path.
For example, on a Windows platform,

java.lang.Thread

would return a List containing one element:

"java\lang\Thread.java"

.

The returned paths are for the specified stratum
(see

Location

for a description of strata).
In the reference implementation, for strata which
do not explicitly specify source path (the Java
programming language stratum never does), the returned
strings are the

sourceNames(String)

prefixed by
the package name of this ReferenceType
converted to a platform dependent path.
For example, on a Windows platform,

java.lang.Thread

would return a List containing one element:

"java\lang\Thread.java"

.

For arrays (

ArrayType

) and primitive classes,
AbsentInformationException is always thrown.

sourceDebugExtension

```java
String
sourceDebugExtension()
throws
AbsentInformationException
```

Get the source debug extension of this type.

Not all target virtual machines support this operation.
Use

canGetSourceDebugExtension()

to determine if the operation is supported.

**Returns:** as a string the source debug extension attribute
**Throws:** AbsentInformationException

- if the extension is not
specified
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetSourceDebugExtension()

,

---

#### sourceDebugExtension

String

sourceDebugExtension()
throws

AbsentInformationException

Get the source debug extension of this type.

Not all target virtual machines support this operation.
Use

canGetSourceDebugExtension()

to determine if the operation is supported.

Not all target virtual machines support this operation.
Use

canGetSourceDebugExtension()

to determine if the operation is supported.

isStatic

```java
boolean isStatic()
```

Determines if this type was declared static. Only nested types,
can be declared static, so

false

is returned
for any package-level type, array type, or primitive class.

**Returns:** true

if this type is static; false otherwise.

---

#### isStatic

boolean isStatic()

Determines if this type was declared static. Only nested types,
can be declared static, so

false

is returned
for any package-level type, array type, or primitive class.

isAbstract

```java
boolean isAbstract()
```

Determines if this type was declared abstract.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:** true

if this type is abstract; false otherwise.

---

#### isAbstract

boolean isAbstract()

Determines if this type was declared abstract.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

isFinal

```java
boolean isFinal()
```

Determines if this type was declared final.

For arrays (

ArrayType

) and primitive classes,
the return value is always true.

**Returns:** true

if this type is final; false otherwise.

---

#### isFinal

boolean isFinal()

Determines if this type was declared final.

For arrays (

ArrayType

) and primitive classes,
the return value is always true.

For arrays (

ArrayType

) and primitive classes,
the return value is always true.

isPrepared

```java
boolean isPrepared()
```

Determines if this type has been prepared. See the JVM
specification for a definition of class preparation.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:** true

if this type is prepared; false otherwise.

---

#### isPrepared

boolean isPrepared()

Determines if this type has been prepared. See the JVM
specification for a definition of class preparation.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

isVerified

```java
boolean isVerified()
```

Determines if this type has been verified. See the JVM
specification for a definition of class verification.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:** true

if this type is verified; false otherwise.

---

#### isVerified

boolean isVerified()

Determines if this type has been verified. See the JVM
specification for a definition of class verification.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

isInitialized

```java
boolean isInitialized()
```

Determines if this type has been initialized. See the JVM
specification for a definition of class verification.
For

InterfaceType

, this method always returns the
same value as

isPrepared()

.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:** true

if this type is initialized; false otherwise.

---

#### isInitialized

boolean isInitialized()

Determines if this type has been initialized. See the JVM
specification for a definition of class verification.
For

InterfaceType

, this method always returns the
same value as

isPrepared()

.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

failedToInitialize

```java
boolean failedToInitialize()
```

Determines if initialization failed for this class. See the JVM
specification for details on class initialization.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

**Returns:** true

if initialization was attempted and
failed; false otherwise.

---

#### failedToInitialize

boolean failedToInitialize()

Determines if initialization failed for this class. See the JVM
specification for details on class initialization.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

For arrays (

ArrayType

) and primitive classes,
the return value is undefined.

fields

```java
List
<
Field
> fields()
```

Returns a list containing each

Field

declared in this type.
Inherited fields are not included. Any synthetic fields created
by the compiler are included in the list.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a list

Field

objects; the list has length 0
if no fields exist.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

---

#### fields

List

<

Field

> fields()

Returns a list containing each

Field

declared in this type.
Inherited fields are not included. Any synthetic fields created
by the compiler are included in the list.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

visibleFields

```java
List
<
Field
> visibleFields()
```

Returns a list containing each unhidden and unambiguous

Field

in this type.
Each field that can be accessed from the class
or its instances with its simple name is included. Fields that
are ambiguously multiply inherited or fields that are hidden by
fields with the same name in a more recently inherited class
cannot be accessed
by their simple names and are not included in the returned
list. All other inherited fields are included.
See JLS section 8.3 for details.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a List of

Field

objects; the list has length
0 if no visible fields exist.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

---

#### visibleFields

List

<

Field

> visibleFields()

Returns a list containing each unhidden and unambiguous

Field

in this type.
Each field that can be accessed from the class
or its instances with its simple name is included. Fields that
are ambiguously multiply inherited or fields that are hidden by
fields with the same name in a more recently inherited class
cannot be accessed
by their simple names and are not included in the returned
list. All other inherited fields are included.
See JLS section 8.3 for details.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

allFields

```java
List
<
Field
> allFields()
```

Returns a list containing each

Field

declared in this type,
and its superclasses, implemented interfaces, and/or superinterfaces.
All declared and inherited
fields are included, regardless of whether they are hidden or
multiply inherited.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a List of

Field

objects; the list has length
0 if no fields exist.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

---

#### allFields

List

<

Field

> allFields()

Returns a list containing each

Field

declared in this type,
and its superclasses, implemented interfaces, and/or superinterfaces.
All declared and inherited
fields are included, regardless of whether they are hidden or
multiply inherited.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

fieldByName

```java
Field
fieldByName​(
String
fieldName)
```

Finds the visible

Field

with the given
non-ambiguous name. This method follows the
inheritance rules specified in the JLS (8.3.3) to determine
visibility.

For arrays (

ArrayType

) and primitive classes, the returned
value is always null.

**Parameters:** fieldName

- a String containing the name of desired field.
**Returns:** a

Field

object which mirrors the found field, or
null if there is no field with the given name or if the given
name is ambiguous.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

---

#### fieldByName

Field

fieldByName​(

String

fieldName)

Finds the visible

Field

with the given
non-ambiguous name. This method follows the
inheritance rules specified in the JLS (8.3.3) to determine
visibility.

For arrays (

ArrayType

) and primitive classes, the returned
value is always null.

For arrays (

ArrayType

) and primitive classes, the returned
value is always null.

methods

```java
List
<
Method
> methods()
```

Returns a list containing each

Method

declared
directly in this type.
Inherited methods are not included. Constructors,
the initialization method if any, and any synthetic methods created
by the compiler are included in the list.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a list

Method

objects; the list has length 0
if no methods exist.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

---

#### methods

List

<

Method

> methods()

Returns a list containing each

Method

declared
directly in this type.
Inherited methods are not included. Constructors,
the initialization method if any, and any synthetic methods created
by the compiler are included in the list.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

visibleMethods

```java
List
<
Method
> visibleMethods()
```

Returns a list containing each

Method

declared or inherited by this type. Methods from superclasses
or superinterfaces that that have been hidden or overridden
are not included.

Note that despite this exclusion, multiple inherited methods
with the same signature can be present in the returned list, but
at most one can be a member of a

ClassType

.
See JLS section 8.4.6 for details.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a List of

Method

objects; the list has length
0 if no visible methods exist.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

---

#### visibleMethods

List

<

Method

> visibleMethods()

Returns a list containing each

Method

declared or inherited by this type. Methods from superclasses
or superinterfaces that that have been hidden or overridden
are not included.

Note that despite this exclusion, multiple inherited methods
with the same signature can be present in the returned list, but
at most one can be a member of a

ClassType

.
See JLS section 8.4.6 for details.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

Note that despite this exclusion, multiple inherited methods
with the same signature can be present in the returned list, but
at most one can be a member of a

ClassType

.
See JLS section 8.4.6 for details.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

allMethods

```java
List
<
Method
> allMethods()
```

Returns a list containing each

Method

declared in this type,
and its superclasses, implemented interfaces, and/or superinterfaces.
All declared and inherited
methods are included, regardless of whether they are hidden or
overridden.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a List of

Method

objects; the list has length
0 if no methods exist.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

---

#### allMethods

List

<

Method

> allMethods()

Returns a list containing each

Method

declared in this type,
and its superclasses, implemented interfaces, and/or superinterfaces.
All declared and inherited
methods are included, regardless of whether they are hidden or
overridden.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

methodsByName

```java
List
<
Method
> methodsByName​(
String
name)
```

Returns a List containing each visible

Method

that
has the given name. This is most commonly used to
find overloaded methods.

Overridden and hidden methods are not included.
See JLS (8.4.6) for details.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Parameters:** name

- the name of the method to find.
**Returns:** a List of

Method

objects that match the given
name; the list has length 0 if no matching methods are found.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

---

#### methodsByName

List

<

Method

> methodsByName​(

String

name)

Returns a List containing each visible

Method

that
has the given name. This is most commonly used to
find overloaded methods.

Overridden and hidden methods are not included.
See JLS (8.4.6) for details.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

Overridden and hidden methods are not included.
See JLS (8.4.6) for details.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

methodsByName

```java
List
<
Method
> methodsByName​(
String
name,

String
signature)
```

Returns a List containing each visible

Method

that
has the given name and signature.
The signature string is the
JNI signature for the target method:

- ()V

([Ljava/lang/String;)V

(IIII)Z

This method follows the inheritance rules specified
in the JLS (8.4.6) to determine visibility.

At most one method in the list is a concrete method and a
component of

ClassType

; any other methods in the list
are abstract. Use

ClassType.concreteMethodByName(java.lang.String, java.lang.String)

to
retrieve only the matching concrete method.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Parameters:** name

- the name of the method to find.
**Parameters:** signature

- the signature of the method to find
**Returns:** a List of

Method

objects that match the given
name and signature; the list has length 0 if no matching methods
are found.
**Throws:** ClassNotPreparedException

- if this class not yet been
prepared.

---

#### methodsByName

List

<

Method

> methodsByName​(

String

name,

String

signature)

Returns a List containing each visible

Method

that
has the given name and signature.
The signature string is the
JNI signature for the target method:

- ()V

([Ljava/lang/String;)V

(IIII)Z

This method follows the inheritance rules specified
in the JLS (8.4.6) to determine visibility.

At most one method in the list is a concrete method and a
component of

ClassType

; any other methods in the list
are abstract. Use

ClassType.concreteMethodByName(java.lang.String, java.lang.String)

to
retrieve only the matching concrete method.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

()V

([Ljava/lang/String;)V

(IIII)Z

At most one method in the list is a concrete method and a
component of

ClassType

; any other methods in the list
are abstract. Use

ClassType.concreteMethodByName(java.lang.String, java.lang.String)

to
retrieve only the matching concrete method.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

nestedTypes

```java
List
<
ReferenceType
> nestedTypes()
```

Returns a List containing

ReferenceType

objects that are
declared within this type and are currently loaded into the Virtual
Machine. Both static nested types and non-static nested
types (that is, inner types) are included. Local inner types
(declared within a code block somewhere in this reference type) are
also included in the returned list.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

**Returns:** a List of nested

ReferenceType

objects; the list
has 0 length if there are no nested types.

---

#### nestedTypes

List

<

ReferenceType

> nestedTypes()

Returns a List containing

ReferenceType

objects that are
declared within this type and are currently loaded into the Virtual
Machine. Both static nested types and non-static nested
types (that is, inner types) are included. Local inner types
(declared within a code block somewhere in this reference type) are
also included in the returned list.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

For arrays (

ArrayType

) and primitive classes, the returned
list is always empty.

getValue

```java
Value
getValue​(
Field
field)
```

Gets the

Value

of a given static

Field

in this type.
The Field must be valid for this type;
that is, it must be declared in this type, a superclass, a
superinterface, or an implemented interface.

**Parameters:** field

- the field containing the requested value
**Returns:** the

Value

of the instance field.
**Throws:** IllegalArgumentException

- if the field is not valid for
this object's class.

---

#### getValue

Value

getValue​(

Field

field)

Gets the

Value

of a given static

Field

in this type.
The Field must be valid for this type;
that is, it must be declared in this type, a superclass, a
superinterface, or an implemented interface.

getValues

```java
Map
<
Field
,​
Value
> getValues​(
List
<? extends
Field
> fields)
```

Returns a map containing the

Value

of each
static

Field

in the given list.
The Fields must be valid for this type;
that is, they must be declared in this type, a superclass, a
superinterface, or an implemented interface.

**Parameters:** fields

- a list of

Field

objects containing the
requested values.
**Returns:** a Map of the requested

Field

objects with
their

Value

.
**Throws:** IllegalArgumentException

- if any field is not valid for
this object's class.
**Throws:** VMMismatchException

- if a

Mirror

argument and this mirror
do not belong to the same

VirtualMachine

.

---

#### getValues

Map

<

Field

,​

Value

> getValues​(

List

<? extends

Field

> fields)

Returns a map containing the

Value

of each
static

Field

in the given list.
The Fields must be valid for this type;
that is, they must be declared in this type, a superclass, a
superinterface, or an implemented interface.

classObject

```java
ClassObjectReference
classObject()
```

Returns the class object that corresponds to this type in the
target VM. The VM creates class objects for every kind of
ReferenceType: classes, interfaces, and array types.

**Returns:** the

ClassObjectReference

for this reference type
in the target VM.

---

#### classObject

ClassObjectReference

classObject()

Returns the class object that corresponds to this type in the
target VM. The VM creates class objects for every kind of
ReferenceType: classes, interfaces, and array types.

allLineLocations

```java
List
<
Location
> allLineLocations()
throws
AbsentInformationException
```

Returns a list containing a

Location

object
for each executable source line in this reference type.

This method is equivalent to

allLineLocations(vm.getDefaultStratum(),null)

-
see

allLineLocations(String,String)

for more information.

**Throws:** AbsentInformationException

- if there is no line
number information for this class and there are non-native,
non-abstract executable members of this class.
**Throws:** ClassNotPreparedException

- if this class not yet
been prepared.

---

#### allLineLocations

List

<

Location

> allLineLocations()
throws

AbsentInformationException

Returns a list containing a

Location

object
for each executable source line in this reference type.

This method is equivalent to

allLineLocations(vm.getDefaultStratum(),null)

-
see

allLineLocations(String,String)

for more information.

This method is equivalent to

allLineLocations(vm.getDefaultStratum(),null)

-
see

allLineLocations(String,String)

for more information.

allLineLocations

```java
List
<
Location
> allLineLocations​(
String
stratum,

String
sourceName)
throws
AbsentInformationException
```

Returns a list containing a

Location

object
for each executable source line in this reference type.
Each location maps a source line to a range of code
indices.
The beginning of the range can be determined through

Location.codeIndex()

. The returned list may contain
multiple locations for a particular line number, if the
compiler and/or VM has mapped that line to two or more
disjoint code index ranges. Note that it is possible for
the same source line to represent different code index
ranges in

different

methods.

For arrays (

ArrayType

) and primitive classes, the
returned list is always empty. For interfaces (

InterfaceType

), the returned list will be non-empty only
if the interface has executable code in its class
initialization.

Returned list is for the specified

stratum

(see

Location

for a description of strata).

**Parameters:** stratum

- The stratum to retrieve information from
or

null

for the

defaultStratum()

.
**Parameters:** sourceName

- Return locations only within this
source file or

null

to return locations.
**Returns:** a List of all source line

Location

objects.
**Throws:** AbsentInformationException

- if there is no line
number information for this class and there are non-native,
non-abstract executable members of this class.
Or if

sourceName

is non-

null

and source name information is not present.
**Throws:** ClassNotPreparedException

- if this class not yet
been prepared.
**Since:** 1.4

---

#### allLineLocations

List

<

Location

> allLineLocations​(

String

stratum,

String

sourceName)
throws

AbsentInformationException

Returns a list containing a

Location

object
for each executable source line in this reference type.
Each location maps a source line to a range of code
indices.
The beginning of the range can be determined through

Location.codeIndex()

. The returned list may contain
multiple locations for a particular line number, if the
compiler and/or VM has mapped that line to two or more
disjoint code index ranges. Note that it is possible for
the same source line to represent different code index
ranges in

different

methods.

For arrays (

ArrayType

) and primitive classes, the
returned list is always empty. For interfaces (

InterfaceType

), the returned list will be non-empty only
if the interface has executable code in its class
initialization.

Returned list is for the specified

stratum

(see

Location

for a description of strata).

For arrays (

ArrayType

) and primitive classes, the
returned list is always empty. For interfaces (

InterfaceType

), the returned list will be non-empty only
if the interface has executable code in its class
initialization.

Returned list is for the specified

stratum

(see

Location

for a description of strata).

Returned list is for the specified

stratum

(see

Location

for a description of strata).

locationsOfLine

```java
List
<
Location
> locationsOfLine​(int lineNumber)
throws
AbsentInformationException
```

Returns a List containing all

Location

objects
that map to the given line number.

This method is equivalent to

locationsOfLine(vm.getDefaultStratum(), null,
lineNumber)

-
see

locationsOfLine(java.lang.String,java.lang.String,int)

for more information.

**Parameters:** lineNumber

- the line number
**Returns:** a List of all

Location

objects that map to
the given line.
**Throws:** AbsentInformationException

- if there is no line
number information for this class.
**Throws:** ClassNotPreparedException

- if this class not yet
been prepared.
**See Also:** VirtualMachine.getDefaultStratum()

---

#### locationsOfLine

List

<

Location

> locationsOfLine​(int lineNumber)
throws

AbsentInformationException

Returns a List containing all

Location

objects
that map to the given line number.

This method is equivalent to

locationsOfLine(vm.getDefaultStratum(), null,
lineNumber)

-
see

locationsOfLine(java.lang.String,java.lang.String,int)

for more information.

This method is equivalent to

locationsOfLine(vm.getDefaultStratum(), null,
lineNumber)

-
see

locationsOfLine(java.lang.String,java.lang.String,int)

for more information.

locationsOfLine

```java
List
<
Location
> locationsOfLine​(
String
stratum,

String
sourceName,
int lineNumber)
throws
AbsentInformationException
```

Returns a List containing all

Location

objects
that map to the given line number.

For arrays (

ArrayType

) and primitive classes, the
returned list is always empty.
For interfaces (

InterfaceType

), the returned list
will be non-empty only if the interface has executable code
in its class initialization at the specified line number.
An empty list will be returned if there is no executable
code at the specified line number.

Returned list is for the specified

stratum

(see

Location

for a description of strata).

**Parameters:** stratum

- the stratum to use for comparing line number
and source name, or

null

to
use the

defaultStratum()

.
**Parameters:** sourceName

- the source name containing the line
number, or

null

to match
all source names
**Parameters:** lineNumber

- the line number
**Returns:** a List of all

Location

objects that map
to the given line.
**Throws:** AbsentInformationException

- if there is no line
number information for this class.
Or if

sourceName

is non-

null

and source name information is not present.
**Throws:** ClassNotPreparedException

- if this class not yet
been prepared.
**Since:** 1.4

---

#### locationsOfLine

List

<

Location

> locationsOfLine​(

String

stratum,

String

sourceName,
int lineNumber)
throws

AbsentInformationException

Returns a List containing all

Location

objects
that map to the given line number.

For arrays (

ArrayType

) and primitive classes, the
returned list is always empty.
For interfaces (

InterfaceType

), the returned list
will be non-empty only if the interface has executable code
in its class initialization at the specified line number.
An empty list will be returned if there is no executable
code at the specified line number.

Returned list is for the specified

stratum

(see

Location

for a description of strata).

For arrays (

ArrayType

) and primitive classes, the
returned list is always empty.
For interfaces (

InterfaceType

), the returned list
will be non-empty only if the interface has executable code
in its class initialization at the specified line number.
An empty list will be returned if there is no executable
code at the specified line number.

Returned list is for the specified

stratum

(see

Location

for a description of strata).

Returned list is for the specified

stratum

(see

Location

for a description of strata).

availableStrata

```java
List
<
String
> availableStrata()
```

Return the available strata for this reference type.

See the

Location

for a description of strata.

**Returns:** List of

java.lang.String

, each
representing a stratum
**Since:** 1.4

---

#### availableStrata

List

<

String

> availableStrata()

Return the available strata for this reference type.

See the

Location

for a description of strata.

See the

Location

for a description of strata.

defaultStratum

```java
String
defaultStratum()
```

Returns the default stratum for this reference type.
This value is specified in the class file and cannot
be set by the user. If the class file does not
specify a default stratum the base stratum
(

"Java"

) will be returned.

See the

Location

for a description of strata.

**Since:** 1.4

---

#### defaultStratum

String

defaultStratum()

Returns the default stratum for this reference type.
This value is specified in the class file and cannot
be set by the user. If the class file does not
specify a default stratum the base stratum
(

"Java"

) will be returned.

See the

Location

for a description of strata.

See the

Location

for a description of strata.

instances

```java
List
<
ObjectReference
> instances​(long maxInstances)
```

Returns instances of this ReferenceType.
Only instances that are reachable for the purposes of garbage collection
are returned.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetInstanceInfo()

to determine if the operation is supported.

**Parameters:** maxInstances

- the maximum number of instances to return.
Must be non-negative. If zero, all instances are returned.
**Returns:** a List of

ObjectReference

objects. If there are
no instances of this ReferenceType, a zero-length list is returned.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetInstanceInfo()
**Throws:** IllegalArgumentException

- if maxInstances is less
than zero.
**Since:** 1.6
**See Also:** VirtualMachine.instanceCounts(List)

,

ObjectReference.referringObjects(long)

---

#### instances

List

<

ObjectReference

> instances​(long maxInstances)

Returns instances of this ReferenceType.
Only instances that are reachable for the purposes of garbage collection
are returned.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetInstanceInfo()

to determine if the operation is supported.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetInstanceInfo()

to determine if the operation is supported.

equals

```java
boolean equals​(
Object
obj)
```

Compares the specified Object with this ReferenceType for equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the Object is a

ReferenceType

, if the
ReferenceTypes belong to the same VM, and if they mirror classes
which correspond to the same instance of java.lang.Class in that VM.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

boolean equals​(

Object

obj)

Compares the specified Object with this ReferenceType for equality.

hashCode

```java
int hashCode()
```

Returns the hash code value for this ObjectReference.

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

Returns the hash code value for this ObjectReference.

majorVersion

```java
int majorVersion()
```

Returns the class major version number, as defined in the class file format
of the Java Virtual Machine Specification.

For arrays (

ArrayType

) and primitive classes,
the returned major version number value is zero.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetClassFileVersion()

to determine if the operation is supported.

**Returns:** the major version number of the class.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetClassFileVersion()
**Since:** 1.6

---

#### majorVersion

int majorVersion()

Returns the class major version number, as defined in the class file format
of the Java Virtual Machine Specification.

For arrays (

ArrayType

) and primitive classes,
the returned major version number value is zero.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetClassFileVersion()

to determine if the operation is supported.

minorVersion

```java
int minorVersion()
```

Returns the class minor version number, as defined in the class file format
of the Java Virtual Machine Specification.

For arrays (

ArrayType

) and primitive classes,
the returned minor version number value is zero.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetClassFileVersion()

to determine if the operation is supported.

**Returns:** the minor version number of the class.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetClassFileVersion()
**Since:** 1.6

---

#### minorVersion

int minorVersion()

Returns the class minor version number, as defined in the class file format
of the Java Virtual Machine Specification.

For arrays (

ArrayType

) and primitive classes,
the returned minor version number value is zero.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetClassFileVersion()

to determine if the operation is supported.

constantPoolCount

```java
int constantPoolCount()
```

Returns the number of entries in the constant pool plus one.
This corresponds to the constant_pool_count item of the Class File Format
in the Java Virtual Machine Specification.

For arrays (

ArrayType

) and primitive classes,
the returned constant pool count value is zero.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetConstantPool()

to determine if the operation is supported.

**Returns:** total number of constant pool entries for a class plus one.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetConstantPool()
**Since:** 1.6
**See Also:** constantPool()

---

#### constantPoolCount

int constantPoolCount()

Returns the number of entries in the constant pool plus one.
This corresponds to the constant_pool_count item of the Class File Format
in the Java Virtual Machine Specification.

For arrays (

ArrayType

) and primitive classes,
the returned constant pool count value is zero.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetConstantPool()

to determine if the operation is supported.

constantPool

```java
byte[] constantPool()
```

Returns the raw bytes of the constant pool in the format of the
constant_pool item of the Class File Format in the Java Virtual
Machine Specification. The format of the constant pool may
differ between versions of the Class File Format, so, the
minor and major class version numbers should be checked for
compatibility.

For arrays (

ArrayType

) and primitive classes,
a zero length byte array is returned.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetConstantPool()

to determine if the operation is supported.

**Returns:** the raw bytes of constant pool.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetConstantPool()
**Since:** 1.6
**See Also:** constantPoolCount()

---

#### constantPool

byte[] constantPool()

Returns the raw bytes of the constant pool in the format of the
constant_pool item of the Class File Format in the Java Virtual
Machine Specification. The format of the constant pool may
differ between versions of the Class File Format, so, the
minor and major class version numbers should be checked for
compatibility.

For arrays (

ArrayType

) and primitive classes,
a zero length byte array is returned.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetConstantPool()

to determine if the operation is supported.

---

