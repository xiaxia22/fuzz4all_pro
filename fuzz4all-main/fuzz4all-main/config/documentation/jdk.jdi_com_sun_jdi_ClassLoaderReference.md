# Interface ClassLoaderReference

**Source:** `jdk.jdi\com\sun\jdi\ClassLoaderReference.html`

### Class Description

```java
public interface
ClassLoaderReference

extends
ObjectReference
```

A class loader object from the target VM.
A ClassLoaderReference is an

ObjectReference

with additional
access to classloader-specific information from the target VM. Instances
ClassLoaderReference are obtained through calls to

ReferenceType.classLoader()

**All Superinterfaces:** Mirror

,

ObjectReference

,

Value

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### List
<
ReferenceType
> definedClasses()

Returns a list of all loaded classes that were defined by this
class loader. No ordering of this list guaranteed.

The returned list will include reference types
loaded at least to the point of preparation and
types (like array) for which preparation is
not defined.

**Returns:**
- a List of

ReferenceType

objects mirroring types
loaded by this class loader. The list has length 0 if no types
have been defined by this classloader.

---

#### List
<
ReferenceType
> visibleClasses()

Returns a list of all classes for which this class loader has
been recorded as the initiating loader in the target VM.
The list contains ReferenceTypes defined directly by this loader
(as returned by

definedClasses()

) and any types for which
loading was delegated by this class loader to another class loader.

The visible class list has useful properties with respect to
the type namespace. A particular type name will occur at most
once in the list. Each field or variable declared with that
type name in a class defined by
this class loader must be resolved to that single type.

No ordering of the returned list is guaranteed.

See

The Java™ Virtual Machine Specification

,
section 5.3 - Creation and Loading
for more information on the initiating classloader.

Note that unlike

definedClasses()

and

VirtualMachine.allClasses()

,
some of the returned reference types may not be prepared.
Attempts to perform some operations on unprepared reference types
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

**Returns:**
- a List of

ReferenceType

objects mirroring classes
initiated by this class loader. The list has length 0 if no classes
are visible to this classloader.

---

### Additional Sections

#### Interface ClassLoaderReference

**All Superinterfaces:** Mirror

,

ObjectReference

,

Value

```java
public interface
ClassLoaderReference

extends
ObjectReference
```

A class loader object from the target VM.
A ClassLoaderReference is an

ObjectReference

with additional
access to classloader-specific information from the target VM. Instances
ClassLoaderReference are obtained through calls to

ReferenceType.classLoader()

**Since:** 1.3
**See Also:** ObjectReference

public interface

ClassLoaderReference

extends

ObjectReference

A class loader object from the target VM.
A ClassLoaderReference is an

ObjectReference

with additional
access to classloader-specific information from the target VM. Instances
ClassLoaderReference are obtained through calls to

ReferenceType.classLoader()

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface com.sun.jdi.

ObjectReference

INVOKE_NONVIRTUAL

,

INVOKE_SINGLE_THREADED

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<

ReferenceType

>

definedClasses

()

Returns a list of all loaded classes that were defined by this
class loader.

List

<

ReferenceType

>

visibleClasses

()

Returns a list of all classes for which this class loader has
been recorded as the initiating loader in the target VM.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.

ObjectReference

disableCollection

,

enableCollection

,

entryCount

,

equals

,

getValue

,

getValues

,

hashCode

,

invokeMethod

,

isCollected

,

owningThread

,

referenceType

,

referringObjects

,

setValue

,

uniqueID

,

waitingThreads

- Methods declared in interface com.sun.jdi.

Value

type

Field Summary

- Fields declared in interface com.sun.jdi.

ObjectReference

INVOKE_NONVIRTUAL

,

INVOKE_SINGLE_THREADED

---

#### Field Summary

Fields declared in interface com.sun.jdi.

ObjectReference

INVOKE_NONVIRTUAL

,

INVOKE_SINGLE_THREADED

---

#### Fields declared in interface com.sun.jdi. ObjectReference

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<

ReferenceType

>

definedClasses

()

Returns a list of all loaded classes that were defined by this
class loader.

