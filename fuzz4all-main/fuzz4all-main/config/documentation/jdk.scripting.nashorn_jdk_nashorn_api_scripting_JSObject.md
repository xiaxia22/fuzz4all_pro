# Interface JSObject

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\scripting\JSObject.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
JSObject
```

This interface can be implemented by an arbitrary Java class. Nashorn will
treat objects of such classes just like nashorn script objects. Usual nashorn
operations like obj[i], obj.foo, obj.func(), delete obj.foo will be delegated
to appropriate method call of this interface.

**All Known Implementing Classes:** AbstractJSObject

,

ScriptObjectMirror

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
call​(
Object
thiz,

Object
... args)

Call this object as a JavaScript function. This is equivalent to
'func.apply(thiz, args)' in JavaScript.

**Parameters:**
- thiz

- 'this' object to be passed to the function. This may be null.
- args

- arguments to method

**Returns:**
- result of call

---

#### Object
newObject​(
Object
... args)

Call this 'constructor' JavaScript function to create a new object.
This is equivalent to 'new func(arg1, arg2...)' in JavaScript.

**Parameters:**
- args

- arguments to method

**Returns:**
- result of constructor call

---

#### Object
eval​(
String
s)

Evaluate a JavaScript expression.

**Parameters:**
- s

- JavaScript expression to evaluate

**Returns:**
- evaluation result

---

#### Object
getMember​(
String
name)

Retrieves a named member of this JavaScript object.

**Parameters:**
- name

- of member

**Returns:**
- member

**Throws:**
- NullPointerException

- if name is null

---

#### Object
getSlot​(int index)

Retrieves an indexed member of this JavaScript object.

**Parameters:**
- index

- index slot to retrieve

**Returns:**
- member

---

#### boolean hasMember​(
String
name)

Does this object have a named member?

**Parameters:**
- name

- name of member

**Returns:**
- true if this object has a member of the given name

---

#### boolean hasSlot​(int slot)

Does this object have a indexed property?

**Parameters:**
- slot

- index to check

**Returns:**
- true if this object has a slot

---

#### void removeMember​(
String
name)

Remove a named member from this JavaScript object

**Parameters:**
- name

- name of the member

**Throws:**
- NullPointerException

- if name is null

---

#### void setMember​(
String
name,

Object
value)

Set a named member in this JavaScript object

**Parameters:**
- name

- name of the member
- value

- value of the member

**Throws:**
- NullPointerException

- if name is null

---

#### void setSlot​(int index,

Object
value)

Set an indexed member in this JavaScript object

**Parameters:**
- index

- index of the member slot
- value

- value of the member

---

#### Set
<
String
> keySet()

Returns the set of all property names of this object.

**Returns:**
- set of property names

---

#### Collection
<
Object
> values()

Returns the set of all property values of this object.

**Returns:**
- set of property values.

---

#### boolean isInstance​(
Object
instance)

Checking whether the given object is an instance of 'this' object.

**Parameters:**
- instance

- instance to check

**Returns:**
- true if the given 'instance' is an instance of this 'function' object

---

#### boolean isInstanceOf​(
Object
clazz)

Checking whether this object is an instance of the given 'clazz' object.

**Parameters:**
- clazz

- clazz to check

**Returns:**
- true if this object is an instance of the given 'clazz'

---

#### String
getClassName()

ECMA [[Class]] property

**Returns:**
- ECMA [[Class]] property value of this object

---

#### boolean isFunction()

Is this a function object?

**Returns:**
- if this mirror wraps a ECMAScript function instance

---

#### boolean isStrictFunction()

Is this a 'use strict' function object?

**Returns:**
- true if this mirror represents a ECMAScript 'use strict' function

---

#### boolean isArray()

Is this an array object?

**Returns:**
- if this mirror wraps a ECMAScript array object

---

#### @Deprecated

default double toNumber()

Returns this object's numeric value.

**Returns:**
- this object's numeric value.

---

#### default
Object
getDefaultValue​(
Class
<?> hint)
throws
UnsupportedOperationException

Implements this object's

[[DefaultValue]]

method as per ECMAScript 5.1 section 8.6.2.

**Parameters:**
- hint

- the type hint. Should be either

null

,

Number.class

or

String.class

.

**Returns:**
- this object's default value.

**Throws:**
- UnsupportedOperationException

- if the conversion can't be performed. The engine will convert this
exception into a JavaScript

TypeError

.

---

### Additional Sections

#### Interface JSObject

**All Known Implementing Classes:** AbstractJSObject

,

ScriptObjectMirror

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
JSObject
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

This interface can be implemented by an arbitrary Java class. Nashorn will
treat objects of such classes just like nashorn script objects. Usual nashorn
operations like obj[i], obj.foo, obj.func(), delete obj.foo will be delegated
to appropriate method call of this interface.

**Since:** 1.8u40

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

JSObject

This interface can be implemented by an arbitrary Java class. Nashorn will
treat objects of such classes just like nashorn script objects. Usual nashorn
operations like obj[i], obj.foo, obj.func(), delete obj.foo will be delegated
to appropriate method call of this interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Deprecated Methods

Modifier and Type

Method

Description

Object

call

​(

Object

thiz,

Object

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Call this object as a JavaScript function.

Object

eval

​(

String

s)

Deprecated, for removal: This API element is subject to removal in a future version.

Evaluate a JavaScript expression.

String

getClassName

()

Deprecated, for removal: This API element is subject to removal in a future version.

ECMA [[Class]] property

default

Object

getDefaultValue

​(

Class

<?> hint)

Deprecated, for removal: This API element is subject to removal in a future version.

Implements this object's

[[DefaultValue]]

method as per ECMAScript 5.1 section 8.6.2.

Object

getMember

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves a named member of this JavaScript object.

Object

getSlot

​(int index)

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves an indexed member of this JavaScript object.

boolean

hasMember

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Does this object have a named member?

boolean

hasSlot

​(int slot)

Deprecated, for removal: This API element is subject to removal in a future version.

Does this object have a indexed property?

boolean

isArray

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this an array object?

boolean

isFunction

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a function object?

boolean

isInstance

​(

Object

instance)

Deprecated, for removal: This API element is subject to removal in a future version.

Checking whether the given object is an instance of 'this' object.

boolean

isInstanceOf

​(

Object

clazz)

Deprecated, for removal: This API element is subject to removal in a future version.

Checking whether this object is an instance of the given 'clazz' object.

boolean

isStrictFunction

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a 'use strict' function object?

Set

<

String

>

keySet

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the set of all property names of this object.

Object

newObject

​(

Object

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Call this 'constructor' JavaScript function to create a new object.

void

removeMember

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Remove a named member from this JavaScript object

void

setMember

​(

String

name,

Object

value)

Deprecated, for removal: This API element is subject to removal in a future version.

Set a named member in this JavaScript object

void

setSlot

​(int index,

Object

value)

Deprecated, for removal: This API element is subject to removal in a future version.

Set an indexed member in this JavaScript object

default double

toNumber

()

Deprecated.

use

getDefaultValue(Class)

with

Number

hint instead.

Collection

<

Object

>

values

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the set of all property values of this object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Deprecated Methods

Modifier and Type

Method

Description

Object

call

​(

Object

thiz,

Object

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Call this object as a JavaScript function.

Object

eval

​(

String

s)

Deprecated, for removal: This API element is subject to removal in a future version.

Evaluate a JavaScript expression.

String

getClassName

()

Deprecated, for removal: This API element is subject to removal in a future version.

ECMA [[Class]] property

default

Object

getDefaultValue

​(

Class

<?> hint)

Deprecated, for removal: This API element is subject to removal in a future version.

Implements this object's

[[DefaultValue]]

method as per ECMAScript 5.1 section 8.6.2.

Object

getMember

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves a named member of this JavaScript object.

Object

getSlot

​(int index)

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves an indexed member of this JavaScript object.

boolean

hasMember

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Does this object have a named member?

boolean

hasSlot

​(int slot)

Deprecated, for removal: This API element is subject to removal in a future version.

Does this object have a indexed property?

boolean

isArray

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this an array object?

boolean

isFunction

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a function object?

boolean

isInstance

​(

Object

instance)

Deprecated, for removal: This API element is subject to removal in a future version.

Checking whether the given object is an instance of 'this' object.

boolean

isInstanceOf

​(

Object

clazz)

Deprecated, for removal: This API element is subject to removal in a future version.

Checking whether this object is an instance of the given 'clazz' object.

boolean

isStrictFunction

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a 'use strict' function object?

Set

<

String

>

keySet

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the set of all property names of this object.

Object

newObject

​(

Object

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Call this 'constructor' JavaScript function to create a new object.

void

removeMember

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Remove a named member from this JavaScript object

void

setMember

​(

String

name,

Object

value)

Deprecated, for removal: This API element is subject to removal in a future version.

Set a named member in this JavaScript object

void

setSlot

​(int index,

Object

value)

Deprecated, for removal: This API element is subject to removal in a future version.

Set an indexed member in this JavaScript object

default double

toNumber

()

Deprecated.

use

getDefaultValue(Class)

with

Number

hint instead.

Collection

<

Object

>

values

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the set of all property values of this object.

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Call this object as a JavaScript function.

Evaluate a JavaScript expression.

ECMA [[Class]] property

Implements this object's

[[DefaultValue]]

method as per ECMAScript 5.1 section 8.6.2.

Retrieves a named member of this JavaScript object.

Retrieves an indexed member of this JavaScript object.

Does this object have a named member?

Does this object have a indexed property?

Is this an array object?

Is this a function object?

Checking whether the given object is an instance of 'this' object.

Checking whether this object is an instance of the given 'clazz' object.

Is this a 'use strict' function object?

Returns the set of all property names of this object.

Call this 'constructor' JavaScript function to create a new object.

Remove a named member from this JavaScript object

Set a named member in this JavaScript object

Set an indexed member in this JavaScript object

Deprecated.

use

getDefaultValue(Class)

with

Number

hint instead.

Returns the set of all property values of this object.

============ METHOD DETAIL ==========

- Method Detail

- call

```java
Object
call​(
Object
thiz,

Object
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Call this object as a JavaScript function. This is equivalent to
'func.apply(thiz, args)' in JavaScript.

**Parameters:** thiz

- 'this' object to be passed to the function. This may be null.
**Parameters:** args

- arguments to method
**Returns:** result of call

- newObject

```java
Object
newObject​(
Object
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Call this 'constructor' JavaScript function to create a new object.
This is equivalent to 'new func(arg1, arg2...)' in JavaScript.

**Parameters:** args

- arguments to method
**Returns:** result of constructor call

- eval

```java
Object
eval​(
String
s)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Evaluate a JavaScript expression.

**Parameters:** s

- JavaScript expression to evaluate
**Returns:** evaluation result

- getMember

```java
Object
getMember​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves a named member of this JavaScript object.

**Parameters:** name

- of member
**Returns:** member
**Throws:** NullPointerException

- if name is null

- getSlot

```java
Object
getSlot​(int index)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves an indexed member of this JavaScript object.

**Parameters:** index

- index slot to retrieve
**Returns:** member

- hasMember

```java
boolean hasMember​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Does this object have a named member?

**Parameters:** name

- name of member
**Returns:** true if this object has a member of the given name

- hasSlot

```java
boolean hasSlot​(int slot)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Does this object have a indexed property?

**Parameters:** slot

- index to check
**Returns:** true if this object has a slot

- removeMember

```java
void removeMember​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Remove a named member from this JavaScript object

**Parameters:** name

- name of the member
**Throws:** NullPointerException

- if name is null

- setMember

```java
void setMember​(
String
name,

Object
value)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set a named member in this JavaScript object

**Parameters:** name

- name of the member
**Parameters:** value

- value of the member
**Throws:** NullPointerException

- if name is null

- setSlot

```java
void setSlot​(int index,

Object
value)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set an indexed member in this JavaScript object

**Parameters:** index

- index of the member slot
**Parameters:** value

- value of the member

- keySet

```java
Set
<
String
> keySet()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the set of all property names of this object.

**Returns:** set of property names

- values

```java
Collection
<
Object
> values()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the set of all property values of this object.

**Returns:** set of property values.

- isInstance

```java
boolean isInstance​(
Object
instance)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Checking whether the given object is an instance of 'this' object.

**Parameters:** instance

- instance to check
**Returns:** true if the given 'instance' is an instance of this 'function' object

- isInstanceOf

```java
boolean isInstanceOf​(
Object
clazz)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Checking whether this object is an instance of the given 'clazz' object.

**Parameters:** clazz

- clazz to check
**Returns:** true if this object is an instance of the given 'clazz'

- getClassName

```java
String
getClassName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

ECMA [[Class]] property

**Returns:** ECMA [[Class]] property value of this object

- isFunction

```java
boolean isFunction()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a function object?

**Returns:** if this mirror wraps a ECMAScript function instance

- isStrictFunction

```java
boolean isStrictFunction()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a 'use strict' function object?

**Returns:** true if this mirror represents a ECMAScript 'use strict' function

- isArray

```java
boolean isArray()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this an array object?

**Returns:** if this mirror wraps a ECMAScript array object

- toNumber

```java
@Deprecated

default double toNumber()
```

Deprecated.

use

getDefaultValue(Class)

with

Number

hint instead.

Returns this object's numeric value.

**Returns:** this object's numeric value.

- getDefaultValue

```java
default
Object
getDefaultValue​(
Class
<?> hint)
throws
UnsupportedOperationException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Implements this object's

[[DefaultValue]]

method as per ECMAScript 5.1 section 8.6.2.

**Parameters:** hint

- the type hint. Should be either

null

,

Number.class

or

String.class

.
**Returns:** this object's default value.
**Throws:** UnsupportedOperationException

- if the conversion can't be performed. The engine will convert this
exception into a JavaScript

TypeError

.

Method Detail

- call

```java
Object
call​(
Object
thiz,

Object
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Call this object as a JavaScript function. This is equivalent to
'func.apply(thiz, args)' in JavaScript.

**Parameters:** thiz

- 'this' object to be passed to the function. This may be null.
**Parameters:** args

- arguments to method
**Returns:** result of call

- newObject

```java
Object
newObject​(
Object
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Call this 'constructor' JavaScript function to create a new object.
This is equivalent to 'new func(arg1, arg2...)' in JavaScript.

**Parameters:** args

- arguments to method
**Returns:** result of constructor call

- eval

```java
Object
eval​(
String
s)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Evaluate a JavaScript expression.

**Parameters:** s

- JavaScript expression to evaluate
**Returns:** evaluation result

- getMember

```java
Object
getMember​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves a named member of this JavaScript object.

**Parameters:** name

- of member
**Returns:** member
**Throws:** NullPointerException

- if name is null

- getSlot

```java
Object
getSlot​(int index)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves an indexed member of this JavaScript object.

**Parameters:** index

- index slot to retrieve
**Returns:** member

- hasMember

```java
boolean hasMember​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Does this object have a named member?

**Parameters:** name

- name of member
**Returns:** true if this object has a member of the given name

- hasSlot

```java
boolean hasSlot​(int slot)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Does this object have a indexed property?

**Parameters:** slot

- index to check
**Returns:** true if this object has a slot

- removeMember

```java
void removeMember​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Remove a named member from this JavaScript object

**Parameters:** name

- name of the member
**Throws:** NullPointerException

- if name is null

- setMember

```java
void setMember​(
String
name,

Object
value)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set a named member in this JavaScript object

**Parameters:** name

- name of the member
**Parameters:** value

- value of the member
**Throws:** NullPointerException

- if name is null

- setSlot

```java
void setSlot​(int index,

Object
value)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set an indexed member in this JavaScript object

**Parameters:** index

- index of the member slot
**Parameters:** value

- value of the member

- keySet

```java
Set
<
String
> keySet()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the set of all property names of this object.

**Returns:** set of property names

- values

```java
Collection
<
Object
> values()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the set of all property values of this object.

**Returns:** set of property values.

- isInstance

```java
boolean isInstance​(
Object
instance)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Checking whether the given object is an instance of 'this' object.

**Parameters:** instance

- instance to check
**Returns:** true if the given 'instance' is an instance of this 'function' object

- isInstanceOf

```java
boolean isInstanceOf​(
Object
clazz)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Checking whether this object is an instance of the given 'clazz' object.

**Parameters:** clazz

- clazz to check
**Returns:** true if this object is an instance of the given 'clazz'

- getClassName

```java
String
getClassName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

ECMA [[Class]] property

**Returns:** ECMA [[Class]] property value of this object

- isFunction

```java
boolean isFunction()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a function object?

**Returns:** if this mirror wraps a ECMAScript function instance

- isStrictFunction

```java
boolean isStrictFunction()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a 'use strict' function object?

**Returns:** true if this mirror represents a ECMAScript 'use strict' function

- isArray

```java
boolean isArray()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this an array object?

**Returns:** if this mirror wraps a ECMAScript array object

- toNumber

```java
@Deprecated

default double toNumber()
```

Deprecated.

use

getDefaultValue(Class)

with

Number

hint instead.

Returns this object's numeric value.

**Returns:** this object's numeric value.

- getDefaultValue

```java
default
Object
getDefaultValue​(
Class
<?> hint)
throws
UnsupportedOperationException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Implements this object's

[[DefaultValue]]

method as per ECMAScript 5.1 section 8.6.2.

**Parameters:** hint

- the type hint. Should be either

null

,

Number.class

or

String.class

.
**Returns:** this object's default value.
**Throws:** UnsupportedOperationException

- if the conversion can't be performed. The engine will convert this
exception into a JavaScript

TypeError

.

---

#### Method Detail

call

```java
Object
call​(
Object
thiz,

Object
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Call this object as a JavaScript function. This is equivalent to
'func.apply(thiz, args)' in JavaScript.

**Parameters:** thiz

- 'this' object to be passed to the function. This may be null.
**Parameters:** args

- arguments to method
**Returns:** result of call

---

#### call

Object

call​(

Object

thiz,

Object

... args)

Call this object as a JavaScript function. This is equivalent to
'func.apply(thiz, args)' in JavaScript.

newObject

```java
Object
newObject​(
Object
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Call this 'constructor' JavaScript function to create a new object.
This is equivalent to 'new func(arg1, arg2...)' in JavaScript.

**Parameters:** args

- arguments to method
**Returns:** result of constructor call

---

#### newObject

Object

newObject​(

Object

... args)

Call this 'constructor' JavaScript function to create a new object.
This is equivalent to 'new func(arg1, arg2...)' in JavaScript.

eval

```java
Object
eval​(
String
s)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Evaluate a JavaScript expression.

**Parameters:** s

- JavaScript expression to evaluate
**Returns:** evaluation result

---

#### eval

Object

eval​(

String

s)

Evaluate a JavaScript expression.

getMember

```java
Object
getMember​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves a named member of this JavaScript object.

**Parameters:** name

- of member
**Returns:** member
**Throws:** NullPointerException

- if name is null

---

#### getMember

Object

getMember​(

String

name)

Retrieves a named member of this JavaScript object.

getSlot

```java
Object
getSlot​(int index)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves an indexed member of this JavaScript object.

**Parameters:** index

- index slot to retrieve
**Returns:** member

---

#### getSlot

Object

getSlot​(int index)

Retrieves an indexed member of this JavaScript object.

hasMember

```java
boolean hasMember​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Does this object have a named member?

**Parameters:** name

- name of member
**Returns:** true if this object has a member of the given name

---

#### hasMember

boolean hasMember​(

String

name)

Does this object have a named member?

hasSlot

```java
boolean hasSlot​(int slot)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Does this object have a indexed property?

**Parameters:** slot

- index to check
**Returns:** true if this object has a slot

---

#### hasSlot

boolean hasSlot​(int slot)

Does this object have a indexed property?

removeMember

```java
void removeMember​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Remove a named member from this JavaScript object

**Parameters:** name

- name of the member
**Throws:** NullPointerException

- if name is null

---

#### removeMember

void removeMember​(

String

name)

Remove a named member from this JavaScript object

setMember

```java
void setMember​(
String
name,

Object
value)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set a named member in this JavaScript object

**Parameters:** name

- name of the member
**Parameters:** value

- value of the member
**Throws:** NullPointerException

- if name is null

---

#### setMember

void setMember​(

String

name,

Object

value)

Set a named member in this JavaScript object

setSlot

```java
void setSlot​(int index,

Object
value)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set an indexed member in this JavaScript object

**Parameters:** index

- index of the member slot
**Parameters:** value

- value of the member

---

#### setSlot

void setSlot​(int index,

Object

value)

Set an indexed member in this JavaScript object

keySet

```java
Set
<
String
> keySet()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the set of all property names of this object.

**Returns:** set of property names

---

#### keySet

Set

<

String

> keySet()

Returns the set of all property names of this object.

values

```java
Collection
<
Object
> values()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the set of all property values of this object.

**Returns:** set of property values.

---

#### values

Collection

<

Object

> values()

Returns the set of all property values of this object.

isInstance

```java
boolean isInstance​(
Object
instance)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Checking whether the given object is an instance of 'this' object.

**Parameters:** instance

- instance to check
**Returns:** true if the given 'instance' is an instance of this 'function' object

---

#### isInstance

boolean isInstance​(

Object

instance)

Checking whether the given object is an instance of 'this' object.

isInstanceOf

```java
boolean isInstanceOf​(
Object
clazz)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Checking whether this object is an instance of the given 'clazz' object.

**Parameters:** clazz

- clazz to check
**Returns:** true if this object is an instance of the given 'clazz'

---

#### isInstanceOf

boolean isInstanceOf​(

Object

clazz)

Checking whether this object is an instance of the given 'clazz' object.

getClassName

```java
String
getClassName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

ECMA [[Class]] property

**Returns:** ECMA [[Class]] property value of this object

---

#### getClassName

String

getClassName()

ECMA [[Class]] property

isFunction

```java
boolean isFunction()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a function object?

**Returns:** if this mirror wraps a ECMAScript function instance

---

#### isFunction

boolean isFunction()

Is this a function object?

isStrictFunction

```java
boolean isStrictFunction()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a 'use strict' function object?

**Returns:** true if this mirror represents a ECMAScript 'use strict' function

---

#### isStrictFunction

boolean isStrictFunction()

Is this a 'use strict' function object?

isArray

```java
boolean isArray()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this an array object?

**Returns:** if this mirror wraps a ECMAScript array object

---

#### isArray

boolean isArray()

Is this an array object?

toNumber

```java
@Deprecated

default double toNumber()
```

Deprecated.

use

getDefaultValue(Class)

with

Number

hint instead.

Returns this object's numeric value.

**Returns:** this object's numeric value.

---

#### toNumber

@Deprecated

default double toNumber()

Returns this object's numeric value.

getDefaultValue

```java
default
Object
getDefaultValue​(
Class
<?> hint)
throws
UnsupportedOperationException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Implements this object's

[[DefaultValue]]

method as per ECMAScript 5.1 section 8.6.2.

**Parameters:** hint

- the type hint. Should be either

null

,

Number.class

or

String.class

.
**Returns:** this object's default value.
**Throws:** UnsupportedOperationException

- if the conversion can't be performed. The engine will convert this
exception into a JavaScript

TypeError

.

---

#### getDefaultValue

default

Object

getDefaultValue​(

Class

<?> hint)
throws

UnsupportedOperationException

Implements this object's

[[DefaultValue]]

method as per ECMAScript 5.1 section 8.6.2.

---

