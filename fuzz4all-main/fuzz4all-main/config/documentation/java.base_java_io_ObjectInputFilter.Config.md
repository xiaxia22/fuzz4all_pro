# Class ObjectInputFilter.Config

**Source:** `java.base\java\io\ObjectInputFilter.Config.html`

### Class Description

```java
public static final class
ObjectInputFilter.Config

extends
Object
```

A utility class to set and get the process-wide filter or create a filter
from a pattern string. If a process-wide filter is set, it will be
used for each

ObjectInputStream

that does not set its own filter.

When setting the filter, it should be stateless and idempotent,
reporting the same result when passed the same arguments.

The filter is configured during the initialization of the

ObjectInputFilter.Config

class. For example, by calling

Config.getSerialFilter

.
If the system property

jdk.serialFilter

is defined, it is used
to configure the filter.
If the system property is not defined, and the

Security

property

jdk.serialFilter

is defined then it is used to configure the filter.
Otherwise, the filter is not configured during initialization.
The syntax for each property is the same as for the

createFilter

method.
If a filter is not configured, it can be set with

Config.setSerialFilter

.

**Enclosing interface:** ObjectInputFilter

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
ObjectInputFilter
getSerialFilter()

Returns the process-wide serialization filter or

null

if not configured.

**Returns:**
- the process-wide serialization filter or

null

if not configured

---

#### public static void setSerialFilter​(
ObjectInputFilter
filter)

Set the process-wide filter if it has not already been configured or set.

**Parameters:**
- filter

- the serialization filter to set as the process-wide filter; not null

**Throws:**
- SecurityException

- if there is security manager and the

SerializablePermission("serialFilter")

is not granted
- IllegalStateException

- if the filter has already been set

non-null

---

#### public static
ObjectInputFilter
createFilter​(
String
pattern)

Returns an ObjectInputFilter from a string of patterns.

Patterns are separated by ";" (semicolon). Whitespace is significant and
is considered part of the pattern.
If a pattern includes an equals assignment, "

=

" it sets a limit.
If a limit appears more than once the last value is used.

- maxdepth=

value

- the maximum depth of a graph
- maxrefs=

value

- the maximum number of internal references
- maxbytes=

value

- the maximum number of bytes in the input stream
- maxarray=

value

- the maximum array length allowed

Other patterns match or reject class or package name
as returned from

Class.getName()

and
if an optional module name is present

class.getModule().getName()

.
Note that for arrays the element type is used in the pattern,
not the array type.

- If the pattern starts with "!", the class is rejected if the remaining pattern is matched;
otherwise the class is allowed if the pattern matches.

If the pattern contains "/", the non-empty prefix up to the "/" is the module name;
if the module name matches the module name of the class then
the remaining pattern is matched with the class name.
If there is no "/", the module name is not compared.

If the pattern ends with ".**" it matches any class in the package and all subpackages.

If the pattern ends with ".*" it matches any class in the package.

If the pattern ends with "*", it matches any class with the pattern as a prefix.

If the pattern is equal to the class name, it matches.

Otherwise, the pattern is not matched.

The resulting filter performs the limit checks and then
tries to match the class, if any. If any of the limits are exceeded,
the filter returns

Status.REJECTED

.
If the class is an array type, the class to be matched is the element type.
Arrays of any number of dimensions are treated the same as the element type.
For example, a pattern of "

!example.Foo

",
rejects creation of any instance or array of

example.Foo

.
The first pattern that matches, working from left to right, determines
the

Status.ALLOWED

or

Status.REJECTED

result.
If the limits are not exceeded and no pattern matches the class,
the result is

Status.UNDECIDED

.

**Parameters:**
- pattern

- the pattern string to parse; not null

**Returns:**
- a filter to check a class being deserialized;

null

if no patterns

**Throws:**
- IllegalArgumentException

- if the pattern string is illegal or
malformed and cannot be parsed.
In particular, if any of the following is true:

- if a limit is missing the name or the name is not one of
"maxdepth", "maxrefs", "maxbytes", or "maxarray"

if the value of the limit can not be parsed by