List

<

ReferenceType

>

visibleClasses

()

Returns a list of all classes for which this class loader has
been recorded as the initiating loader in the target VM.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.

ObjectReference

disableCollection

,

enableCollection

,

entryCount

,

equals

,

getValue

,

getValues

,

hashCode

,

invokeMethod

,

isCollected

,

owningThread

,

referenceType

,

referringObjects

,

setValue

,

uniqueID

,

waitingThreads

- Methods declared in interface com.sun.jdi.

Value

type

---

#### Method Summary

Returns a list of all loaded classes that were defined by this
class loader.

Returns a list of all classes for which this class loader has
been recorded as the initiating loader in the target VM.

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

Methods declared in interface com.sun.jdi.

ObjectReference

disableCollection

,

enableCollection

,

entryCount

,

equals

,

getValue

,

getValues

,

hashCode

,

invokeMethod

,

isCollected

,

owningThread

,

referenceType

,

referringObjects

,

setValue

,

uniqueID

,

waitingThreads

---

#### Methods declared in interface com.sun.jdi. ObjectReference

Methods declared in interface com.sun.jdi.

Value

type

---

#### Methods declared in interface com.sun.jdi. Value

============ METHOD DETAIL ==========

- Method Detail

- definedClasses

```java
List
<
ReferenceType
> definedClasses()
```

Returns a list of all loaded classes that were defined by this
class loader. No ordering of this list guaranteed.

The returned list will include reference types
loaded at least to the point of preparation and
types (like array) for which preparation is
not defined.

**Returns:** a List of

ReferenceType

objects mirroring types
loaded by this class loader. The list has length 0 if no types
have been defined by this classloader.

- visibleClasses

```java
List
<
ReferenceType
> visibleClasses()
```

Returns a list of all classes for which this class loader has
been recorded as the initiating loader in the target VM.
The list contains ReferenceTypes defined directly by this loader
(as returned by

definedClasses()

) and any types for which
loading was delegated by this class loader to another class loader.

The visible class list has useful properties with respect to
the type namespace. A particular type name will occur at most
once in the list. Each field or variable declared with that
type name in a class defined by
this class loader must be resolved to that single type.

No ordering of the returned list is guaranteed.

See

The Java™ Virtual Machine Specification

,
section 5.3 - Creation and Loading
for more information on the initiating classloader.

Note that unlike

definedClasses()

and

VirtualMachine.allClasses()

,
some of the returned reference types may not be prepared.
Attempts to perform some operations on unprepared reference types
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

**Returns:** a List of

ReferenceType

objects mirroring classes
initiated by this class loader. The list has length 0 if no classes
are visible to this classloader.

Method Detail

- definedClasses

```java
List
<
ReferenceType
> definedClasses()
```

Returns a list of all loaded classes that were defined by this
class loader. No ordering of this list guaranteed.

The returned list will include reference types
loaded at least to the point of preparation and
types (like array) for which preparation is
not defined.

**Returns:** a List of

ReferenceType

objects mirroring types
loaded by this class loader. The list has length 0 if no types
have been defined by this classloader.

- visibleClasses

```java
List
<
ReferenceType
> visibleClasses()
```

Returns a list of all classes for which this class loader has
been recorded as the initiating loader in the target VM.
The list contains ReferenceTypes defined directly by this loader
(as returned by

definedClasses()

) and any types for which
loading was delegated by this class loader to another class loader.

The visible class list has useful properties with respect to
the type namespace. A particular type name will occur at most
once in the list. Each field or variable declared with that
type name in a class defined by
this class loader must be resolved to that single type.

No ordering of the returned list is guaranteed.

See

The Java™ Virtual Machine Specification

,
section 5.3 - Creation and Loading
for more information on the initiating classloader.

Note that unlike

definedClasses()

and

VirtualMachine.allClasses()

,
some of the returned reference types may not be prepared.
Attempts to perform some operations on unprepared reference types
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

**Returns:** a List of

ReferenceType

objects mirroring classes
initiated by this class loader. The list has length 0 if no classes
are visible to this classloader.

---

#### Method Detail

