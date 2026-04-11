# Interface LinkRequest

**Source:** `jdk.dynalink\jdk\dynalink\linker\LinkRequest.html`

### Class Description

```java
public interface
LinkRequest
```

Represents a request to link a particular invocation at a particular call
site. Instances of these requests will be constructed and passed to all

GuardingDynamicLinker

objects managed by the

DynamicLinker

that is trying to link the call site.

**All Known Implementing Classes:** SimpleLinkRequest

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### CallSiteDescriptor
getCallSiteDescriptor()

Returns the call site descriptor for the call site being linked.

**Returns:**
- the call site descriptor for the call site being linked.

---

#### Object
[] getArguments()

Returns the arguments for the invocation being linked. The returned array
must be a clone; modifications to it must not affect the arguments in
this request.

**Returns:**
- the arguments for the invocation being linked.

---

#### Object
getReceiver()

Returns the first argument for the invocation being linked; this is
typically the receiver object. This is a shorthand for

getArguments()[0]

that also avoids the cloning of the arguments
array.

**Returns:**
- the receiver object.

---

#### boolean isCallSiteUnstable()

Returns true if the call site is considered unstable, that is, it has been relinked more times than was
specified in

DynamicLinkerFactory.setUnstableRelinkThreshold(int)

. Linkers should use this as a
hint to prefer producing linkage that is more stable (its guard fails less frequently), even if that assumption
causes a less effective version of an operation to be linked. This is just a hint, though, and linkers are
allowed to ignore this property.

**Returns:**
- true if the call site is considered unstable.

---

#### LinkRequest
replaceArguments​(
CallSiteDescriptor
callSiteDescriptor,

Object
... arguments)

Returns a request identical to this one with call site descriptor and arguments replaced with the ones specified.

**Parameters:**
- callSiteDescriptor

- the new call site descriptor
- arguments

- the new arguments

**Returns:**
- a new request identical to this one, except with the call site descriptor and arguments replaced with the
specified ones.

---

### Additional Sections

#### Interface LinkRequest

**All Known Implementing Classes:** SimpleLinkRequest

```java
public interface
LinkRequest
```

Represents a request to link a particular invocation at a particular call
site. Instances of these requests will be constructed and passed to all

GuardingDynamicLinker

objects managed by the

DynamicLinker

that is trying to link the call site.

public interface

LinkRequest

Represents a request to link a particular invocation at a particular call
site. Instances of these requests will be constructed and passed to all

GuardingDynamicLinker

objects managed by the

DynamicLinker

that is trying to link the call site.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

[]

getArguments

()

Returns the arguments for the invocation being linked.

CallSiteDescriptor

getCallSiteDescriptor

()

Returns the call site descriptor for the call site being linked.

Object

getReceiver

()

Returns the first argument for the invocation being linked; this is
typically the receiver object.

boolean

isCallSiteUnstable

()

Returns true if the call site is considered unstable, that is, it has been relinked more times than was
specified in

DynamicLinkerFactory.setUnstableRelinkThreshold(int)

.

LinkRequest

replaceArguments

​(

CallSiteDescriptor

callSiteDescriptor,

Object

... arguments)

Returns a request identical to this one with call site descriptor and arguments replaced with the ones specified.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

[]

getArguments

()

Returns the arguments for the invocation being linked.

CallSiteDescriptor

getCallSiteDescriptor

()

Returns the call site descriptor for the call site being linked.

Object

getReceiver

()

Returns the first argument for the invocation being linked; this is
typically the receiver object.

boolean

isCallSiteUnstable

()

Returns true if the call site is considered unstable, that is, it has been relinked more times than was
specified in

DynamicLinkerFactory.setUnstableRelinkThreshold(int)

.

LinkRequest

replaceArguments

​(

CallSiteDescriptor

callSiteDescriptor,

Object

... arguments)

Returns a request identical to this one with call site descriptor and arguments replaced with the ones specified.

---

#### Method Summary

Returns the arguments for the invocation being linked.

Returns the call site descriptor for the call site being linked.

Returns the first argument for the invocation being linked; this is
typically the receiver object.

Returns true if the call site is considered unstable, that is, it has been relinked more times than was
specified in

DynamicLinkerFactory.setUnstableRelinkThreshold(int)

.

Returns a request identical to this one with call site descriptor and arguments replaced with the ones specified.

============ METHOD DETAIL ==========

- Method Detail

- getCallSiteDescriptor

```java
CallSiteDescriptor
getCallSiteDescriptor()
```

Returns the call site descriptor for the call site being linked.

**Returns:** the call site descriptor for the call site being linked.

- getArguments

```java
Object
[] getArguments()
```

Returns the arguments for the invocation being linked. The returned array
must be a clone; modifications to it must not affect the arguments in
this request.

**Returns:** the arguments for the invocation being linked.

- getReceiver

```java
Object
getReceiver()
```

Returns the first argument for the invocation being linked; this is
typically the receiver object. This is a shorthand for

getArguments()[0]

that also avoids the cloning of the arguments
array.

**Returns:** the receiver object.

- isCallSiteUnstable

```java
boolean isCallSiteUnstable()
```

Returns true if the call site is considered unstable, that is, it has been relinked more times than was
specified in

