# Class AbstractJSObject

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\scripting\AbstractJSObject.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public abstract class
AbstractJSObject

extends
Object

implements
JSObject
```

This is the base class for nashorn ScriptObjectMirror class.

This class can also be subclassed by an arbitrary Java class. Nashorn will
treat objects of such classes just like nashorn script objects. Usual nashorn
operations like obj[i], obj.foo, obj.func(), delete obj.foo will be delegated
to appropriate method call of this class.

**All Implemented Interfaces:** JSObject

---

### Field Details

*No entries found.*

### Constructor Details

#### public AbstractJSObject()

The default constructor.

---

### Method Details

#### public
Object
call​(
Object
thiz,

Object
... args)

Description copied from interface:

JSObject

**Specified by:**
- call

in interface

JSObject

**Parameters:**
- thiz

- 'this' object to be passed to the function. This may be null.
- args

- arguments to method

**Returns:**
- result of call

**Implementation Requirements:**
- This implementation always throws UnsupportedOperationException

---

#### public
Object
newObject​(
Object
... args)

Description copied from interface:

JSObject

**Specified by:**
- newObject

in interface

JSObject

**Parameters:**
- args

- arguments to method

**Returns:**
- result of constructor call

**Implementation Requirements:**
- This implementation always throws UnsupportedOperationException

---

#### public
Object
eval​(
String
s)

Description copied from interface:

JSObject

**Specified by:**
- eval

in interface

JSObject

**Parameters:**
- s

- JavaScript expression to evaluate

**Returns:**
- evaluation result

**Implementation Requirements:**
- This imlementation always throws UnsupportedOperationException

---

#### public
Object
getMember​(
String
name)

Description copied from interface:

JSObject

**Specified by:**
- getMember

in interface

JSObject

**Parameters:**
- name

- of member

**Returns:**
- member

**Implementation Requirements:**
- This implementation always returns null

---

#### public
Object
getSlot​(int index)

Description copied from interface:

JSObject

**Specified by:**
- getSlot

in interface

JSObject

**Parameters:**
- index

- index slot to retrieve

**Returns:**
- member

**Implementation Requirements:**
- This implementation always returns null

---

#### public boolean hasMember​(
String
name)

Description copied from interface:

JSObject

**Specified by:**
- hasMember

in interface

JSObject

**Parameters:**
- name

- name of member

**Returns:**
- true if this object has a member of the given name

**Implementation Requirements:**
- This implementation always returns false

---

#### public boolean hasSlot​(int slot)

Description copied from interface:

JSObject

**Specified by:**
- hasSlot

in interface

JSObject

**Parameters:**
- slot

- index to check

**Returns:**
- true if this object has a slot

**Implementation Requirements:**
- This implementation always returns false

---

#### public void removeMember​(
String
name)

Description copied from interface:

JSObject

**Specified by:**
- removeMember

in interface

JSObject

**Parameters:**
- name

- name of the member

**Implementation Requirements:**
- This implementation is a no-op

---

#### public void setMember​(
String
name,

Object
value)

Description copied from interface:

JSObject

**Specified by:**
- setMember

in interface

JSObject

**Parameters:**
- name

- name of the member
- value

- value of the member

**Implementation Requirements:**
- This implementation is a no-op

---

#### public void setSlot​(int index,

Object
value)

Description copied from interface:

JSObject

**Specified by:**
- setSlot

in interface

JSObject

**Parameters:**
- index

- index of the member slot
- value

- value of the member

**Implementation Requirements:**
- This implementation is a no-op

---

#### public
Set
<
String
> keySet()

Description copied from interface:

JSObject

**Specified by:**
- keySet

in interface

JSObject

**Returns:**
- set of property names

**Implementation Requirements:**
- This implementation returns empty set

---

#### public
Collection
<
Object
> values()

Description copied from interface:

JSObject

**Specified by:**
- values

in interface

JSObject

**Returns:**
- set of property values.

**Implementation Requirements:**
- This implementation returns empty set

---

#### public boolean isInstance​(
Object
instance)

Description copied from interface:

JSObject

**Specified by:**
- isInstance

in interface

JSObject

**Parameters:**
- instance

- instance to check

**Returns:**
- true if the given 'instance' is an instance of this 'function' object

**Implementation Requirements:**
- This implementation always returns false

---

#### public boolean isFunction()

Description copied from interface:

JSObject

**Specified by:**
- isFunction

in interface

JSObject

**Returns:**
- if this mirror wraps a ECMAScript function instance

**Implementation Requirements:**
- This implementation always returns false

---

#### public boolean isStrictFunction()

Description copied from interface:

JSObject

**Specified by:**
- isStrictFunction

in interface

JSObject

**Returns:**
- true if this mirror represents a ECMAScript 'use strict' function

**Implementation Requirements:**
- This implementation always returns false

---

#### public boolean isArray()

Description copied from interface:

JSObject

**Specified by:**
- isArray

in interface

JSObject

**Returns:**
- if this mirror wraps a ECMAScript array object

**Implementation Requirements:**
- This implementation always returns false

---

#### @Deprecated

public double toNumber()

Returns this object's numeric value.

**Specified by:**
- toNumber

in interface

JSObject

**Returns:**
- this object's numeric value.

---

#### @Deprecated

public static
Object
getDefaultValue​(
JSObject
jsobj,

Class
<?> hint)

When passed an

AbstractJSObject

, invokes its

JSObject.getDefaultValue(Class)

method. When passed any
other

JSObject

, it will obtain its

[[DefaultValue]]

method as per ECMAScript 5.1 section
8.6.2.

**Parameters:**
- jsobj

- the

JSObject

whose

[[DefaultValue]]

is obtained.
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

#### Class AbstractJSObject

java.lang.Object

- jdk.nashorn.api.scripting.AbstractJSObject

jdk.nashorn.api.scripting.AbstractJSObject

**All Implemented Interfaces:** JSObject

**Direct Known Subclasses:** ScriptObjectMirror

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public abstract class
AbstractJSObject

extends
Object

implements
JSObject
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

This is the base class for nashorn ScriptObjectMirror class.

This class can also be subclassed by an arbitrary Java class. Nashorn will
treat objects of such classes just like nashorn script objects. Usual nashorn
operations like obj[i], obj.foo, obj.func(), delete obj.foo will be delegated
to appropriate method call of this class.

**Since:** 1.8u40

@Deprecated

(

since

="11",

forRemoval

=true)
public abstract class

AbstractJSObject

extends

Object

implements

JSObject

This is the base class for nashorn ScriptObjectMirror class.

This class can also be subclassed by an arbitrary Java class. Nashorn will
treat objects of such classes just like nashorn script objects. Usual nashorn
operations like obj[i], obj.foo, obj.func(), delete obj.foo will be delegated
to appropriate method call of this class.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AbstractJSObject

()

Deprecated, for removal: This API element is subject to removal in a future version.

The default constructor.

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

static

Object

getDefaultValue

​(

JSObject

jsobj,

Class

<?> hint)

Deprecated.

use

JSObject.getDefaultValue(Class)

instead.

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

double

toNumber

()

Deprecated.

use

JSObject.getDefaultValue(Class)

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

- Methods declared in interface jdk.nashorn.api.scripting.

JSObject

getClassName

,

getDefaultValue

,

isInstanceOf

Constructor Summary

Constructors

Constructor

Description

AbstractJSObject

()

Deprecated, for removal: This API element is subject to removal in a future version.

The default constructor.

---

#### Constructor Summary

Deprecated, for removal: This API element is subject to removal in a future version.

The default constructor.

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

static

Object

getDefaultValue

​(

JSObject

jsobj,

Class

<?> hint)

Deprecated.

use

JSObject.getDefaultValue(Class)

instead.

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

double

toNumber

()

Deprecated.

use

JSObject.getDefaultValue(Class)

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

- Methods declared in interface jdk.nashorn.api.scripting.

JSObject

getClassName

,

getDefaultValue

,

isInstanceOf

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Call this object as a JavaScript function.

Evaluate a JavaScript expression.

Deprecated.

use

JSObject.getDefaultValue(Class)

instead.

Retrieves a named member of this JavaScript object.

Retrieves an indexed member of this JavaScript object.

Does this object have a named member?

Does this object have a indexed property?

Is this an array object?

Is this a function object?

Checking whether the given object is an instance of 'this' object.

Is this a 'use strict' function object?

Returns the set of all property names of this object.

Call this 'constructor' JavaScript function to create a new object.

Remove a named member from this JavaScript object

Set a named member in this JavaScript object

Set an indexed member in this JavaScript object

Deprecated.

use

JSObject.getDefaultValue(Class)

with

Number

hint instead.

Returns the set of all property values of this object.

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

Methods declared in interface jdk.nashorn.api.scripting.

JSObject

getClassName

,

getDefaultValue

,

isInstanceOf

---

#### Methods declared in interface jdk.nashorn.api.scripting. JSObject

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractJSObject

```java
public AbstractJSObject()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The default constructor.