Long.parseLong

or is negative

if the pattern contains "/" and the module name is missing
or the remaining pattern is empty

if the package is missing for ".*" and ".**"

---

### Additional Sections

#### Class ObjectInputFilter.Config

java.lang.Object

- java.io.ObjectInputFilter.Config

java.io.ObjectInputFilter.Config

**Enclosing interface:** ObjectInputFilter

```java
public static final class
ObjectInputFilter.Config

extends
Object
```

A utility class to set and get the process-wide filter or create a filter
from a pattern string. If a process-wide filter is set, it will be
used for each

ObjectInputStream

that does not set its own filter.

When setting the filter, it should be stateless and idempotent,
reporting the same result when passed the same arguments.

The filter is configured during the initialization of the

ObjectInputFilter.Config

class. For example, by calling

Config.getSerialFilter

.
If the system property

jdk.serialFilter

is defined, it is used
to configure the filter.
If the system property is not defined, and the

Security

property

jdk.serialFilter

is defined then it is used to configure the filter.
Otherwise, the filter is not configured during initialization.
The syntax for each property is the same as for the

createFilter

method.
If a filter is not configured, it can be set with

Config.setSerialFilter

.

**Since:** 9

public static final class

ObjectInputFilter.Config

extends

Object

A utility class to set and get the process-wide filter or create a filter
from a pattern string. If a process-wide filter is set, it will be
used for each

ObjectInputStream

that does not set its own filter.

When setting the filter, it should be stateless and idempotent,
reporting the same result when passed the same arguments.

The filter is configured during the initialization of the

ObjectInputFilter.Config

class. For example, by calling

Config.getSerialFilter

.
If the system property

jdk.serialFilter

is defined, it is used
to configure the filter.
If the system property is not defined, and the

Security

property

jdk.serialFilter

is defined then it is used to configure the filter.
Otherwise, the filter is not configured during initialization.
The syntax for each property is the same as for the

createFilter

method.
If a filter is not configured, it can be set with

Config.setSerialFilter

.

When setting the filter, it should be stateless and idempotent,
reporting the same result when passed the same arguments.

The filter is configured during the initialization of the

ObjectInputFilter.Config

class. For example, by calling

Config.getSerialFilter

.
If the system property

jdk.serialFilter

is defined, it is used
to configure the filter.
If the system property is not defined, and the

Security

property

jdk.serialFilter

is defined then it is used to configure the filter.
Otherwise, the filter is not configured during initialization.
The syntax for each property is the same as for the

createFilter

method.
If a filter is not configured, it can be set with

Config.setSerialFilter

.

The filter is configured during the initialization of the

ObjectInputFilter.Config

class. For example, by calling

Config.getSerialFilter

.
If the system property

jdk.serialFilter

is defined, it is used
to configure the filter.
If the system property is not defined, and the

Security

property

jdk.serialFilter

is defined then it is used to configure the filter.
Otherwise, the filter is not configured during initialization.
The syntax for each property is the same as for the

createFilter

method.
If a filter is not configured, it can be set with

Config.setSerialFilter

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ObjectInputFilter

createFilter

​(

String

pattern)

Returns an ObjectInputFilter from a string of patterns.

static

ObjectInputFilter

getSerialFilter

()

Returns the process-wide serialization filter or

null

if not configured.

static void

setSerialFilter

​(

ObjectInputFilter

filter)

Set the process-wide filter if it has not already been configured or set.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ObjectInputFilter

createFilter

​(

String

pattern)

Returns an ObjectInputFilter from a string of patterns.

static

ObjectInputFilter

getSerialFilter

()

Returns the process-wide serialization filter or

null

if not configured.

static void

setSerialFilter

​(

ObjectInputFilter

filter)

Set the process-wide filter if it has not already been configured or set.

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

Returns an ObjectInputFilter from a string of patterns.

Returns the process-wide serialization filter or

null

if not configured.

Set the process-wide filter if it has not already been configured or set.

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

- getSerialFilter

```java
public static
ObjectInputFilter
getSerialFilter()
```

Returns the process-wide serialization filter or