DynamicLinkerFactory.setUnstableRelinkThreshold(int)

. Linkers should use this as a
hint to prefer producing linkage that is more stable (its guard fails less frequently), even if that assumption
causes a less effective version of an operation to be linked. This is just a hint, though, and linkers are
allowed to ignore this property.

**Returns:** true if the call site is considered unstable.

- replaceArguments

```java
LinkRequest
replaceArguments​(
CallSiteDescriptor
callSiteDescriptor,

Object
... arguments)
```

Returns a request identical to this one with call site descriptor and arguments replaced with the ones specified.

**Parameters:** callSiteDescriptor

- the new call site descriptor
**Parameters:** arguments

- the new arguments
**Returns:** a new request identical to this one, except with the call site descriptor and arguments replaced with the
specified ones.

Method Detail

- getCallSiteDescriptor

```java
CallSiteDescriptor
getCallSiteDescriptor()
```

Returns the call site descriptor for the call site being linked.

**Returns:** the call site descriptor for the call site being linked.

- getArguments

```java
Object
[] getArguments()
```

Returns the arguments for the invocation being linked. The returned array
must be a clone; modifications to it must not affect the arguments in
this request.

**Returns:** the arguments for the invocation being linked.

- getReceiver

```java
Object
getReceiver()
```

Returns the first argument for the invocation being linked; this is
typically the receiver object. This is a shorthand for

getArguments()[0]

that also avoids the cloning of the arguments
array.

**Returns:** the receiver object.

- isCallSiteUnstable

```java
boolean isCallSiteUnstable()
```

Returns true if the call site is considered unstable, that is, it has been relinked more times than was
specified in

DynamicLinkerFactory.setUnstableRelinkThreshold(int)

. Linkers should use this as a
hint to prefer producing linkage that is more stable (its guard fails less frequently), even if that assumption
causes a less effective version of an operation to be linked. This is just a hint, though, and linkers are
allowed to ignore this property.

**Returns:** true if the call site is considered unstable.

- replaceArguments

```java
LinkRequest
replaceArguments​(
CallSiteDescriptor
callSiteDescriptor,

Object
... arguments)
```

Returns a request identical to this one with call site descriptor and arguments replaced with the ones specified.

**Parameters:** callSiteDescriptor

- the new call site descriptor
**Parameters:** arguments

- the new arguments
**Returns:** a new request identical to this one, except with the call site descriptor and arguments replaced with the
specified ones.

---

#### Method Detail

getCallSiteDescriptor

```java
CallSiteDescriptor
getCallSiteDescriptor()
```

Returns the call site descriptor for the call site being linked.

**Returns:** the call site descriptor for the call site being linked.

---

#### getCallSiteDescriptor

CallSiteDescriptor

getCallSiteDescriptor()

Returns the call site descriptor for the call site being linked.

getArguments

```java
Object
[] getArguments()
```

Returns the arguments for the invocation being linked. The returned array
must be a clone; modifications to it must not affect the arguments in
this request.

**Returns:** the arguments for the invocation being linked.

---

#### getArguments

Object

[] getArguments()

Returns the arguments for the invocation being linked. The returned array
must be a clone; modifications to it must not affect the arguments in
this request.

getReceiver

```java
Object
getReceiver()
```

Returns the first argument for the invocation being linked; this is
typically the receiver object. This is a shorthand for

getArguments()[0]

that also avoids the cloning of the arguments
array.

**Returns:** the receiver object.

---

#### getReceiver

Object

getReceiver()

Returns the first argument for the invocation being linked; this is
typically the receiver object. This is a shorthand for

getArguments()[0]

that also avoids the cloning of the arguments
array.

isCallSiteUnstable

```java
boolean isCallSiteUnstable()
```

Returns true if the call site is considered unstable, that is, it has been relinked more times than was
specified in

DynamicLinkerFactory.setUnstableRelinkThreshold(int)

. Linkers should use this as a
hint to prefer producing linkage that is more stable (its guard fails less frequently), even if that assumption
causes a less effective version of an operation to be linked. This is just a hint, though, and linkers are
allowed to ignore this property.

**Returns:** true if the call site is considered unstable.

---

#### isCallSiteUnstable

boolean isCallSiteUnstable()

Returns true if the call site is considered unstable, that is, it has been relinked more times than was
specified in

DynamicLinkerFactory.setUnstableRelinkThreshold(int)

. Linkers should use this as a
hint to prefer producing linkage that is more stable (its guard fails less frequently), even if that assumption
causes a less effective version of an operation to be linked. This is just a hint, though, and linkers are
allowed to ignore this property.

replaceArguments

```java
LinkRequest
replaceArguments​(
CallSiteDescriptor
callSiteDescriptor,

Object
... arguments)
```

Returns a request identical to this one with call site descriptor and arguments replaced with the ones specified.

**Parameters:** callSiteDescriptor

- the new call site descriptor
**Parameters:** arguments

- the new arguments
**Returns:** a new request identical to this one, except with the call site descriptor and arguments replaced with the
specified ones.

---

#### replaceArguments

LinkRequest

replaceArguments​(

CallSiteDescriptor

callSiteDescriptor,

Object

... arguments)

Returns a request identical to this one with call site descriptor and arguments replaced with the ones specified.

---