============ METHOD DETAIL ==========

- Method Detail

- call

```java
public
Object
call​(
Object
thiz,

Object
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Call this object as a JavaScript function. This is equivalent to
'func.apply(thiz, args)' in JavaScript.

**Specified by:** call

in interface

JSObject
**Implementation Requirements:** This implementation always throws UnsupportedOperationException
**Parameters:** thiz

- 'this' object to be passed to the function. This may be null.
**Parameters:** args

- arguments to method
**Returns:** result of call

- newObject

```java
public
Object
newObject​(
Object
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Call this 'constructor' JavaScript function to create a new object.
This is equivalent to 'new func(arg1, arg2...)' in JavaScript.

**Specified by:** newObject

in interface

JSObject
**Implementation Requirements:** This implementation always throws UnsupportedOperationException
**Parameters:** args

- arguments to method
**Returns:** result of constructor call

- eval

```java
public
Object
eval​(
String
s)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Evaluate a JavaScript expression.

**Specified by:** eval

in interface

JSObject
**Implementation Requirements:** This imlementation always throws UnsupportedOperationException
**Parameters:** s

- JavaScript expression to evaluate
**Returns:** evaluation result

- getMember

```java
public
Object
getMember​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Retrieves a named member of this JavaScript object.

**Specified by:** getMember

in interface

JSObject
**Implementation Requirements:** This implementation always returns null
**Parameters:** name

- of member
**Returns:** member

- getSlot

```java
public
Object
getSlot​(int index)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Retrieves an indexed member of this JavaScript object.

**Specified by:** getSlot

in interface

JSObject
**Implementation Requirements:** This implementation always returns null
**Parameters:** index

- index slot to retrieve
**Returns:** member

- hasMember

```java
public boolean hasMember​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Does this object have a named member?

**Specified by:** hasMember

in interface

JSObject
**Implementation Requirements:** This implementation always returns false
**Parameters:** name

- name of member
**Returns:** true if this object has a member of the given name

- hasSlot

```java
public boolean hasSlot​(int slot)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Does this object have a indexed property?

**Specified by:** hasSlot

in interface

JSObject
**Implementation Requirements:** This implementation always returns false
**Parameters:** slot

- index to check
**Returns:** true if this object has a slot

- removeMember

```java
public void removeMember​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Remove a named member from this JavaScript object

**Specified by:** removeMember

in interface

JSObject
**Implementation Requirements:** This implementation is a no-op
**Parameters:** name

- name of the member

- setMember

```java
public void setMember​(
String
name,

Object
value)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Set a named member in this JavaScript object

**Specified by:** setMember

in interface

JSObject
**Implementation Requirements:** This implementation is a no-op
**Parameters:** name

- name of the member
**Parameters:** value

- value of the member

- setSlot

```java
public void setSlot​(int index,

Object
value)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Set an indexed member in this JavaScript object

**Specified by:** setSlot

in interface

JSObject
**Implementation Requirements:** This implementation is a no-op
**Parameters:** index

- index of the member slot
**Parameters:** value

- value of the member

- keySet

```java
public
Set
<
String
> keySet()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Returns the set of all property names of this object.

**Specified by:** keySet

in interface

JSObject
**Implementation Requirements:** This implementation returns empty set
**Returns:** set of property names

- values

```java
public
Collection
<
Object
> values()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Returns the set of all property values of this object.

**Specified by:** values

in interface

JSObject
**Implementation Requirements:** This implementation returns empty set
**Returns:** set of property values.

- isInstance

```java
public boolean isInstance​(
Object
instance)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Checking whether the given object is an instance of 'this' object.

**Specified by:** isInstance

in interface

JSObject
**Implementation Requirements:** This implementation always returns false
**Parameters:** instance

- instance to check
**Returns:** true if the given 'instance' is an instance of this 'function' object

- isFunction

```java
public boolean isFunction()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Is this a function object?

**Specified by:** isFunction

in interface

JSObject
**Implementation Requirements:** This implementation always returns false
**Returns:** if this mirror wraps a ECMAScript function instance

- isStrictFunction

```java
public boolean isStrictFunction()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Is this a 'use strict' function object?

**Specified by:** isStrictFunction

in interface

JSObject
**Implementation Requirements:** This implementation always returns false
**Returns:** true if this mirror represents a ECMAScript 'use strict' function

- isArray

```java
public boolean isArray()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Is this an array object?

**Specified by:** isArray

in interface

JSObject
**Implementation Requirements:** This implementation always returns false
**Returns:** if this mirror wraps a ECMAScript array object

- toNumber

```java
@Deprecated

public double toNumber()
```

Deprecated.

use

JSObject.getDefaultValue(Class)

with

Number

hint instead.

Returns this object's numeric value.

**Specified by:** toNumber

in interface

JSObject
**Returns:** this object's numeric value.

- getDefaultValue

```java
@Deprecated

public static
Object
getDefaultValue​(
JSObject
jsobj,

Class
<?> hint)
```

Deprecated.

use

JSObject.getDefaultValue(Class)

instead.

When passed an

AbstractJSObject

, invokes its

JSObject.getDefaultValue(Class)

method. When passed any
other

JSObject

, it will obtain its

[[DefaultValue]]

method as per ECMAScript 5.1 section
8.6.2.

**Parameters:** jsobj

- the

JSObject

whose

[[DefaultValue]]

is obtained.
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

Constructor Detail

- AbstractJSObject

```java
public AbstractJSObject()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The default constructor.

---

#### Constructor Detail

AbstractJSObject

```java
public AbstractJSObject()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The default constructor.

---

#### AbstractJSObject

public AbstractJSObject()

The default constructor.

Method Detail

- call

```java
public
Object
call​(
Object
thiz,

Object
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Call this object as a JavaScript function. This is equivalent to
'func.apply(thiz, args)' in JavaScript.

**Specified by:** call

in interface

JSObject
**Implementation Requirements:** This implementation always throws UnsupportedOperationException
**Parameters:** thiz

- 'this' object to be passed to the function. This may be null.
**Parameters:** args

- arguments to method
**Returns:** result of call

- newObject

```java
public
Object
newObject​(
Object
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Call this 'constructor' JavaScript function to create a new object.
This is equivalent to 'new func(arg1, arg2...)' in JavaScript.

**Specified by:** newObject

in interface

JSObject
**Implementation Requirements:** This implementation always throws UnsupportedOperationException
**Parameters:** args

- arguments to method
**Returns:** result of constructor call

- eval

```java
public
Object
eval​(
String
s)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Evaluate a JavaScript expression.

**Specified by:** eval

in interface

JSObject
**Implementation Requirements:** This imlementation always throws UnsupportedOperationException
**Parameters:** s

- JavaScript expression to evaluate
**Returns:** evaluation result

- getMember

```java
public
Object
getMember​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Retrieves a named member of this JavaScript object.

**Specified by:** getMember

in interface

JSObject
**Implementation Requirements:** This implementation always returns null
**Parameters:** name

- of member
**Returns:** member

- getSlot

```java
public
Object
getSlot​(int index)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Retrieves an indexed member of this JavaScript object.

**Specified by:** getSlot

in interface

JSObject
**Implementation Requirements:** This implementation always returns null
**Parameters:** index

- index slot to retrieve
**Returns:** member

- hasMember

```java
public boolean hasMember​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Does this object have a named member?

**Specified by:** hasMember

in interface

JSObject
**Implementation Requirements:** This implementation always returns false
**Parameters:** name

- name of member
**Returns:** true if this object has a member of the given name

- hasSlot

```java
public boolean hasSlot​(int slot)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Does this object have a indexed property?

**Specified by:** hasSlot

in interface

JSObject
**Implementation Requirements:** This implementation always returns false
**Parameters:** slot

- index to check
**Returns:** true if this object has a slot

- removeMember

```java
public void removeMember​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Remove a named member from this JavaScript object

**Specified by:** removeMember

in interface

JSObject
**Implementation Requirements:** This implementation is a no-op
**Parameters:** name

- name of the member

- setMember

```java
public void setMember​(
String
name,

Object
value)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Set a named member in this JavaScript object

**Specified by:** setMember

in interface

JSObject
**Implementation Requirements:** This implementation is a no-op
**Parameters:** name

- name of the member
**Parameters:** value

- value of the member

- setSlot

```java
public void setSlot​(int index,

Object
value)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Set an indexed member in this JavaScript object

**Specified by:** setSlot

in interface

JSObject
**Implementation Requirements:** This implementation is a no-op
**Parameters:** index

- index of the member slot
**Parameters:** value

- value of the member

- keySet

```java
public
Set
<
String
> keySet()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Returns the set of all property names of this object.

**Specified by:** keySet

in interface

JSObject
**Implementation Requirements:** This implementation returns empty set
**Returns:** set of property names

- values

```java
public
Collection
<
Object
> values()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Returns the set of all property values of this object.

**Specified by:** values

in interface

JSObject
**Implementation Requirements:** This implementation returns empty set
**Returns:** set of property values.

- isInstance

```java
public boolean isInstance​(
Object
instance)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Checking whether the given object is an instance of 'this' object.

**Specified by:** isInstance

in interface

JSObject
**Implementation Requirements:** This implementation always returns false
**Parameters:** instance

- instance to check
**Returns:** true if the given 'instance' is an instance of this 'function' object

- isFunction

```java
public boolean isFunction()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Is this a function object?

**Specified by:** isFunction

in interface

JSObject
**Implementation Requirements:** This implementation always returns false
**Returns:** if this mirror wraps a ECMAScript function instance

- isStrictFunction

```java
public boolean isStrictFunction()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Is this a 'use strict' function object?

**Specified by:** isStrictFunction

in interface

JSObject
**Implementation Requirements:** This implementation always returns false
**Returns:** true if this mirror represents a ECMAScript 'use strict' function

- isArray

```java
public boolean isArray()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Is this an array object?

**Specified by:** isArray

in interface

JSObject
**Implementation Requirements:** This implementation always returns false
**Returns:** if this mirror wraps a ECMAScript array object

- toNumber

```java
@Deprecated

public double toNumber()
```

Deprecated.

use

JSObject.getDefaultValue(Class)

with

Number

hint instead.

Returns this object's numeric value.

**Specified by:** toNumber

in interface

JSObject
**Returns:** this object's numeric value.

- getDefaultValue

```java
@Deprecated

public static
Object
getDefaultValue​(
JSObject
jsobj,

Class
<?> hint)
```

Deprecated.

use

JSObject.getDefaultValue(Class)

instead.

When passed an

AbstractJSObject

, invokes its

JSObject.getDefaultValue(Class)

method. When passed any
other

JSObject

, it will obtain its

[[DefaultValue]]

method as per ECMAScript 5.1 section
8.6.2.

**Parameters:** jsobj

- the

JSObject

whose

[[DefaultValue]]

is obtained.
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
public
Object
call​(
Object
thiz,

Object
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Call this object as a JavaScript function. This is equivalent to
'func.apply(thiz, args)' in JavaScript.

**Specified by:** call

in interface

JSObject
**Implementation Requirements:** This implementation always throws UnsupportedOperationException
**Parameters:** thiz

- 'this' object to be passed to the function. This may be null.
**Parameters:** args

- arguments to method
**Returns:** result of call

---

#### call

public

Object

call​(

Object

thiz,

Object

... args)

Description copied from interface:

JSObject

Call this object as a JavaScript function. This is equivalent to
'func.apply(thiz, args)' in JavaScript.

newObject

```java
public
Object
newObject​(
Object
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Call this 'constructor' JavaScript function to create a new object.
This is equivalent to 'new func(arg1, arg2...)' in JavaScript.

**Specified by:** newObject

in interface

JSObject
**Implementation Requirements:** This implementation always throws UnsupportedOperationException
**Parameters:** args

- arguments to method
**Returns:** result of constructor call

---

#### newObject

public

Object

newObject​(

Object

... args)

Description copied from interface:

JSObject

Call this 'constructor' JavaScript function to create a new object.
This is equivalent to 'new func(arg1, arg2...)' in JavaScript.

eval

```java
public
Object
eval​(
String
s)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Evaluate a JavaScript expression.

**Specified by:** eval

in interface

JSObject
**Implementation Requirements:** This imlementation always throws UnsupportedOperationException
**Parameters:** s

- JavaScript expression to evaluate
**Returns:** evaluation result

---

#### eval

public

Object

eval​(

String

s)

Description copied from interface:

JSObject

Evaluate a JavaScript expression.

getMember

```java
public
Object
getMember​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Retrieves a named member of this JavaScript object.

**Specified by:** getMember

in interface

JSObject
**Implementation Requirements:** This implementation always returns null
**Parameters:** name

- of member
**Returns:** member

---

#### getMember

public

Object

getMember​(

String

name)

Description copied from interface:

JSObject

Retrieves a named member of this JavaScript object.

getSlot

```java
public
Object
getSlot​(int index)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Retrieves an indexed member of this JavaScript object.

**Specified by:** getSlot

in interface

JSObject
**Implementation Requirements:** This implementation always returns null
**Parameters:** index

- index slot to retrieve
**Returns:** member

---

#### getSlot

public

Object

getSlot​(int index)

Description copied from interface:

JSObject

Retrieves an indexed member of this JavaScript object.

hasMember

```java
public boolean hasMember​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Does this object have a named member?

**Specified by:** hasMember

in interface

JSObject
**Implementation Requirements:** This implementation always returns false
**Parameters:** name

- name of member
**Returns:** true if this object has a member of the given name

---

#### hasMember

public boolean hasMember​(

String

name)

Description copied from interface:

JSObject

Does this object have a named member?

hasSlot

```java
public boolean hasSlot​(int slot)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Does this object have a indexed property?

**Specified by:** hasSlot

in interface

JSObject
**Implementation Requirements:** This implementation always returns false
**Parameters:** slot

- index to check
**Returns:** true if this object has a slot

---

#### hasSlot

public boolean hasSlot​(int slot)

Description copied from interface:

JSObject

Does this object have a indexed property?

removeMember

```java
public void removeMember​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Remove a named member from this JavaScript object

**Specified by:** removeMember

in interface

JSObject
**Implementation Requirements:** This implementation is a no-op
**Parameters:** name

- name of the member

---

#### removeMember

public void removeMember​(

String

name)

Description copied from interface:

JSObject

Remove a named member from this JavaScript object

setMember

```java
public void setMember​(
String
name,

Object
value)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Set a named member in this JavaScript object

**Specified by:** setMember

in interface

JSObject
**Implementation Requirements:** This implementation is a no-op
**Parameters:** name

- name of the member
**Parameters:** value

- value of the member

---

#### setMember

public void setMember​(

String

name,

Object

value)

Description copied from interface:

JSObject

Set a named member in this JavaScript object

setSlot

```java
public void setSlot​(int index,

Object
value)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Set an indexed member in this JavaScript object

**Specified by:** setSlot

in interface

JSObject
**Implementation Requirements:** This implementation is a no-op
**Parameters:** index

- index of the member slot
**Parameters:** value

- value of the member

---

#### setSlot

public void setSlot​(int index,

Object

value)

Description copied from interface:

JSObject

Set an indexed member in this JavaScript object

keySet

```java
public
Set
<
String
> keySet()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Returns the set of all property names of this object.

**Specified by:** keySet

in interface

JSObject
**Implementation Requirements:** This implementation returns empty set
**Returns:** set of property names

---

#### keySet

public

Set

<

String

> keySet()

Description copied from interface:

JSObject

Returns the set of all property names of this object.

values

```java
public
Collection
<
Object
> values()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Returns the set of all property values of this object.

**Specified by:** values

in interface

JSObject
**Implementation Requirements:** This implementation returns empty set
**Returns:** set of property values.

---

#### values

public

Collection

<

Object

> values()

Description copied from interface:

JSObject

Returns the set of all property values of this object.

isInstance

```java
public boolean isInstance​(
Object
instance)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Checking whether the given object is an instance of 'this' object.

**Specified by:** isInstance

in interface

JSObject
**Implementation Requirements:** This implementation always returns false
**Parameters:** instance

- instance to check
**Returns:** true if the given 'instance' is an instance of this 'function' object

---

#### isInstance

public boolean isInstance​(

Object

instance)

Description copied from interface:

JSObject

Checking whether the given object is an instance of 'this' object.

isFunction

```java
public boolean isFunction()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Is this a function object?

**Specified by:** isFunction

in interface

JSObject
**Implementation Requirements:** This implementation always returns false
**Returns:** if this mirror wraps a ECMAScript function instance

---

#### isFunction

public boolean isFunction()

Description copied from interface:

JSObject

Is this a function object?

isStrictFunction

```java
public boolean isStrictFunction()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Is this a 'use strict' function object?

**Specified by:** isStrictFunction

in interface

JSObject
**Implementation Requirements:** This implementation always returns false
**Returns:** true if this mirror represents a ECMAScript 'use strict' function

---

#### isStrictFunction

public boolean isStrictFunction()

Description copied from interface:

JSObject

Is this a 'use strict' function object?

isArray

```java
public boolean isArray()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Description copied from interface:

JSObject

Is this an array object?

**Specified by:** isArray

in interface

JSObject
**Implementation Requirements:** This implementation always returns false
**Returns:** if this mirror wraps a ECMAScript array object

---

#### isArray

public boolean isArray()

Description copied from interface:

JSObject

Is this an array object?

toNumber

```java
@Deprecated

public double toNumber()
```

Deprecated.

use

JSObject.getDefaultValue(Class)

with

Number

hint instead.

Returns this object's numeric value.

**Specified by:** toNumber

in interface

JSObject
**Returns:** this object's numeric value.

---

#### toNumber

@Deprecated

public double toNumber()

Returns this object's numeric value.

getDefaultValue

```java
@Deprecated

public static
Object
getDefaultValue​(
JSObject
jsobj,

Class
<?> hint)
```

Deprecated.

use

JSObject.getDefaultValue(Class)

instead.

When passed an

AbstractJSObject

, invokes its

JSObject.getDefaultValue(Class)

method. When passed any
other

JSObject

, it will obtain its

[[DefaultValue]]

method as per ECMAScript 5.1 section
8.6.2.

**Parameters:** jsobj

- the

JSObject

whose

[[DefaultValue]]

is obtained.
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

@Deprecated

public static

Object

getDefaultValue​(

JSObject

jsobj,

Class

<?> hint)

When passed an

AbstractJSObject

, invokes its

JSObject.getDefaultValue(Class)

method. When passed any
other

JSObject

, it will obtain its

[[DefaultValue]]

method as per ECMAScript 5.1 section
8.6.2.

---