null

if not configured.

**Returns:** the process-wide serialization filter or

null

if not configured

- setSerialFilter

```java
public static void setSerialFilter​(
ObjectInputFilter
filter)
```

Set the process-wide filter if it has not already been configured or set.

**Parameters:** filter

- the serialization filter to set as the process-wide filter; not null
**Throws:** SecurityException

- if there is security manager and the

SerializablePermission("serialFilter")

is not granted
**Throws:** IllegalStateException

- if the filter has already been set

non-null

- createFilter

```java
public static
ObjectInputFilter
createFilter​(
String
pattern)
```

Returns an ObjectInputFilter from a string of patterns.

Patterns are separated by ";" (semicolon). Whitespace is significant and
is considered part of the pattern.
If a pattern includes an equals assignment, "

=

" it sets a limit.
If a limit appears more than once the last value is used.

- maxdepth=

value

- the maximum depth of a graph
- maxrefs=

value

- the maximum number of internal references
- maxbytes=

value

- the maximum number of bytes in the input stream
- maxarray=

value

- the maximum array length allowed

Other patterns match or reject class or package name
as returned from

Class.getName()

and
if an optional module name is present

class.getModule().getName()

.
Note that for arrays the element type is used in the pattern,
not the array type.

- If the pattern starts with "!", the class is rejected if the remaining pattern is matched;
otherwise the class is allowed if the pattern matches.

If the pattern contains "/", the non-empty prefix up to the "/" is the module name;
if the module name matches the module name of the class then
the remaining pattern is matched with the class name.
If there is no "/", the module name is not compared.

If the pattern ends with ".**" it matches any class in the package and all subpackages.

If the pattern ends with ".*" it matches any class in the package.

If the pattern ends with "*", it matches any class with the pattern as a prefix.

If the pattern is equal to the class name, it matches.

Otherwise, the pattern is not matched.

The resulting filter performs the limit checks and then
tries to match the class, if any. If any of the limits are exceeded,
the filter returns

Status.REJECTED

.
If the class is an array type, the class to be matched is the element type.
Arrays of any number of dimensions are treated the same as the element type.
For example, a pattern of "

!example.Foo

",
rejects creation of any instance or array of

example.Foo

.
The first pattern that matches, working from left to right, determines
the

Status.ALLOWED

or

Status.REJECTED

result.
If the limits are not exceeded and no pattern matches the class,
the result is

Status.UNDECIDED

.

**Parameters:** pattern

- the pattern string to parse; not null
**Returns:** a filter to check a class being deserialized;

null

if no patterns
**Throws:** IllegalArgumentException

- if the pattern string is illegal or
malformed and cannot be parsed.
In particular, if any of the following is true:

- if a limit is missing the name or the name is not one of
"maxdepth", "maxrefs", "maxbytes", or "maxarray"

if the value of the limit can not be parsed by

Long.parseLong

or is negative

if the pattern contains "/" and the module name is missing
or the remaining pattern is empty

if the package is missing for ".*" and ".**"

Method Detail

- getSerialFilter

```java
public static
ObjectInputFilter
getSerialFilter()
```

Returns the process-wide serialization filter or

null

if not configured.

**Returns:** the process-wide serialization filter or

null

if not configured

- setSerialFilter

```java
public static void setSerialFilter​(
ObjectInputFilter
filter)
```

Set the process-wide filter if it has not already been configured or set.

**Parameters:** filter

- the serialization filter to set as the process-wide filter; not null
**Throws:** SecurityException

- if there is security manager and the

SerializablePermission("serialFilter")

is not granted
**Throws:** IllegalStateException

- if the filter has already been set

non-null

- createFilter

```java
public static
ObjectInputFilter
createFilter​(
String
pattern)
```

Returns an ObjectInputFilter from a string of patterns.

Patterns are separated by ";" (semicolon). Whitespace is significant and
is considered part of the pattern.
If a pattern includes an equals assignment, "

=

" it sets a limit.
If a limit appears more than once the last value is used.

- maxdepth=

value

- the maximum depth of a graph
- maxrefs=

