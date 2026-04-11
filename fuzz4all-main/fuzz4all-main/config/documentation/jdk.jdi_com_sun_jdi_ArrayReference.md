# Interface ArrayReference

**Source:** `jdk.jdi\com\sun\jdi\ArrayReference.html`

### Class Description

```java
public interface
ArrayReference

extends
ObjectReference
```

Provides access to an array object and its components in the target VM.
Each array component is mirrored by a

Value

object.
The array components, in aggregate, are placed in

List

objects instead of arrays for consistency with the rest of the API and
for interoperability with other APIs.

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

#### int length()

Returns the number of components in this array.

**Returns:**
- the integer count of components in this array.

---

#### Value
getValue​(int index)

Returns an array component value.

**Parameters:**
- index

- the index of the component to retrieve

**Returns:**
- the

Value

at the given index.

**Throws:**
- IndexOutOfBoundsException

- if

index

is outside the range of this array,
that is, if either of the following are true:

```java
index
< 0

index
>=
length()
```

---

#### List
<
Value
> getValues()

Returns all of the components in this array.

**Returns:**
- a list of

Value

objects, one for each array
component ordered by array index. For zero length arrays,
an empty list is returned.

---

#### List
<
Value
> getValues​(int index,
int length)

Returns a range of array components.

**Parameters:**
- index

- the index of the first component to retrieve
- length

- the number of components to retrieve, or -1 to
retrieve all components to the end of this array.

**Returns:**
- a list of

Value

objects, one for each requested
array component ordered by array index. When there are
no elements in the specified range (e.g.

length

is zero) an empty list is returned

**Throws:**
- IndexOutOfBoundsException

- if the range
specified with

index

and

length

is not within the range of the array,
that is, if either of the following are true:

```java
index
< 0

index
>
length()
```

or if

length

!= -1

and
either of the following are true:

```java
length
< 0

index
+
length
>
length()
```

---

#### void setValue​(int index,

Value
value)
throws
InvalidTypeException
,

ClassNotLoadedException

Replaces an array component with another value.

Object values must be assignment compatible with the component type
(This implies that the component type must be loaded through the
declaring class's class loader). Primitive values must be
either assignment compatible with the component type or must be
convertible to the component type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

**Parameters:**
- value

- the new value
- index

- the index of the component to set

**Throws:**
- IndexOutOfBoundsException

- if

index

is outside the range of this array,
that is, if either of the following are true:

```java
index
< 0

index
>=
length()
```
- InvalidTypeException

- if the type of

value

is not compatible with the declared type of array components.
- ClassNotLoadedException

- if the array component type
has not yet been loaded
through the appropriate class loader.
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

**See Also:**
- ArrayType.componentType()

---

#### void setValues​(
List
<? extends
Value
> values)
throws
InvalidTypeException
,

ClassNotLoadedException

Replaces all array components with other values. If the given
list is larger in size than the array, the values at the
end of the list are ignored.

Object values must be assignment compatible with the element type
(This implies that the component type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the component type or must be
convertible to the component type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

**Parameters:**
- values

- a list of

Value

objects to be placed
in this array. If

values

.size()

is
less that the length of the array, the first

values

.size()

elements are set.

**Throws:**
- InvalidTypeException

- if any of the
new

values

is not compatible with the declared type of array components.
- ClassNotLoadedException

- if the array component
type has not yet been loaded
through the appropriate class loader.
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

**See Also:**
- ArrayType.componentType()

---

#### void setValues​(int index,

List
<? extends
Value
> values,
int srcIndex,
int length)
throws
InvalidTypeException
,

ClassNotLoadedException

Replaces a range of array components with other values.

