# Interface ObjectInputFilter

**Source:** `java.base\java\io\ObjectInputFilter.html`

### Class Description

```java
@FunctionalInterface

public interface
ObjectInputFilter
```

Filter classes, array lengths, and graph metrics during deserialization.

Warning: Deserialization of untrusted data is inherently dangerous
and should be avoided. Untrusted data should be carefully validated according to the
"Serialization and Deserialization" section of the

Secure Coding Guidelines for Java SE

.

Serialization Filtering

describes best
practices for defensive use of serial filters.

If set on an

ObjectInputStream

, the

checkInput(FilterInfo)

method is called to validate classes, the length of each array,
the number of objects being read from the stream, the depth of the graph,
and the total number of bytes read from the stream.

A filter can be set via

setObjectInputFilter

for an individual ObjectInputStream.
A filter can be set via

Config.setSerialFilter

to affect every

ObjectInputStream

that does not otherwise set a filter.

A filter determines whether the arguments are

ALLOWED

or

REJECTED

and should return the appropriate status.
If the filter cannot determine the status it should return

UNDECIDED

.
Filters should be designed for the specific use case and expected types.
A filter designed for a particular use may be passed a class that is outside
of the scope of the filter. If the purpose of the filter is to reject classes
then it can reject a candidate class that matches and report UNDECIDED for others.
A filter may be called with class equals

null

,

arrayLength

equal -1,
the depth, number of references, and stream size and return a status
that reflects only one or only some of the values.
This allows a filter to be specific about the choice it is reporting and
to use other filters without forcing either allowed or rejected status.

Typically, a custom filter should check if a process-wide filter
is configured and defer to it if so. For example,

```java
ObjectInputFilter.Status checkInput(FilterInfo info) {
ObjectInputFilter serialFilter = ObjectInputFilter.Config.getSerialFilter();
if (serialFilter != null) {
ObjectInputFilter.Status status = serialFilter.checkInput(info);
if (status != ObjectInputFilter.Status.UNDECIDED) {
// The process-wide filter overrides this filter
return status;
}
}
if (info.serialClass() != null &&
Remote.class.isAssignableFrom(info.serialClass())) {
return Status.REJECTED; // Do not allow Remote objects
}
return Status.UNDECIDED;
}
```

Unless otherwise noted, passing a

null

argument to a
method in this interface and its nested classes will cause a

NullPointerException

to be thrown.

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ObjectInputFilter.Status
checkInput​(
ObjectInputFilter.FilterInfo
filterInfo)

Check the class, array length, number of object references, depth,
stream size, and other available filtering information.
Implementations of this method check the contents of the object graph being created
during deserialization. The filter returns

Status.ALLOWED

,

Status.REJECTED

, or

Status.UNDECIDED

.

**Parameters:**
- filterInfo

- provides information about the current object being deserialized,
if any, and the status of the

ObjectInputStream

**Returns:**
- Status.ALLOWED

if accepted,

Status.REJECTED

if rejected,

Status.UNDECIDED

if undecided.

---

### Additional Sections