value

- the maximum number of internal references
- maxbytes=

value

- the maximum number of bytes in the input stream
- maxarray=

value

- the maximum array length allowed

Other patterns match or reject class or package name
as returned from

Class.getName()

and
if an optional module name is present

class.getModule().getName()

.
Note that for arrays the element type is used in the pattern,
not the array type.

- If the pattern starts with "!", the class is rejected if the remaining pattern is matched;
otherwise the class is allowed if the pattern matches.

If the pattern contains "/", the non-empty prefix up to the "/" is the module name;
if the module name matches the module name of the class then
the remaining pattern is matched with the class name.
If there is no "/", the module name is not compared.

If the pattern ends with ".**" it matches any class in the package and all subpackages.

If the pattern ends with ".*" it matches any class in the package.

If the pattern ends with "*", it matches any class with the pattern as a prefix.

If the pattern is equal to the class name, it matches.

Otherwise, the pattern is not matched.

The resulting filter performs the limit checks and then
tries to match the class, if any. If any of the limits are exceeded,
the filter returns

Status.REJECTED

.
If the class is an array type, the class to be matched is the element type.
Arrays of any number of dimensions are treated the same as the element type.
For example, a pattern of "

!example.Foo

",
rejects creation of any instance or array of

example.Foo

.
The first pattern that matches, working from left to right, determines
the

Status.ALLOWED

or

Status.REJECTED

result.
If the limits are not exceeded and no pattern matches the class,
the result is

Status.UNDECIDED

.

**Parameters:** pattern

- the pattern string to parse; not null
**Returns:** a filter to check a class being deserialized;

null

if no patterns
**Throws:** IllegalArgumentException

- if the pattern string is illegal or
malformed and cannot be parsed.
In particular, if any of the following is true:

- if a limit is missing the name or the name is not one of
"maxdepth", "maxrefs", "maxbytes", or "maxarray"

if the value of the limit can not be parsed by

Long.parseLong

or is negative

if the pattern contains "/" and the module name is missing
or the remaining pattern is empty

if the package is missing for ".*" and ".**"

---

#### Method Detail

getSerialFilter

```java
public static
ObjectInputFilter
getSerialFilter()
```

Returns the process-wide serialization filter or

null

if not configured.

**Returns:** the process-wide serialization filter or

null

if not configured

---

#### getSerialFilter

public static

ObjectInputFilter

getSerialFilter()

Returns the process-wide serialization filter or

null

if not configured.

setSerialFilter

```java
public static void setSerialFilter​(
ObjectInputFilter
filter)
```

Set the process-wide filter if it has not already been configured or set.

**Parameters:** filter

- the serialization filter to set as the process-wide filter; not null
**Throws:** SecurityException

- if there is security manager and the

SerializablePermission("serialFilter")

is not granted
**Throws:** IllegalStateException

- if the filter has already been set

non-null

---

#### setSerialFilter

public static void setSerialFilter​(

ObjectInputFilter

filter)

Set the process-wide filter if it has not already been configured or set.

createFilter

```java
public static
ObjectInputFilter
createFilter​(
String
pattern)
```

Returns an ObjectInputFilter from a string of patterns.

Patterns are separated by ";" (semicolon). Whitespace is significant and
is considered part of the pattern.
If a pattern includes an equals assignment, "

=

" it sets a limit.
If a limit appears more than once the last value is used.

- maxdepth=

value

- the maximum depth of a graph
- maxrefs=

value

- the maximum number of internal references
- maxbytes=

value

- the maximum number of bytes in the input stream
- maxarray=

value

- the maximum array length allowed

Other patterns match or reject class or package name
as returned from

Class.getName()

and
if an optional module name is present

class.getModule().getName()

.
Note that for arrays the element type is used in the pattern,
not the array type.

- If the pattern starts with "!", the class is rejected if the remaining pattern is matched;
otherwise the class is allowed if the pattern matches.

If the pattern contains "/", the non-empty prefix up to the "/" is the module name;
if the module name matches the module name of the class then
the remaining pattern is matched with the class name.
If there is no "/", the module name is not compared.

