# Class ScriptObjectMirror

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\scripting\ScriptObjectMirror.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public final class
ScriptObjectMirror

extends
AbstractJSObject

implements
Bindings
```

Mirror object that wraps a given Nashorn Script object.

**All Implemented Interfaces:** Map

<

String

,​

Object

>

,

Bindings

,

JSObject

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
Object
callMember​(
String
functionName,

Object
... args)

Call member function

**Parameters:**
- functionName

- function name
- args

- arguments

**Returns:**
- return value of function

---

#### public void setIndexedPropertiesToExternalArrayData​(
ByteBuffer
buf)

Nashorn extension: setIndexedPropertiesToExternalArrayData.
set indexed properties be exposed from a given nio ByteBuffer.

**Parameters:**
- buf

- external buffer - should be a nio ByteBuffer

---

#### public boolean delete​(
Object
key)

Delete a property from this object.

**Parameters:**
- key

- the property to be deleted

**Returns:**
- if the delete was successful or not

---

#### public
Object
getProto()

Return the __proto__ of this object.

**Returns:**
- __proto__ object.

---

#### public void setProto​(
Object
proto)

Set the __proto__ of this object.

**Parameters:**
- proto

- new proto for this object

---

#### public
Object
getOwnPropertyDescriptor​(
String
key)

ECMA 8.12.1 [[GetOwnProperty]] (P)

**Parameters:**
- key

- property key

**Returns:**
- Returns the Property Descriptor of the named own property of this
object, or undefined if absent.

---

#### public
String
[] getOwnKeys​(boolean all)

return an array of own property keys associated with the object.

**Parameters:**
- all

- True if to include non-enumerable keys.

**Returns:**
- Array of keys.

---

#### public
ScriptObjectMirror
preventExtensions()

Flag this script object as non extensible

**Returns:**
- the object after being made non extensible

---

#### public boolean isExtensible()

Check if this script object is extensible

**Returns:**
- true if extensible

---

#### public
ScriptObjectMirror
seal()

ECMAScript 15.2.3.8 - seal implementation

**Returns:**
- the sealed script object

---

#### public boolean isSealed()

Check whether this script object is sealed

**Returns:**
- true if sealed

---

#### public
ScriptObjectMirror
freeze()

ECMA 15.2.39 - freeze implementation. Freeze this script object

**Returns:**
- the frozen script object

---

#### public boolean isFrozen()

Check whether this script object is frozen

**Returns:**
- true if frozen

---

#### public static boolean isUndefined​(
Object
obj)

Utility to check if given object is ECMAScript undefined value

**Parameters:**
- obj

- object to check

**Returns:**
- true if 'obj' is ECMAScript undefined value

---

#### public <T> T to​(
Class
<T> type)

Utility to convert this script object to the given type.

**Parameters:**
- type

- destination type to convert to

**Returns:**
- converted object

**Type Parameters:**
- T

- destination type to convert to

---

#### public static
Object
wrap​(
Object
obj,

Object
homeGlobal)

Make a script object mirror on given object if needed.

**Parameters:**
- obj

- object to be wrapped/converted
- homeGlobal

- global to which this object belongs.

**Returns:**
- wrapped/converted object

---

#### public static
Object
wrapAsJSONCompatible​(
Object
obj,

Object
homeGlobal)

Make a script object mirror on given object if needed. The created wrapper will implement
the Java

List

interface if

obj

is a JavaScript

Array

object;
this is compatible with Java JSON libraries expectations. Arrays retrieved through its
properties (transitively) will also implement the list interface.

**Parameters:**
- obj

- object to be wrapped/converted
- homeGlobal

- global to which this object belongs.

**Returns:**
- wrapped/converted object

---

#### public static
Object
unwrap​(
Object
obj,

Object
homeGlobal)

Unwrap a script object mirror if needed.

**Parameters:**
- obj

- object to be unwrapped
- homeGlobal

- global to which this object belongs

**Returns:**
- unwrapped object

---

#### public static
Object
[] wrapArray​(
Object
[] args,

Object
homeGlobal)

Wrap an array of object to script object mirrors if needed.

**Parameters:**
- args

- array to be unwrapped
- homeGlobal

- global to which this object belongs

**Returns:**
- wrapped array

---

#### public static
Object
[] unwrapArray​(
Object
[] args,

Object
homeGlobal)

Unwrap an array of script object mirrors if needed.

**Parameters:**
- args

- array to be unwrapped
- homeGlobal

- global to which this object belongs

**Returns:**
- unwrapped array

---

#### public static boolean identical​(
Object
obj1,

Object
obj2)

Are the given objects mirrors to same underlying object?

**Parameters:**
- obj1

- first object
- obj2

- second object

**Returns:**
- true if obj1 and obj2 are identical script objects or mirrors of it.

---

### Additional Sections

#### Class ScriptObjectMirror

java.lang.Object

- jdk.nashorn.api.scripting.AbstractJSObject
- - jdk.nashorn.api.scripting.ScriptObjectMirror

jdk.nashorn.api.scripting.AbstractJSObject

- jdk.nashorn.api.scripting.ScriptObjectMirror

jdk.nashorn.api.scripting.ScriptObjectMirror

**All Implemented Interfaces:** Map

<

String

,​

Object

>

,

Bindings

,

JSObject

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public final class
ScriptObjectMirror

extends
AbstractJSObject

implements
Bindings
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

Mirror object that wraps a given Nashorn Script object.

**Since:** 1.8u40

@Deprecated

(

since

="11",

forRemoval

=true)
public final class

ScriptObjectMirror

extends

AbstractJSObject

implements

Bindings

Mirror object that wraps a given Nashorn Script object.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface java.util.

Map

Map.Entry

<

K

,​

V

>

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Object

callMember

​(

String

functionName,

Object

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Call member function

boolean

delete

​(

Object

key)

Deprecated, for removal: This API element is subject to removal in a future version.

Delete a property from this object.

ScriptObjectMirror

freeze

()

Deprecated, for removal: This API element is subject to removal in a future version.

ECMA 15.2.39 - freeze implementation.

String

[]

getOwnKeys

​(boolean all)

Deprecated, for removal: This API element is subject to removal in a future version.

return an array of own property keys associated with the object.

Object

getOwnPropertyDescriptor

​(

String

key)

Deprecated, for removal: This API element is subject to removal in a future version.

ECMA 8.12.1 [[GetOwnProperty]] (P)

Object

getProto

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the __proto__ of this object.

static boolean

identical

​(

Object

obj1,

Object

obj2)

Deprecated, for removal: This API element is subject to removal in a future version.

Are the given objects mirrors to same underlying object?

boolean

isExtensible

()

Deprecated, for removal: This API element is subject to removal in a future version.

Check if this script object is extensible

boolean

isFrozen

()

Deprecated, for removal: This API element is subject to removal in a future version.

Check whether this script object is frozen

boolean

isSealed

()

Deprecated, for removal: This API element is subject to removal in a future version.

Check whether this script object is sealed

static boolean

isUndefined

​(

Object

obj)

Deprecated, for removal: This API element is subject to removal in a future version.

Utility to check if given object is ECMAScript undefined value

ScriptObjectMirror

preventExtensions

()

Deprecated, for removal: This API element is subject to removal in a future version.

Flag this script object as non extensible

ScriptObjectMirror

seal

()

Deprecated, for removal: This API element is subject to removal in a future version.

ECMAScript 15.2.3.8 - seal implementation

void

setIndexedPropertiesToExternalArrayData

​(

ByteBuffer

buf)

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn extension: setIndexedPropertiesToExternalArrayData.

void

setProto

​(

Object

proto)

Deprecated, for removal: This API element is subject to removal in a future version.

Set the __proto__ of this object.

<T> T

to

​(

Class

<T> type)

Deprecated, for removal: This API element is subject to removal in a future version.

Utility to convert this script object to the given type.

static

Object

unwrap

​(

Object

obj,

Object

homeGlobal)

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap a script object mirror if needed.

static

Object

[]

unwrapArray

​(

Object

[] args,

Object

homeGlobal)

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap an array of script object mirrors if needed.

static

Object

wrap

​(

Object

obj,

Object

homeGlobal)

Deprecated, for removal: This API element is subject to removal in a future version.

Make a script object mirror on given object if needed.

static

Object

[]

wrapArray

​(

Object

[] args,

Object

homeGlobal)

Deprecated, for removal: This API element is subject to removal in a future version.

Wrap an array of object to script object mirrors if needed.

static

Object

wrapAsJSONCompatible

​(

Object

obj,

Object

homeGlobal)

Deprecated, for removal: This API element is subject to removal in a future version.

Make a script object mirror on given object if needed.

- Methods declared in class jdk.nashorn.api.scripting.

AbstractJSObject

call

,

eval

,

getDefaultValue

,

getMember

,

getSlot

,

hasMember

,

hasSlot

,

isArray

,

isFunction

,

isInstance

,

isStrictFunction

,

keySet

,

newObject

,

removeMember

,

setMember

,

setSlot

,

toNumber

,

values

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

- Methods declared in interface javax.script.

Bindings

containsKey

,

get

,

put

,

putAll

,

remove

- Methods declared in interface jdk.nashorn.api.scripting.

JSObject

getClassName

,

getDefaultValue

,

isInstanceOf

- Methods declared in interface java.util.

Map

clear

,

compute

,

computeIfAbsent

,

computeIfPresent

,

containsValue

,

entrySet

,

equals

,

forEach

,

getOrDefault

,

hashCode

,

isEmpty

,

keySet

,

merge

,

putIfAbsent

,

remove

,

replace

,

replace

,

replaceAll

,

size

,

values

Nested Class Summary

- Nested classes/interfaces declared in interface java.util.

Map

Map.Entry

<

K

,​

V

>

---

#### Nested Class Summary

Nested classes/interfaces declared in interface java.util.

Map

Map.Entry

<

K

,​

V

>

---

#### Nested classes/interfaces declared in interface java.util. Map

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Object

callMember

​(

String

functionName,

Object

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Call member function

boolean

delete

​(

Object

key)

Deprecated, for removal: This API element is subject to removal in a future version.

Delete a property from this object.

ScriptObjectMirror

freeze

()

Deprecated, for removal: This API element is subject to removal in a future version.

ECMA 15.2.39 - freeze implementation.

String

[]

getOwnKeys

​(boolean all)

Deprecated, for removal: This API element is subject to removal in a future version.

return an array of own property keys associated with the object.

Object

getOwnPropertyDescriptor

​(

String

key)

Deprecated, for removal: This API element is subject to removal in a future version.

ECMA 8.12.1 [[GetOwnProperty]] (P)

Object

getProto

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the __proto__ of this object.

static boolean

identical

​(

Object

obj1,

Object

obj2)

Deprecated, for removal: This API element is subject to removal in a future version.

Are the given objects mirrors to same underlying object?

boolean

isExtensible

()

Deprecated, for removal: This API element is subject to removal in a future version.

Check if this script object is extensible

boolean

isFrozen

()

Deprecated, for removal: This API element is subject to removal in a future version.

Check whether this script object is frozen

boolean

isSealed

()

Deprecated, for removal: This API element is subject to removal in a future version.

Check whether this script object is sealed

static boolean

isUndefined

​(

Object

obj)

Deprecated, for removal: This API element is subject to removal in a future version.

Utility to check if given object is ECMAScript undefined value

ScriptObjectMirror

preventExtensions

()

Deprecated, for removal: This API element is subject to removal in a future version.

Flag this script object as non extensible

ScriptObjectMirror

seal

()

Deprecated, for removal: This API element is subject to removal in a future version.

ECMAScript 15.2.3.8 - seal implementation

void

setIndexedPropertiesToExternalArrayData

​(

ByteBuffer

buf)

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn extension: setIndexedPropertiesToExternalArrayData.

void

setProto

​(

Object

proto)

Deprecated, for removal: This API element is subject to removal in a future version.

Set the __proto__ of this object.

<T> T

to

​(

Class

<T> type)

Deprecated, for removal: This API element is subject to removal in a future version.

Utility to convert this script object to the given type.

static

Object

unwrap

​(

Object

obj,

Object

homeGlobal)

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap a script object mirror if needed.

static

Object

[]

unwrapArray

​(

Object

[] args,

Object

homeGlobal)

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap an array of script object mirrors if needed.

static

Object

wrap

​(

Object

obj,

Object

homeGlobal)

Deprecated, for removal: This API element is subject to removal in a future version.

Make a script object mirror on given object if needed.

static

Object

[]

wrapArray

​(

Object

[] args,

Object

homeGlobal)

Deprecated, for removal: This API element is subject to removal in a future version.

Wrap an array of object to script object mirrors if needed.

static

Object

wrapAsJSONCompatible

​(

Object

obj,

Object

homeGlobal)

Deprecated, for removal: This API element is subject to removal in a future version.

Make a script object mirror on given object if needed.

- Methods declared in class jdk.nashorn.api.scripting.

AbstractJSObject

call

,

eval

,

getDefaultValue

,

getMember

,

getSlot

,

hasMember

,

hasSlot

,

isArray

,

isFunction

,

isInstance

,

isStrictFunction

,

keySet

,

newObject

,

removeMember

,

setMember

,

setSlot

,

toNumber

,

values

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

- Methods declared in interface javax.script.

Bindings

containsKey

,

get

,

put

,

putAll

,

remove

- Methods declared in interface jdk.nashorn.api.scripting.

JSObject

getClassName

,

getDefaultValue

,

isInstanceOf

- Methods declared in interface java.util.

Map

clear

,

compute

,

computeIfAbsent

,

computeIfPresent

,

containsValue

,

entrySet

,

equals

,

forEach

,

getOrDefault

,

hashCode

,

isEmpty

,

keySet

,

merge

,

putIfAbsent

,

remove

,

replace

,

replace

,

replaceAll

,

size

,

values

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Call member function

Delete a property from this object.

ECMA 15.2.39 - freeze implementation.

return an array of own property keys associated with the object.

ECMA 8.12.1 [[GetOwnProperty]] (P)

Return the __proto__ of this object.

Are the given objects mirrors to same underlying object?

Check if this script object is extensible

Check whether this script object is frozen

Check whether this script object is sealed

Utility to check if given object is ECMAScript undefined value

Flag this script object as non extensible

ECMAScript 15.2.3.8 - seal implementation

Nashorn extension: setIndexedPropertiesToExternalArrayData.

Set the __proto__ of this object.

Utility to convert this script object to the given type.

Unwrap a script object mirror if needed.

Unwrap an array of script object mirrors if needed.

Make a script object mirror on given object if needed.

Wrap an array of object to script object mirrors if needed.

Methods declared in class jdk.nashorn.api.scripting.

AbstractJSObject

call

,

eval

,

getDefaultValue

,

getMember

,

getSlot

,

hasMember

,

hasSlot

,

isArray

,

isFunction

,

isInstance

,

isStrictFunction

,

keySet

,

newObject

,

removeMember

,

setMember

,

setSlot

,

toNumber

,

values

---

#### Methods declared in class jdk.nashorn.api.scripting. AbstractJSObject

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

Methods declared in interface javax.script.

Bindings

containsKey

,

get

,

put

,

putAll

,

remove

---

#### Methods declared in interface javax.script. Bindings

Methods declared in interface jdk.nashorn.api.scripting.

JSObject

getClassName

,

getDefaultValue

,

isInstanceOf

---

#### Methods declared in interface jdk.nashorn.api.scripting. JSObject

Methods declared in interface java.util.

Map

clear

,

compute

,

computeIfAbsent

,

computeIfPresent

,

containsValue

,

entrySet

,

equals

,

forEach

,

getOrDefault

,

hashCode

,

isEmpty

,

keySet

,

merge

,

putIfAbsent

,

remove

,

replace

,

replace

,

replaceAll

,

size

,

values

---

#### Methods declared in interface java.util. Map

============ METHOD DETAIL ==========

- Method Detail

- callMember

```java
public
Object
callMember​(
String
functionName,

Object
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Call member function

**Parameters:** functionName

- function name
**Parameters:** args

- arguments
**Returns:** return value of function

- setIndexedPropertiesToExternalArrayData

```java
public void setIndexedPropertiesToExternalArrayData​(
ByteBuffer
buf)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn extension: setIndexedPropertiesToExternalArrayData.
set indexed properties be exposed from a given nio ByteBuffer.

**Parameters:** buf

- external buffer - should be a nio ByteBuffer

- delete

```java
public boolean delete​(
Object
key)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Delete a property from this object.

**Parameters:** key

- the property to be deleted
**Returns:** if the delete was successful or not

- getProto

```java
public
Object
getProto()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the __proto__ of this object.

**Returns:** __proto__ object.

- setProto

```java
public void setProto​(
Object
proto)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set the __proto__ of this object.

**Parameters:** proto

- new proto for this object

- getOwnPropertyDescriptor

```java
public
Object
getOwnPropertyDescriptor​(
String
key)
```

Deprecated, for removal: This API element is subject to removal in a future version.

ECMA 8.12.1 [[GetOwnProperty]] (P)

**Parameters:** key

- property key
**Returns:** Returns the Property Descriptor of the named own property of this
object, or undefined if absent.

- getOwnKeys

```java
public
String
[] getOwnKeys​(boolean all)
```

Deprecated, for removal: This API element is subject to removal in a future version.

return an array of own property keys associated with the object.

**Parameters:** all

- True if to include non-enumerable keys.
**Returns:** Array of keys.

- preventExtensions

```java
public
ScriptObjectMirror
preventExtensions()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Flag this script object as non extensible

**Returns:** the object after being made non extensible

- isExtensible

```java
public boolean isExtensible()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Check if this script object is extensible

**Returns:** true if extensible

- seal

```java
public
ScriptObjectMirror
seal()
```

Deprecated, for removal: This API element is subject to removal in a future version.

ECMAScript 15.2.3.8 - seal implementation

**Returns:** the sealed script object

- isSealed

```java
public boolean isSealed()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Check whether this script object is sealed

**Returns:** true if sealed

- freeze

```java
public
ScriptObjectMirror
freeze()
```

Deprecated, for removal: This API element is subject to removal in a future version.

ECMA 15.2.39 - freeze implementation. Freeze this script object

**Returns:** the frozen script object

- isFrozen

```java
public boolean isFrozen()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Check whether this script object is frozen

**Returns:** true if frozen

- isUndefined

```java
public static boolean isUndefined​(
Object
obj)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Utility to check if given object is ECMAScript undefined value

**Parameters:** obj

- object to check
**Returns:** true if 'obj' is ECMAScript undefined value

- to

```java
public <T> T to​(
Class
<T> type)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Utility to convert this script object to the given type.

**Type Parameters:** T

- destination type to convert to
**Parameters:** type

- destination type to convert to
**Returns:** converted object

- wrap

```java
public static
Object
wrap​(
Object
obj,

Object
homeGlobal)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Make a script object mirror on given object if needed.

**Parameters:** obj

- object to be wrapped/converted
**Parameters:** homeGlobal

- global to which this object belongs.
**Returns:** wrapped/converted object

- wrapAsJSONCompatible

```java
public static
Object
wrapAsJSONCompatible​(
Object
obj,

Object
homeGlobal)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Make a script object mirror on given object if needed. The created wrapper will implement
the Java

List

interface if

obj

is a JavaScript

Array

object;
this is compatible with Java JSON libraries expectations. Arrays retrieved through its
properties (transitively) will also implement the list interface.

**Parameters:** obj

- object to be wrapped/converted
**Parameters:** homeGlobal

- global to which this object belongs.
**Returns:** wrapped/converted object

- unwrap

```java
public static
Object
unwrap​(
Object
obj,

Object
homeGlobal)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap a script object mirror if needed.

**Parameters:** obj

- object to be unwrapped
**Parameters:** homeGlobal

- global to which this object belongs
**Returns:** unwrapped object

- wrapArray

```java
public static
Object
[] wrapArray​(
Object
[] args,

Object
homeGlobal)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Wrap an array of object to script object mirrors if needed.

**Parameters:** args

- array to be unwrapped
**Parameters:** homeGlobal

- global to which this object belongs
**Returns:** wrapped array

- unwrapArray

```java
public static
Object
[] unwrapArray​(
Object
[] args,

Object
homeGlobal)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap an array of script object mirrors if needed.

**Parameters:** args

- array to be unwrapped
**Parameters:** homeGlobal

- global to which this object belongs
**Returns:** unwrapped array

- identical

```java
public static boolean identical​(
Object
obj1,

Object
obj2)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Are the given objects mirrors to same underlying object?

**Parameters:** obj1

- first object
**Parameters:** obj2

- second object
**Returns:** true if obj1 and obj2 are identical script objects or mirrors of it.

Method Detail

- callMember

```java
public
Object
callMember​(
String
functionName,

Object
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Call member function

**Parameters:** functionName

- function name
**Parameters:** args

- arguments
**Returns:** return value of function

- setIndexedPropertiesToExternalArrayData

```java
public void setIndexedPropertiesToExternalArrayData​(
ByteBuffer
buf)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn extension: setIndexedPropertiesToExternalArrayData.
set indexed properties be exposed from a given nio ByteBuffer.

**Parameters:** buf

- external buffer - should be a nio ByteBuffer

- delete

```java
public boolean delete​(
Object
key)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Delete a property from this object.

**Parameters:** key

- the property to be deleted
**Returns:** if the delete was successful or not

- getProto

```java
public
Object
getProto()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the __proto__ of this object.

**Returns:** __proto__ object.

- setProto

```java
public void setProto​(
Object
proto)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set the __proto__ of this object.

**Parameters:** proto

- new proto for this object

- getOwnPropertyDescriptor

```java
public
Object
getOwnPropertyDescriptor​(
String
key)
```

Deprecated, for removal: This API element is subject to removal in a future version.

ECMA 8.12.1 [[GetOwnProperty]] (P)

**Parameters:** key

- property key
**Returns:** Returns the Property Descriptor of the named own property of this
object, or undefined if absent.

- getOwnKeys

```java
public
String
[] getOwnKeys​(boolean all)
```

Deprecated, for removal: This API element is subject to removal in a future version.

return an array of own property keys associated with the object.

**Parameters:** all

- True if to include non-enumerable keys.
**Returns:** Array of keys.

- preventExtensions

```java
public
ScriptObjectMirror
preventExtensions()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Flag this script object as non extensible

**Returns:** the object after being made non extensible

- isExtensible

```java
public boolean isExtensible()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Check if this script object is extensible

**Returns:** true if extensible

- seal

```java
public
ScriptObjectMirror
seal()
```

Deprecated, for removal: This API element is subject to removal in a future version.

ECMAScript 15.2.3.8 - seal implementation

**Returns:** the sealed script object

- isSealed

```java
public boolean isSealed()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Check whether this script object is sealed

**Returns:** true if sealed

- freeze

```java
public
ScriptObjectMirror
freeze()
```

Deprecated, for removal: This API element is subject to removal in a future version.

ECMA 15.2.39 - freeze implementation. Freeze this script object

**Returns:** the frozen script object

- isFrozen

```java
public boolean isFrozen()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Check whether this script object is frozen

**Returns:** true if frozen

- isUndefined

```java
public static boolean isUndefined​(
Object
obj)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Utility to check if given object is ECMAScript undefined value

**Parameters:** obj

- object to check
**Returns:** true if 'obj' is ECMAScript undefined value

- to

```java
public <T> T to​(
Class
<T> type)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Utility to convert this script object to the given type.

**Type Parameters:** T

- destination type to convert to
**Parameters:** type

- destination type to convert to
**Returns:** converted object

- wrap

```java
public static
Object
wrap​(
Object
obj,

Object
homeGlobal)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Make a script object mirror on given object if needed.

**Parameters:** obj

- object to be wrapped/converted
**Parameters:** homeGlobal

- global to which this object belongs.
**Returns:** wrapped/converted object

- wrapAsJSONCompatible

```java
public static
Object
wrapAsJSONCompatible​(
Object
obj,

Object
homeGlobal)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Make a script object mirror on given object if needed. The created wrapper will implement
the Java

List

interface if

obj

is a JavaScript

Array

object;
this is compatible with Java JSON libraries expectations. Arrays retrieved through its
properties (transitively) will also implement the list interface.

**Parameters:** obj

- object to be wrapped/converted
**Parameters:** homeGlobal

- global to which this object belongs.
**Returns:** wrapped/converted object

- unwrap

```java
public static
Object
unwrap​(
Object
obj,

Object
homeGlobal)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap a script object mirror if needed.

**Parameters:** obj

- object to be unwrapped
**Parameters:** homeGlobal

- global to which this object belongs
**Returns:** unwrapped object

- wrapArray

```java
public static
Object
[] wrapArray​(
Object
[] args,

Object
homeGlobal)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Wrap an array of object to script object mirrors if needed.

**Parameters:** args

- array to be unwrapped
**Parameters:** homeGlobal

- global to which this object belongs
**Returns:** wrapped array

- unwrapArray

```java
public static
Object
[] unwrapArray​(
Object
[] args,

Object
homeGlobal)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap an array of script object mirrors if needed.

**Parameters:** args

- array to be unwrapped
**Parameters:** homeGlobal

- global to which this object belongs
**Returns:** unwrapped array

- identical

```java
public static boolean identical​(
Object
obj1,

Object
obj2)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Are the given objects mirrors to same underlying object?

**Parameters:** obj1

- first object
**Parameters:** obj2

- second object
**Returns:** true if obj1 and obj2 are identical script objects or mirrors of it.

---

#### Method Detail

callMember

```java
public
Object
callMember​(
String
functionName,

Object
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Call member function

**Parameters:** functionName

- function name
**Parameters:** args

- arguments
**Returns:** return value of function

---

#### callMember

public

Object

callMember​(

String

functionName,

Object

... args)

Call member function

setIndexedPropertiesToExternalArrayData

```java
public void setIndexedPropertiesToExternalArrayData​(
ByteBuffer
buf)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn extension: setIndexedPropertiesToExternalArrayData.
set indexed properties be exposed from a given nio ByteBuffer.

**Parameters:** buf

- external buffer - should be a nio ByteBuffer

---

#### setIndexedPropertiesToExternalArrayData

public void setIndexedPropertiesToExternalArrayData​(

ByteBuffer

buf)

Nashorn extension: setIndexedPropertiesToExternalArrayData.
set indexed properties be exposed from a given nio ByteBuffer.

delete

```java
public boolean delete​(
Object
key)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Delete a property from this object.

**Parameters:** key

- the property to be deleted
**Returns:** if the delete was successful or not

---

#### delete

public boolean delete​(

Object

key)

Delete a property from this object.

getProto

```java
public
Object
getProto()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the __proto__ of this object.

**Returns:** __proto__ object.

---

#### getProto

public

Object

getProto()

Return the __proto__ of this object.

setProto

```java
public void setProto​(
Object
proto)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set the __proto__ of this object.

**Parameters:** proto

- new proto for this object

---

#### setProto

public void setProto​(

Object

proto)

Set the __proto__ of this object.

getOwnPropertyDescriptor

```java
public
Object
getOwnPropertyDescriptor​(
String
key)
```

Deprecated, for removal: This API element is subject to removal in a future version.

ECMA 8.12.1 [[GetOwnProperty]] (P)

**Parameters:** key

- property key
**Returns:** Returns the Property Descriptor of the named own property of this
object, or undefined if absent.

---

#### getOwnPropertyDescriptor

public

Object

getOwnPropertyDescriptor​(

String

key)

ECMA 8.12.1 [[GetOwnProperty]] (P)

getOwnKeys

```java
public
String
[] getOwnKeys​(boolean all)
```

Deprecated, for removal: This API element is subject to removal in a future version.

return an array of own property keys associated with the object.

**Parameters:** all

- True if to include non-enumerable keys.
**Returns:** Array of keys.

---

#### getOwnKeys

public

String

[] getOwnKeys​(boolean all)

return an array of own property keys associated with the object.

preventExtensions

```java
public
ScriptObjectMirror
preventExtensions()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Flag this script object as non extensible

**Returns:** the object after being made non extensible

---

#### preventExtensions

public

ScriptObjectMirror

preventExtensions()

Flag this script object as non extensible

isExtensible

```java
public boolean isExtensible()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Check if this script object is extensible

**Returns:** true if extensible

---

#### isExtensible

public boolean isExtensible()

Check if this script object is extensible

seal

```java
public
ScriptObjectMirror
seal()
```

Deprecated, for removal: This API element is subject to removal in a future version.

ECMAScript 15.2.3.8 - seal implementation

**Returns:** the sealed script object

---

#### seal

public

ScriptObjectMirror

seal()

ECMAScript 15.2.3.8 - seal implementation

isSealed

```java
public boolean isSealed()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Check whether this script object is sealed

**Returns:** true if sealed

---

#### isSealed

public boolean isSealed()

Check whether this script object is sealed

freeze

```java
public
ScriptObjectMirror
freeze()
```

Deprecated, for removal: This API element is subject to removal in a future version.

ECMA 15.2.39 - freeze implementation. Freeze this script object

**Returns:** the frozen script object

---

#### freeze

public

ScriptObjectMirror

freeze()

ECMA 15.2.39 - freeze implementation. Freeze this script object

isFrozen

```java
public boolean isFrozen()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Check whether this script object is frozen

**Returns:** true if frozen

---

#### isFrozen

public boolean isFrozen()

Check whether this script object is frozen

isUndefined

```java
public static boolean isUndefined​(
Object
obj)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Utility to check if given object is ECMAScript undefined value

**Parameters:** obj

- object to check
**Returns:** true if 'obj' is ECMAScript undefined value

---

#### isUndefined

public static boolean isUndefined​(

Object

obj)

Utility to check if given object is ECMAScript undefined value

to

```java
public <T> T to​(
Class
<T> type)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Utility to convert this script object to the given type.

**Type Parameters:** T

- destination type to convert to
**Parameters:** type

- destination type to convert to
**Returns:** converted object

---

#### to

public <T> T to​(

Class

<T> type)

Utility to convert this script object to the given type.

wrap

```java
public static
Object
wrap​(
Object
obj,

Object
homeGlobal)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Make a script object mirror on given object if needed.

**Parameters:** obj

- object to be wrapped/converted
**Parameters:** homeGlobal

- global to which this object belongs.
**Returns:** wrapped/converted object

---

#### wrap

public static

Object

wrap​(

Object

obj,

Object

homeGlobal)

Make a script object mirror on given object if needed.

wrapAsJSONCompatible

```java
public static
Object
wrapAsJSONCompatible​(
Object
obj,

Object
homeGlobal)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Make a script object mirror on given object if needed. The created wrapper will implement
the Java

List

interface if

obj

is a JavaScript

Array

object;
this is compatible with Java JSON libraries expectations. Arrays retrieved through its
properties (transitively) will also implement the list interface.

**Parameters:** obj

- object to be wrapped/converted
**Parameters:** homeGlobal

- global to which this object belongs.
**Returns:** wrapped/converted object

---

#### wrapAsJSONCompatible

public static

Object

wrapAsJSONCompatible​(

Object

obj,

Object

homeGlobal)

Make a script object mirror on given object if needed. The created wrapper will implement
the Java

List

interface if

obj

is a JavaScript

Array

object;
this is compatible with Java JSON libraries expectations. Arrays retrieved through its
properties (transitively) will also implement the list interface.

unwrap

```java
public static
Object
unwrap​(
Object
obj,

Object
homeGlobal)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap a script object mirror if needed.

**Parameters:** obj

- object to be unwrapped
**Parameters:** homeGlobal

- global to which this object belongs
**Returns:** unwrapped object

---

#### unwrap

public static

Object

unwrap​(

Object

obj,

Object

homeGlobal)

Unwrap a script object mirror if needed.

wrapArray

```java
public static
Object
[] wrapArray​(
Object
[] args,

Object
homeGlobal)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Wrap an array of object to script object mirrors if needed.

**Parameters:** args

- array to be unwrapped
**Parameters:** homeGlobal

- global to which this object belongs
**Returns:** wrapped array

---

#### wrapArray

public static

Object

[] wrapArray​(

Object

[] args,

Object

homeGlobal)

Wrap an array of object to script object mirrors if needed.

unwrapArray

```java
public static
Object
[] unwrapArray​(
Object
[] args,

Object
homeGlobal)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Unwrap an array of script object mirrors if needed.

**Parameters:** args

- array to be unwrapped
**Parameters:** homeGlobal

- global to which this object belongs
**Returns:** unwrapped array

---

#### unwrapArray

public static

Object

[] unwrapArray​(

Object

[] args,

Object

homeGlobal)

Unwrap an array of script object mirrors if needed.

identical

```java
public static boolean identical​(
Object
obj1,

Object
obj2)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Are the given objects mirrors to same underlying object?

**Parameters:** obj1

- first object
**Parameters:** obj2

- second object
**Returns:** true if obj1 and obj2 are identical script objects or mirrors of it.

---

#### identical

public static boolean identical​(

Object

obj1,

Object

obj2)

Are the given objects mirrors to same underlying object?

---