#### Interface ObjectInputFilter

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
ObjectInputFilter
```

Filter classes, array lengths, and graph metrics during deserialization.

Warning: Deserialization of untrusted data is inherently dangerous
and should be avoided. Untrusted data should be carefully validated according to the
"Serialization and Deserialization" section of the

Secure Coding Guidelines for Java SE

.

Serialization Filtering

describes best
practices for defensive use of serial filters.

If set on an

ObjectInputStream

, the

checkInput(FilterInfo)

method is called to validate classes, the length of each array,
the number of objects being read from the stream, the depth of the graph,
and the total number of bytes read from the stream.

A filter can be set via

setObjectInputFilter

for an individual ObjectInputStream.
A filter can be set via

Config.setSerialFilter

to affect every

ObjectInputStream

that does not otherwise set a filter.

A filter determines whether the arguments are

ALLOWED

or

REJECTED

and should return the appropriate status.
If the filter cannot determine the status it should return

UNDECIDED

.
Filters should be designed for the specific use case and expected types.
A filter designed for a particular use may be passed a class that is outside
of the scope of the filter. If the purpose of the filter is to reject classes
then it can reject a candidate class that matches and report UNDECIDED for others.
A filter may be called with class equals

null

,

arrayLength

equal -1,
the depth, number of references, and stream size and return a status
that reflects only one or only some of the values.
This allows a filter to be specific about the choice it is reporting and
to use other filters without forcing either allowed or rejected status.

Typically, a custom filter should check if a process-wide filter
is configured and defer to it if so. For example,

```java
ObjectInputFilter.Status checkInput(FilterInfo info) {
ObjectInputFilter serialFilter = ObjectInputFilter.Config.getSerialFilter();
if (serialFilter != null) {
ObjectInputFilter.Status status = serialFilter.checkInput(info);
if (status != ObjectInputFilter.Status.UNDECIDED) {
// The process-wide filter overrides this filter
return status;
}
}
if (info.serialClass() != null &&
Remote.class.isAssignableFrom(info.serialClass())) {
return Status.REJECTED; // Do not allow Remote objects
}
return Status.UNDECIDED;
}
```

Unless otherwise noted, passing a

null

argument to a
method in this interface and its nested classes will cause a

NullPointerException

to be thrown.

**Since:** 9
**See Also:** ObjectInputStream.setObjectInputFilter(ObjectInputFilter)

@FunctionalInterface

public interface

ObjectInputFilter

Filter classes, array lengths, and graph metrics during deserialization.

Warning: Deserialization of untrusted data is inherently dangerous
and should be avoided. Untrusted data should be carefully validated according to the
"Serialization and Deserialization" section of the

Secure Coding Guidelines for Java SE

.

Serialization Filtering

describes best
practices for defensive use of serial filters.

If set on an

ObjectInputStream

, the

checkInput(FilterInfo)

method is called to validate classes, the length of each array,
the number of objects being read from the stream, the depth of the graph,
and the total number of bytes read from the stream.

A filter can be set via

setObjectInputFilter

for an individual ObjectInputStream.
A filter can be set via

Config.setSerialFilter

to affect every

ObjectInputStream

that does not otherwise set a filter.

A filter determines whether the arguments are

ALLOWED

or

REJECTED

and should return the appropriate status.
If the filter cannot determine the status it should return

UNDECIDED

.
Filters should be designed for the specific use case and expected types.
A filter designed for a particular use may be passed a class that is outside
of the scope of the filter. If the purpose of the filter is to reject classes
then it can reject a candidate class that matches and report UNDECIDED for others.
A filter may be called with class equals

null

,

arrayLength

equal -1,
the depth, number of references, and stream size and return a status
that reflects only one or only some of the values.
This allows a filter to be specific about the choice it is reporting and
to use other filters without forcing either allowed or rejected status.

Typically, a custom filter should check if a process-wide filter
is configured and defer to it if so. For example,

```java
ObjectInputFilter.Status checkInput(FilterInfo info) {
ObjectInputFilter serialFilter = ObjectInputFilter.Config.getSerialFilter();
if (serialFilter != null) {
ObjectInputFilter.Status status = serialFilter.checkInput(info);
if (status != ObjectInputFilter.Status.UNDECIDED) {
// The process-wide filter overrides this filter
return status;
}
}
if (info.serialClass() != null &&
Remote.class.isAssignableFrom(info.serialClass())) {
return Status.REJECTED; // Do not allow Remote objects
}
return Status.UNDECIDED;
}
```

Unless otherwise noted, passing a

null

argument to a
method in this interface and its nested classes will cause a

NullPointerException

to be thrown.

Warning: Deserialization of untrusted data is inherently dangerous
and should be avoided. Untrusted data should be carefully validated according to the
"Serialization and Deserialization" section of the

Secure Coding Guidelines for Java SE

.

Serialization Filtering

describes best
practices for defensive use of serial filters.

A filter can be set via

setObjectInputFilter

for an individual ObjectInputStream.
A filter can be set via

Config.setSerialFilter

to affect every

ObjectInputStream

that does not otherwise set a filter.

A filter determines whether the arguments are

ALLOWED

or

REJECTED

and should return the appropriate status.
If the filter cannot determine the status it should return

UNDECIDED

.
Filters should be designed for the specific use case and expected types.
A filter designed for a particular use may be passed a class that is outside
of the scope of the filter. If the purpose of the filter is to reject classes
then it can reject a candidate class that matches and report UNDECIDED for others.
A filter may be called with class equals

null

,

arrayLength

equal -1,
the depth, number of references, and stream size and return a status
that reflects only one or only some of the values.
This allows a filter to be specific about the choice it is reporting and
to use other filters without forcing either allowed or rejected status.

Typically, a custom filter should check if a process-wide filter
is configured and defer to it if so. For example,

```java
ObjectInputFilter.Status checkInput(FilterInfo info) {
ObjectInputFilter serialFilter = ObjectInputFilter.Config.getSerialFilter();
if (serialFilter != null) {
ObjectInputFilter.Status status = serialFilter.checkInput(info);
if (status != ObjectInputFilter.Status.UNDECIDED) {
// The process-wide filter overrides this filter
return status;
}
}
if (info.serialClass() != null &&
Remote.class.isAssignableFrom(info.serialClass())) {
return Status.REJECTED; // Do not allow Remote objects
}
return Status.UNDECIDED;
}
```

Unless otherwise noted, passing a

null

argument to a
method in this interface and its nested classes will cause a

NullPointerException

to be thrown.

A filter determines whether the arguments are

ALLOWED

or

REJECTED

and should return the appropriate status.
If the filter cannot determine the status it should return

UNDECIDED

.
Filters should be designed for the specific use case and expected types.
A filter designed for a particular use may be passed a class that is outside
of the scope of the filter. If the purpose of the filter is to reject classes
then it can reject a candidate class that matches and report UNDECIDED for others.
A filter may be called with class equals

null

,

arrayLength

equal -1,
the depth, number of references, and stream size and return a status
that reflects only one or only some of the values.
This allows a filter to be specific about the choice it is reporting and
to use other filters without forcing either allowed or rejected status.

Typically, a custom filter should check if a process-wide filter
is configured and defer to it if so. For example,

```java
ObjectInputFilter.Status checkInput(FilterInfo info) {
ObjectInputFilter serialFilter = ObjectInputFilter.Config.getSerialFilter();
if (serialFilter != null) {
ObjectInputFilter.Status status = serialFilter.checkInput(info);
if (status != ObjectInputFilter.Status.UNDECIDED) {
// The process-wide filter overrides this filter
return status;
}
}
if (info.serialClass() != null &&
Remote.class.isAssignableFrom(info.serialClass())) {
return Status.REJECTED; // Do not allow Remote objects
}
return Status.UNDECIDED;
}
```

Unless otherwise noted, passing a

null

argument to a
method in this interface and its nested classes will cause a

NullPointerException

to be thrown.

Typically, a custom filter should check if a process-wide filter
is configured and defer to it if so. For example,

```java
ObjectInputFilter.Status checkInput(FilterInfo info) {
ObjectInputFilter serialFilter = ObjectInputFilter.Config.getSerialFilter();
if (serialFilter != null) {
ObjectInputFilter.Status status = serialFilter.checkInput(info);
if (status != ObjectInputFilter.Status.UNDECIDED) {
// The process-wide filter overrides this filter
return status;
}
}
if (info.serialClass() != null &&
Remote.class.isAssignableFrom(info.serialClass())) {
return Status.REJECTED; // Do not allow Remote objects
}
return Status.UNDECIDED;
}
```

Unless otherwise noted, passing a

null

argument to a
method in this interface and its nested classes will cause a

NullPointerException

to be thrown.

ObjectInputFilter.Status checkInput(FilterInfo info) {
ObjectInputFilter serialFilter = ObjectInputFilter.Config.getSerialFilter();
if (serialFilter != null) {
ObjectInputFilter.Status status = serialFilter.checkInput(info);
if (status != ObjectInputFilter.Status.UNDECIDED) {
// The process-wide filter overrides this filter
return status;
}
}
if (info.serialClass() != null &&
Remote.class.isAssignableFrom(info.serialClass())) {
return Status.REJECTED; // Do not allow Remote objects
}
return Status.UNDECIDED;
}

Unless otherwise noted, passing a

null

argument to a
method in this interface and its nested classes will cause a

NullPointerException

to be thrown.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

ObjectInputFilter.Config

A utility class to set and get the process-wide filter or create a filter
from a pattern string.

static interface

ObjectInputFilter.FilterInfo

FilterInfo provides access to information about the current object
being deserialized and the status of the

ObjectInputStream

.

static class

ObjectInputFilter.Status

The status of a check on the class, array length, number of references,
depth, and stream size.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ObjectInputFilter.Status

checkInput

​(

ObjectInputFilter.FilterInfo

filterInfo)

Check the class, array length, number of object references, depth,
stream size, and other available filtering information.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

ObjectInputFilter.Config

A utility class to set and get the process-wide filter or create a filter
from a pattern string.

static interface

ObjectInputFilter.FilterInfo

FilterInfo provides access to information about the current object
being deserialized and the status of the

ObjectInputStream

.

static class

ObjectInputFilter.Status

The status of a check on the class, array length, number of references,
depth, and stream size.

---

#### Nested Class Summary

A utility class to set and get the process-wide filter or create a filter
from a pattern string.

FilterInfo provides access to information about the current object
being deserialized and the status of the

ObjectInputStream

.

The status of a check on the class, array length, number of references,
depth, and stream size.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ObjectInputFilter.Status

checkInput

​(

ObjectInputFilter.FilterInfo

filterInfo)

Check the class, array length, number of object references, depth,
stream size, and other available filtering information.

---

#### Method Summary

Check the class, array length, number of object references, depth,
stream size, and other available filtering information.

============ METHOD DETAIL ==========

- Method Detail

- checkInput

```java
ObjectInputFilter.Status
checkInput​(
ObjectInputFilter.FilterInfo
filterInfo)
```

Check the class, array length, number of object references, depth,
stream size, and other available filtering information.
Implementations of this method check the contents of the object graph being created
during deserialization. The filter returns

Status.ALLOWED

,

Status.REJECTED

, or

Status.UNDECIDED

.

**Parameters:** filterInfo

- provides information about the current object being deserialized,
if any, and the status of the

ObjectInputStream
**Returns:** Status.ALLOWED

if accepted,

Status.REJECTED

if rejected,

Status.UNDECIDED

if undecided.

Method Detail

- checkInput

```java
ObjectInputFilter.Status
checkInput​(
ObjectInputFilter.FilterInfo
filterInfo)
```

Check the class, array length, number of object references, depth,
stream size, and other available filtering information.
Implementations of this method check the contents of the object graph being created
during deserialization. The filter returns

Status.ALLOWED

,

Status.REJECTED

, or

Status.UNDECIDED

.

**Parameters:** filterInfo

- provides information about the current object being deserialized,
if any, and the status of the

ObjectInputStream
**Returns:** Status.ALLOWED

if accepted,

Status.REJECTED

if rejected,

Status.UNDECIDED

if undecided.

---

#### Method Detail

checkInput

```java
ObjectInputFilter.Status
checkInput​(
ObjectInputFilter.FilterInfo
filterInfo)
```

Check the class, array length, number of object references, depth,
stream size, and other available filtering information.
Implementations of this method check the contents of the object graph being created
during deserialization. The filter returns

Status.ALLOWED

,

Status.REJECTED

, or

Status.UNDECIDED

.

**Parameters:** filterInfo

- provides information about the current object being deserialized,
if any, and the status of the

ObjectInputStream
**Returns:** Status.ALLOWED

if accepted,

Status.REJECTED

if rejected,

Status.UNDECIDED

if undecided.

---

#### checkInput

ObjectInputFilter.Status

checkInput​(

ObjectInputFilter.FilterInfo

filterInfo)

Check the class, array length, number of object references, depth,
stream size, and other available filtering information.
Implementations of this method check the contents of the object graph being created
during deserialization. The filter returns

Status.ALLOWED

,

Status.REJECTED

, or

Status.UNDECIDED

.

---