If the pattern ends with ".**" it matches any class in the package and all subpackages.

If the pattern ends with ".*" it matches any class in the package.

If the pattern ends with "*", it matches any class with the pattern as a prefix.

If the pattern is equal to the class name, it matches.

Otherwise, the pattern is not matched.

The resulting filter performs the limit checks and then
tries to match the class, if any. If any of the limits are exceeded,
the filter returns

Status.REJECTED

.
If the class is an array type, the class to be matched is the element type.
Arrays of any number of dimensions are treated the same as the element type.
For example, a pattern of "

!example.Foo

",
rejects creation of any instance or array of

example.Foo

.
The first pattern that matches, working from left to right, determines
the

Status.ALLOWED

or

Status.REJECTED

result.
If the limits are not exceeded and no pattern matches the class,
the result is

Status.UNDECIDED

.

**Parameters:** pattern

- the pattern string to parse; not null
**Returns:** a filter to check a class being deserialized;

null

if no patterns
**Throws:** IllegalArgumentException

- if the pattern string is illegal or
malformed and cannot be parsed.
In particular, if any of the following is true:

- if a limit is missing the name or the name is not one of
"maxdepth", "maxrefs", "maxbytes", or "maxarray"

if the value of the limit can not be parsed by

Long.parseLong

or is negative

if the pattern contains "/" and the module name is missing
or the remaining pattern is empty

if the package is missing for ".*" and ".**"

---

#### createFilter

public static

ObjectInputFilter

createFilter​(

String

pattern)

Returns an ObjectInputFilter from a string of patterns.

Patterns are separated by ";" (semicolon). Whitespace is significant and
is considered part of the pattern.
If a pattern includes an equals assignment, "

=

" it sets a limit.
If a limit appears more than once the last value is used.

- maxdepth=

value

- the maximum depth of a graph
- maxrefs=

value

- the maximum number of internal references
- maxbytes=

value

- the maximum number of bytes in the input stream
- maxarray=

value

- the maximum array length allowed

Other patterns match or reject class or package name
as returned from

Class.getName()

and
if an optional module name is present

class.getModule().getName()

.
Note that for arrays the element type is used in the pattern,
not the array type.

- If the pattern starts with "!", the class is rejected if the remaining pattern is matched;
otherwise the class is allowed if the pattern matches.

If the pattern contains "/", the non-empty prefix up to the "/" is the module name;
if the module name matches the module name of the class then
the remaining pattern is matched with the class name.
If there is no "/", the module name is not compared.

If the pattern ends with ".**" it matches any class in the package and all subpackages.

If the pattern ends with ".*" it matches any class in the package.

If the pattern ends with "*", it matches any class with the pattern as a prefix.

If the pattern is equal to the class name, it matches.

Otherwise, the pattern is not matched.

The resulting filter performs the limit checks and then
tries to match the class, if any. If any of the limits are exceeded,
the filter returns

Status.REJECTED

.
If the class is an array type, the class to be matched is the element type.
Arrays of any number of dimensions are treated the same as the element type.
For example, a pattern of "

!example.Foo

",
rejects creation of any instance or array of

example.Foo

.
The first pattern that matches, working from left to right, determines
the

Status.ALLOWED

or

Status.REJECTED

result.
If the limits are not exceeded and no pattern matches the class,
the result is

Status.UNDECIDED

.

Patterns are separated by ";" (semicolon). Whitespace is significant and
is considered part of the pattern.
If a pattern includes an equals assignment, "

=

" it sets a limit.
If a limit appears more than once the last value is used.

- maxdepth=

value

- the maximum depth of a graph
- maxrefs=

value

- the maximum number of internal references
- maxbytes=

value

- the maximum number of bytes in the input stream
- maxarray=

value

- the maximum array length allowed

Other patterns match or reject class or package name
as returned from

Class.getName()

and
if an optional module name is present

class.getModule().getName()

.
Note that for arrays the element type is used in the pattern,
not the array type.

- If the pattern starts with "!", the class is rejected if the remaining pattern is matched;
otherwise the class is allowed if the pattern matches.