definedClasses

```java
List
<
ReferenceType
> definedClasses()
```

Returns a list of all loaded classes that were defined by this
class loader. No ordering of this list guaranteed.

The returned list will include reference types
loaded at least to the point of preparation and
types (like array) for which preparation is
not defined.

**Returns:** a List of

ReferenceType

objects mirroring types
loaded by this class loader. The list has length 0 if no types
have been defined by this classloader.

---

#### definedClasses

List

<

ReferenceType

> definedClasses()

Returns a list of all loaded classes that were defined by this
class loader. No ordering of this list guaranteed.

The returned list will include reference types
loaded at least to the point of preparation and
types (like array) for which preparation is
not defined.

The returned list will include reference types
loaded at least to the point of preparation and
types (like array) for which preparation is
not defined.

visibleClasses

```java
List
<
ReferenceType
> visibleClasses()
```

Returns a list of all classes for which this class loader has
been recorded as the initiating loader in the target VM.
The list contains ReferenceTypes defined directly by this loader
(as returned by

definedClasses()

) and any types for which
loading was delegated by this class loader to another class loader.

The visible class list has useful properties with respect to
the type namespace. A particular type name will occur at most
once in the list. Each field or variable declared with that
type name in a class defined by
this class loader must be resolved to that single type.

No ordering of the returned list is guaranteed.

See

The Java™ Virtual Machine Specification

,
section 5.3 - Creation and Loading
for more information on the initiating classloader.

Note that unlike

definedClasses()

and

VirtualMachine.allClasses()

,
some of the returned reference types may not be prepared.
Attempts to perform some operations on unprepared reference types
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

**Returns:** a List of

ReferenceType

objects mirroring classes
initiated by this class loader. The list has length 0 if no classes
are visible to this classloader.

---

#### visibleClasses

List

<

ReferenceType

> visibleClasses()

Returns a list of all classes for which this class loader has
been recorded as the initiating loader in the target VM.
The list contains ReferenceTypes defined directly by this loader
(as returned by

definedClasses()

) and any types for which
loading was delegated by this class loader to another class loader.

The visible class list has useful properties with respect to
the type namespace. A particular type name will occur at most
once in the list. Each field or variable declared with that
type name in a class defined by
this class loader must be resolved to that single type.

No ordering of the returned list is guaranteed.

See

The Java™ Virtual Machine Specification

,
section 5.3 - Creation and Loading
for more information on the initiating classloader.

Note that unlike

definedClasses()

and

VirtualMachine.allClasses()

,
some of the returned reference types may not be prepared.
Attempts to perform some operations on unprepared reference types
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

The visible class list has useful properties with respect to
the type namespace. A particular type name will occur at most
once in the list. Each field or variable declared with that
type name in a class defined by
this class loader must be resolved to that single type.

No ordering of the returned list is guaranteed.

See

The Java™ Virtual Machine Specification

,
section 5.3 - Creation and Loading
for more information on the initiating classloader.

Note that unlike

definedClasses()

and

VirtualMachine.allClasses()

,
some of the returned reference types may not be prepared.
Attempts to perform some operations on unprepared reference types
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

No ordering of the returned list is guaranteed.

See

The Java™ Virtual Machine Specification

,
section 5.3 - Creation and Loading
for more information on the initiating classloader.

Note that unlike

definedClasses()

and

VirtualMachine.allClasses()

,
some of the returned reference types may not be prepared.
Attempts to perform some operations on unprepared reference types
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

See

The Java™ Virtual Machine Specification

,
section 5.3 - Creation and Loading
for more information on the initiating classloader.

Note that unlike

definedClasses()

and

VirtualMachine.allClasses()

,
some of the returned reference types may not be prepared.
Attempts to perform some operations on unprepared reference types
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

Note that unlike

definedClasses()

and

VirtualMachine.allClasses()

,
some of the returned reference types may not be prepared.
Attempts to perform some operations on unprepared reference types
(e.g.

fields()

) will throw
a

ClassNotPreparedException

.
Use

ReferenceType.isPrepared()

to determine if
a reference type is prepared.

---