Object values must be assignment compatible with the component type
(This implies that the component type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the component type or must be
convertible to the component type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

**Parameters:**
- index

- the index of the first component to set.
- values

- a list of

Value

objects to be placed
in this array.
- srcIndex

- the index of the first source value to use.
- length

- the number of components to set, or -1 to set
all components to the end of this array or the end of

values

(whichever comes first).

**Throws:**
- InvalidTypeException

- if any element of

values

is not compatible with the declared type of array components.
- IndexOutOfBoundsException

- if the
array range specified with

index

and

length

is not within the range of the array,
or if the source range specified with

srcIndex

and

length

is not within

values

,
that is, if any of the following are true:

```java
index
< 0

index
>
length()

srcIndex
< 0

srcIndex
>
values
.size()
```

or if

length

!= -1

and any of the
following are true:

```java
length
< 0

index
+
length
>
length()

srcIndex
+
length
>
values
.size()
```
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
- ClassNotLoadedException

**See Also:**
- ArrayType.componentType()

---

### Additional Sections

#### Interface ArrayReference

**All Superinterfaces:** Mirror

,

ObjectReference

,

Value

```java
public interface
ArrayReference

extends
ObjectReference
```

Provides access to an array object and its components in the target VM.
Each array component is mirrored by a

Value

object.
The array components, in aggregate, are placed in

List

objects instead of arrays for consistency with the rest of the API and
for interoperability with other APIs.

**Since:** 1.3

public interface

ArrayReference

extends

ObjectReference

Provides access to an array object and its components in the target VM.
Each array component is mirrored by a

Value

object.
The array components, in aggregate, are placed in

List

objects instead of arrays for consistency with the rest of the API and
for interoperability with other APIs.

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

Value

getValue

​(int index)

Returns an array component value.

List

<

Value

>

getValues

()

Returns all of the components in this array.

List

<

Value

>

getValues

​(int index,
int length)

Returns a range of array components.

int

length

()

Returns the number of components in this array.

void

setValue

​(int index,

Value

value)

Replaces an array component with another value.

void

setValues

​(int index,

List

<? extends

Value

> values,
int srcIndex,
int length)

Replaces a range of array components with other values.

void

setValues

​(

List

<? extends

Value

> values)

Replaces all array components with other values.

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

Value

getValue

​(int index)

Returns an array component value.

List

<

Value

>

getValues

()

Returns all of the components in this array.

List

<

Value

>

getValues

​(int index,
int length)

Returns a range of array components.

int

length

()

Returns the number of components in this array.

void

setValue

​(int index,

Value

value)

Replaces an array component with another value.

void

setValues

​(int index,

List

<? extends

Value

> values,
int srcIndex,
int length)

Replaces a range of array components with other values.

void

setValues

​(

List

<? extends

Value

> values)

Replaces all array components with other values.

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

Returns an array component value.

Returns all of the components in this array.

Returns a range of array components.

Returns the number of components in this array.

Replaces an array component with another value.

Replaces a range of array components with other values.

Replaces all array components with other values.

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

- length

```java
int length()
```

Returns the number of components in this array.

**Returns:** the integer count of components in this array.

- getValue

```java
Value
getValue​(int index)
```

Returns an array component value.

**Parameters:** index

- the index of the component to retrieve
**Returns:** the

Value

at the given index.
**Throws:** IndexOutOfBoundsException

- if

index

is outside the range of this array,
that is, if either of the following are true:

```java
index
< 0

index
>=
length()
```

- getValues

```java
List
<
Value
> getValues()
```

Returns all of the components in this array.

**Returns:** a list of

Value

objects, one for each array
component ordered by array index. For zero length arrays,
an empty list is returned.

- getValues

```java
List
<
Value
> getValues​(int index,
int length)
```

Returns a range of array components.

**Parameters:** index

- the index of the first component to retrieve
**Parameters:** length

- the number of components to retrieve, or -1 to
retrieve all components to the end of this array.
**Returns:** a list of

Value

objects, one for each requested
array component ordered by array index. When there are
no elements in the specified range (e.g.

length

is zero) an empty list is returned
**Throws:** IndexOutOfBoundsException

- if the range
specified with

index

and

length

is not within the range of the array,
that is, if either of the following are true:

```java
index
< 0

index
>
length()
```

or if

length

!= -1

and
either of the following are true:

```java
length
< 0

index
+
length
>
length()
```

- setValue

```java
void setValue​(int index,

Value
value)
throws
InvalidTypeException
,

ClassNotLoadedException
```

Replaces an array component with another value.

Object values must be assignment compatible with the component type
(This implies that the component type must be loaded through the
declaring class's class loader). Primitive values must be
either assignment compatible with the component type or must be
convertible to the component type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

**Parameters:** value

- the new value
**Parameters:** index

- the index of the component to set
**Throws:** IndexOutOfBoundsException

- if

index

is outside the range of this array,
that is, if either of the following are true:

```java
index
< 0

index
>=
length()
```
**Throws:** InvalidTypeException

- if the type of

value

is not compatible with the declared type of array components.
**Throws:** ClassNotLoadedException

- if the array component type
has not yet been loaded
through the appropriate class loader.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
**See Also:** ArrayType.componentType()

- setValues

```java
void setValues​(
List
<? extends
Value
> values)
throws
InvalidTypeException
,

ClassNotLoadedException
```

Replaces all array components with other values. If the given
list is larger in size than the array, the values at the
end of the list are ignored.

Object values must be assignment compatible with the element type
(This implies that the component type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the component type or must be
convertible to the component type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

**Parameters:** values

- a list of

Value

objects to be placed
in this array. If

values

.size()

is
less that the length of the array, the first

values

.size()

elements are set.
**Throws:** InvalidTypeException

- if any of the
new

values

is not compatible with the declared type of array components.
**Throws:** ClassNotLoadedException

- if the array component
type has not yet been loaded
through the appropriate class loader.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
**See Also:** ArrayType.componentType()

- setValues

```java
void setValues​(int index,

List
<? extends
Value
> values,
int srcIndex,
int length)
throws
InvalidTypeException
,

ClassNotLoadedException
```

Replaces a range of array components with other values.

Object values must be assignment compatible with the component type
(This implies that the component type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the component type or must be
convertible to the component type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

**Parameters:** index

- the index of the first component to set.
**Parameters:** values

- a list of

Value

objects to be placed
in this array.
**Parameters:** srcIndex

- the index of the first source value to use.
**Parameters:** length

- the number of components to set, or -1 to set
all components to the end of this array or the end of

values

(whichever comes first).
**Throws:** InvalidTypeException

- if any element of

values

is not compatible with the declared type of array components.
**Throws:** IndexOutOfBoundsException

- if the
array range specified with

index

and

length

is not within the range of the array,
or if the source range specified with

srcIndex

and

length

is not within

values

,
that is, if any of the following are true:

```java
index
< 0

index
>
length()

srcIndex
< 0

srcIndex
>
values
.size()
```

or if

length

!= -1

and any of the
following are true:

```java
length
< 0

index
+
length
>
length()

srcIndex
+
length
>
values
.size()
```
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
**Throws:** ClassNotLoadedException
**See Also:** ArrayType.componentType()

Method Detail

- length

```java
int length()
```

Returns the number of components in this array.

**Returns:** the integer count of components in this array.

- getValue

```java
Value
getValue​(int index)
```

Returns an array component value.

**Parameters:** index

- the index of the component to retrieve
**Returns:** the

Value

at the given index.
**Throws:** IndexOutOfBoundsException

- if

index

is outside the range of this array,
that is, if either of the following are true:

```java
index
< 0

index
>=
length()
```

- getValues

```java
List
<
Value
> getValues()
```

Returns all of the components in this array.

**Returns:** a list of

Value

objects, one for each array
component ordered by array index. For zero length arrays,
an empty list is returned.

- getValues

```java
List
<
Value
> getValues​(int index,
int length)
```

Returns a range of array components.

**Parameters:** index

- the index of the first component to retrieve
**Parameters:** length

- the number of components to retrieve, or -1 to
retrieve all components to the end of this array.
**Returns:** a list of

Value

objects, one for each requested
array component ordered by array index. When there are
no elements in the specified range (e.g.

length

is zero) an empty list is returned
**Throws:** IndexOutOfBoundsException

- if the range
specified with

index

and

length

is not within the range of the array,
that is, if either of the following are true:

```java
index
< 0

index
>
length()
```

or if

length

!= -1

and
either of the following are true:

```java
length
< 0

index
+
length
>
length()
```

- setValue

```java
void setValue​(int index,

Value
value)
throws
InvalidTypeException
,

ClassNotLoadedException
```

Replaces an array component with another value.

Object values must be assignment compatible with the component type
(This implies that the component type must be loaded through the
declaring class's class loader). Primitive values must be
either assignment compatible with the component type or must be
convertible to the component type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

**Parameters:** value

- the new value
**Parameters:** index

- the index of the component to set
**Throws:** IndexOutOfBoundsException

- if

index

is outside the range of this array,
that is, if either of the following are true:

```java
index
< 0

index
>=
length()
```
**Throws:** InvalidTypeException

- if the type of

value

is not compatible with the declared type of array components.
**Throws:** ClassNotLoadedException

- if the array component type
has not yet been loaded
through the appropriate class loader.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
**See Also:** ArrayType.componentType()

- setValues

```java
void setValues​(
List
<? extends
Value
> values)
throws
InvalidTypeException
,

ClassNotLoadedException
```

Replaces all array components with other values. If the given
list is larger in size than the array, the values at the
end of the list are ignored.

Object values must be assignment compatible with the element type
(This implies that the component type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the component type or must be
convertible to the component type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

**Parameters:** values

- a list of

Value

objects to be placed
in this array. If

values

.size()

is
less that the length of the array, the first

values

.size()

elements are set.
**Throws:** InvalidTypeException

- if any of the
new

values

is not compatible with the declared type of array components.
**Throws:** ClassNotLoadedException

- if the array component
type has not yet been loaded
through the appropriate class loader.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
**See Also:** ArrayType.componentType()

- setValues

```java
void setValues​(int index,

List
<? extends
Value
> values,
int srcIndex,
int length)
throws
InvalidTypeException
,

ClassNotLoadedException
```

Replaces a range of array components with other values.

Object values must be assignment compatible with the component type
(This implies that the component type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the component type or must be
convertible to the component type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

**Parameters:** index

- the index of the first component to set.
**Parameters:** values

- a list of

Value

objects to be placed
in this array.
**Parameters:** srcIndex

- the index of the first source value to use.
**Parameters:** length

- the number of components to set, or -1 to set
all components to the end of this array or the end of

values

(whichever comes first).
**Throws:** InvalidTypeException

- if any element of

values

is not compatible with the declared type of array components.
**Throws:** IndexOutOfBoundsException

- if the
array range specified with

index

and

length

is not within the range of the array,
or if the source range specified with

srcIndex

and

length

is not within

values

,
that is, if any of the following are true:

```java
index
< 0

index
>
length()

srcIndex
< 0

srcIndex
>
values
.size()
```

or if

length

!= -1

and any of the
following are true:

```java
length
< 0

index
+
length
>
length()

srcIndex
+
length
>
values
.size()
```
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
**Throws:** ClassNotLoadedException
**See Also:** ArrayType.componentType()

---

#### Method Detail

length

```java
int length()
```

Returns the number of components in this array.

**Returns:** the integer count of components in this array.

---

#### length

int length()

Returns the number of components in this array.

getValue

```java
Value
getValue​(int index)
```

Returns an array component value.

**Parameters:** index

- the index of the component to retrieve
**Returns:** the

Value

at the given index.
**Throws:** IndexOutOfBoundsException

- if

index

is outside the range of this array,
that is, if either of the following are true:

```java
index
< 0

index
>=
length()
```

---

#### getValue

Value

getValue​(int index)

Returns an array component value.

index

< 0

index

>=

length()

getValues

```java
List
<
Value
> getValues()
```

Returns all of the components in this array.

**Returns:** a list of

Value

objects, one for each array
component ordered by array index. For zero length arrays,
an empty list is returned.

---

#### getValues

List

<

Value

> getValues()

Returns all of the components in this array.

getValues

```java
List
<
Value
> getValues​(int index,
int length)
```

Returns a range of array components.

**Parameters:** index

- the index of the first component to retrieve
**Parameters:** length

- the number of components to retrieve, or -1 to
retrieve all components to the end of this array.
**Returns:** a list of

Value

objects, one for each requested
array component ordered by array index. When there are
no elements in the specified range (e.g.

length

is zero) an empty list is returned
**Throws:** IndexOutOfBoundsException

- if the range
specified with

index

and

length

is not within the range of the array,
that is, if either of the following are true:

```java
index
< 0

index
>
length()
```

or if

length

!= -1

and
either of the following are true:

```java
length
< 0

index
+
length
>
length()
```

---

#### getValues

List

<

Value

> getValues​(int index,
int length)

Returns a range of array components.

index

< 0

index

>

length()

length

< 0

index

+

length

>

length()

setValue

```java
void setValue​(int index,

Value
value)
throws
InvalidTypeException
,

ClassNotLoadedException
```

Replaces an array component with another value.

Object values must be assignment compatible with the component type
(This implies that the component type must be loaded through the
declaring class's class loader). Primitive values must be
either assignment compatible with the component type or must be
convertible to the component type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

**Parameters:** value

- the new value
**Parameters:** index

- the index of the component to set
**Throws:** IndexOutOfBoundsException

- if

index

is outside the range of this array,
that is, if either of the following are true:

```java
index
< 0

index
>=
length()
```
**Throws:** InvalidTypeException

- if the type of

value

is not compatible with the declared type of array components.
**Throws:** ClassNotLoadedException

- if the array component type
has not yet been loaded
through the appropriate class loader.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
**See Also:** ArrayType.componentType()

---

#### setValue

void setValue​(int index,

Value

value)
throws

InvalidTypeException

,

ClassNotLoadedException

Replaces an array component with another value.

Object values must be assignment compatible with the component type
(This implies that the component type must be loaded through the
declaring class's class loader). Primitive values must be
either assignment compatible with the component type or must be
convertible to the component type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

Object values must be assignment compatible with the component type
(This implies that the component type must be loaded through the
declaring class's class loader). Primitive values must be
either assignment compatible with the component type or must be
convertible to the component type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

index

< 0

index

>=

length()

setValues

```java
void setValues​(
List
<? extends
Value
> values)
throws
InvalidTypeException
,

ClassNotLoadedException
```

Replaces all array components with other values. If the given
list is larger in size than the array, the values at the
end of the list are ignored.

Object values must be assignment compatible with the element type
(This implies that the component type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the component type or must be
convertible to the component type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

**Parameters:** values

- a list of

Value

objects to be placed
in this array. If

values

.size()

is
less that the length of the array, the first

values

.size()

elements are set.
**Throws:** InvalidTypeException

- if any of the
new

values

is not compatible with the declared type of array components.
**Throws:** ClassNotLoadedException

- if the array component
type has not yet been loaded
through the appropriate class loader.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
**See Also:** ArrayType.componentType()

---

#### setValues

void setValues​(

List

<? extends

Value

> values)
throws

InvalidTypeException

,

ClassNotLoadedException

Replaces all array components with other values. If the given
list is larger in size than the array, the values at the
end of the list are ignored.

Object values must be assignment compatible with the element type
(This implies that the component type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the component type or must be
convertible to the component type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

Object values must be assignment compatible with the element type
(This implies that the component type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the component type or must be
convertible to the component type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

setValues

```java
void setValues​(int index,

List
<? extends
Value
> values,
int srcIndex,
int length)
throws
InvalidTypeException
,

ClassNotLoadedException
```

Replaces a range of array components with other values.

Object values must be assignment compatible with the component type
(This implies that the component type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the component type or must be
convertible to the component type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

**Parameters:** index

- the index of the first component to set.
**Parameters:** values

- a list of

Value

objects to be placed
in this array.
**Parameters:** srcIndex

- the index of the first source value to use.
**Parameters:** length

- the number of components to set, or -1 to set
all components to the end of this array or the end of

values

(whichever comes first).
**Throws:** InvalidTypeException

- if any element of

values

is not compatible with the declared type of array components.
**Throws:** IndexOutOfBoundsException

- if the
array range specified with

index

and

length

is not within the range of the array,
or if the source range specified with

srcIndex

and

length

is not within

values

,
that is, if any of the following are true:

```java
index
< 0

index
>
length()

srcIndex
< 0

srcIndex
>
values
.size()
```

or if

length

!= -1

and any of the
following are true:

```java
length
< 0

index
+
length
>
length()

srcIndex
+
length
>
values
.size()
```
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
**Throws:** ClassNotLoadedException
**See Also:** ArrayType.componentType()

---

#### setValues

void setValues​(int index,

List

<? extends

Value

> values,
int srcIndex,
int length)
throws

InvalidTypeException

,

ClassNotLoadedException

Replaces a range of array components with other values.

Object values must be assignment compatible with the component type
(This implies that the component type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the component type or must be
convertible to the component type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

Object values must be assignment compatible with the component type
(This implies that the component type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the component type or must be
convertible to the component type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

index

< 0

index

>

length()

srcIndex

< 0

srcIndex

>

values

.size()

length

< 0

index

+

length

>

length()

srcIndex

+

length

>

values

.size()

---