If the pattern contains "/", the non-empty prefix up to the "/" is the module name;
if the module name matches the module name of the class then
the remaining pattern is matched with the class name.
If there is no "/", the module name is not compared.

If the pattern ends with ".**" it matches any class in the package and all subpackages.

If the pattern ends with ".*" it matches any class in the package.

If the pattern ends with "*", it matches any class with the pattern as a prefix.

If the pattern is equal to the class name, it matches.

Otherwise, the pattern is not matched.

The resulting filter performs the limit checks and then
tries to match the class, if any. If any of the limits are exceeded,
the filter returns

Status.REJECTED

.
If the class is an array type, the class to be matched is the element type.
Arrays of any number of dimensions are treated the same as the element type.
For example, a pattern of "

!example.Foo

",
rejects creation of any instance or array of

example.Foo

.
The first pattern that matches, working from left to right, determines
the

Status.ALLOWED

or

Status.REJECTED

result.
If the limits are not exceeded and no pattern matches the class,
the result is

Status.UNDECIDED

.

maxdepth=

value

- the maximum depth of a graph

maxrefs=

value

- the maximum number of internal references

maxbytes=

value

- the maximum number of bytes in the input stream

maxarray=

value

- the maximum array length allowed

Other patterns match or reject class or package name
as returned from

Class.getName()

and
if an optional module name is present

class.getModule().getName()

.
Note that for arrays the element type is used in the pattern,
not the array type.

- If the pattern starts with "!", the class is rejected if the remaining pattern is matched;
otherwise the class is allowed if the pattern matches.

If the pattern contains "/", the non-empty prefix up to the "/" is the module name;
if the module name matches the module name of the class then
the remaining pattern is matched with the class name.
If there is no "/", the module name is not compared.

If the pattern ends with ".**" it matches any class in the package and all subpackages.

If the pattern ends with ".*" it matches any class in the package.

If the pattern ends with "*", it matches any class with the pattern as a prefix.

If the pattern is equal to the class name, it matches.

Otherwise, the pattern is not matched.

The resulting filter performs the limit checks and then
tries to match the class, if any. If any of the limits are exceeded,
the filter returns

Status.REJECTED

.
If the class is an array type, the class to be matched is the element type.
Arrays of any number of dimensions are treated the same as the element type.
For example, a pattern of "

!example.Foo

",
rejects creation of any instance or array of

example.Foo

.
The first pattern that matches, working from left to right, determines
the

Status.ALLOWED

or

Status.REJECTED

result.
If the limits are not exceeded and no pattern matches the class,
the result is

Status.UNDECIDED

.

If the pattern starts with "!", the class is rejected if the remaining pattern is matched;
otherwise the class is allowed if the pattern matches.

If the pattern contains "/", the non-empty prefix up to the "/" is the module name;
if the module name matches the module name of the class then
the remaining pattern is matched with the class name.
If there is no "/", the module name is not compared.

If the pattern ends with ".**" it matches any class in the package and all subpackages.

If the pattern ends with ".*" it matches any class in the package.

If the pattern ends with "*", it matches any class with the pattern as a prefix.

If the pattern is equal to the class name, it matches.

Otherwise, the pattern is not matched.

The resulting filter performs the limit checks and then
tries to match the class, if any. If any of the limits are exceeded,
the filter returns

Status.REJECTED

.
If the class is an array type, the class to be matched is the element type.
Arrays of any number of dimensions are treated the same as the element type.
For example, a pattern of "

!example.Foo

",
rejects creation of any instance or array of

example.Foo

.
The first pattern that matches, working from left to right, determines
the

Status.ALLOWED

or

Status.REJECTED

result.
If the limits are not exceeded and no pattern matches the class,
the result is

Status.UNDECIDED

.

if a limit is missing the name or the name is not one of
"maxdepth", "maxrefs", "maxbytes", or "maxarray"

if the value of the limit can not be parsed by

Long.parseLong

or is negative

if the pattern contains "/" and the module name is missing
or the remaining pattern is empty

if the package is missing for ".*" and ".**"

---

