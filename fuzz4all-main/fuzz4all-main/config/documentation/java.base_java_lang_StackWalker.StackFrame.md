# Interface StackWalker.StackFrame

**Source:** `java.base\java\lang\StackWalker.StackFrame.html`

### Class Description

```java
public static interface
StackWalker.StackFrame
```

A

StackFrame

object represents a method invocation returned by

StackWalker

.

The

getDeclaringClass()

method may be unsupported as determined
by the

stack walking options

of a

stack walker

.

**Enclosing class:** StackWalker

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getClassName()

Gets the

binary name

of the declaring class of the method represented by this stack frame.

**Returns:**
- the binary name of the declaring class of the method
represented by this stack frame

**See The Java™ Language Specification :**
- 13.1 The Form of a Binary

---

#### String
getMethodName()

Gets the name of the method represented by this stack frame.

**Returns:**
- the name of the method represented by this stack frame

---

#### Class
<?> getDeclaringClass()

Gets the declaring

Class

for the method represented by
this stack frame.

**Returns:**
- the declaring

Class

of the method represented by
this stack frame

**Throws:**
- UnsupportedOperationException

- if this

StackWalker

is not configured with

Option.RETAIN_CLASS_REFERENCE

.

---

#### default
MethodType
getMethodType()

Returns the

MethodType

representing the parameter types and
the return type for the method represented by this stack frame.

**Returns:**
- the

MethodType

for this stack frame

**Throws:**
- UnsupportedOperationException

- if this

StackWalker

is not configured with

Option.RETAIN_CLASS_REFERENCE

.

**Since:**
- 10

**Implementation Requirements:**
- The default implementation throws

UnsupportedOperationException

.

---

#### default
String
getDescriptor()

Returns the

descriptor

of the method represented by
this stack frame as defined by

The Java Virtual Machine Specification

.

**Returns:**
- the descriptor of the method represented by
this stack frame

**See Also:**
- MethodType.fromMethodDescriptorString(String, ClassLoader)

,

MethodType.toMethodDescriptorString()

**Since:**
- 10

**Implementation Requirements:**
- The default implementation throws

UnsupportedOperationException

.

**See The Java™ Virtual Machine Specification :**
- 4.3.3 Method Descriptor

---

#### int getByteCodeIndex()

Returns the index to the code array of the

Code

attribute
containing the execution point represented by this stack frame.
The code array gives the actual bytes of Java Virtual Machine code
that implement the method.

**Returns:**
- the index to the code array of the

Code

attribute
containing the execution point represented by this stack frame,
or a negative number if the method is native.

**See The Java™ Virtual Machine Specification :**
- 4.7.3 The

Code

Attribute

---

#### String
getFileName()

Returns the name of the source file containing the execution point
represented by this stack frame. Generally, this corresponds
to the

SourceFile

attribute of the relevant

class

file as defined by

The Java Virtual Machine Specification

.
In some systems, the name may refer to some source code unit
other than a file, such as an entry in a source repository.

**Returns:**
- the name of the file containing the execution point
represented by this stack frame, or

null

if
this information is unavailable.

**See The Java™ Virtual Machine Specification :**
- 4.7.10 The

SourceFile

Attribute

---

#### int getLineNumber()

Returns the line number of the source line containing the execution
point represented by this stack frame. Generally, this is
derived from the

LineNumberTable

attribute of the relevant

class

file as defined by

The Java Virtual Machine
Specification

.

**Returns:**
- the line number of the source line containing the execution
point represented by this stack frame, or a negative number if
this information is unavailable.

**See The Java™ Virtual Machine Specification :**
- 4.7.12 The

LineNumberTable

Attribute

---

#### boolean isNativeMethod()

Returns

true

if the method containing the execution point
represented by this stack frame is a native method.

**Returns:**
- true

if the method containing the execution point
represented by this stack frame is a native method.

---

#### StackTraceElement
toStackTraceElement()

Gets a

StackTraceElement

for this stack frame.

**Returns:**
- StackTraceElement

for this stack frame.

---

### Additional Sections

#### Interface StackWalker.StackFrame

**Enclosing class:** StackWalker

```java
public static interface
StackWalker.StackFrame
```

A

StackFrame

object represents a method invocation returned by

StackWalker

.

The

getDeclaringClass()

method may be unsupported as determined
by the

stack walking options

of a

stack walker

.

**Since:** 9
**See The Java™ Virtual Machine Specification :** 2.6

public static interface

StackWalker.StackFrame

A

StackFrame

object represents a method invocation returned by

StackWalker

.

The

getDeclaringClass()

method may be unsupported as determined
by the

stack walking options

of a

stack walker

.

The

getDeclaringClass()

method may be unsupported as determined
by the

stack walking options

of a

stack walker

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

int

getByteCodeIndex

()

Returns the index to the code array of the

Code

attribute
containing the execution point represented by this stack frame.

String

getClassName

()

Gets the

binary name

of the declaring class of the method represented by this stack frame.

Class

<?>

getDeclaringClass

()

Gets the declaring

Class

for the method represented by
this stack frame.

default

String

getDescriptor

()

Returns the

descriptor

of the method represented by
this stack frame as defined by

The Java Virtual Machine Specification

.

String

getFileName

()

Returns the name of the source file containing the execution point
represented by this stack frame.

int

getLineNumber

()

Returns the line number of the source line containing the execution
point represented by this stack frame.

String

getMethodName

()

Gets the name of the method represented by this stack frame.

default

MethodType

getMethodType

()

Returns the

MethodType

representing the parameter types and
the return type for the method represented by this stack frame.

boolean

isNativeMethod

()

Returns

true

if the method containing the execution point
represented by this stack frame is a native method.

StackTraceElement

toStackTraceElement

()

Gets a

StackTraceElement

for this stack frame.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

int

getByteCodeIndex

()

Returns the index to the code array of the

Code

attribute
containing the execution point represented by this stack frame.

String

getClassName

()

Gets the

binary name

of the declaring class of the method represented by this stack frame.

Class

<?>

getDeclaringClass

()

Gets the declaring

Class

for the method represented by
this stack frame.

default

String

getDescriptor

()

Returns the

descriptor

of the method represented by
this stack frame as defined by

The Java Virtual Machine Specification

.

String

getFileName

()

Returns the name of the source file containing the execution point
represented by this stack frame.

int

getLineNumber

()

Returns the line number of the source line containing the execution
point represented by this stack frame.

String

getMethodName

()

Gets the name of the method represented by this stack frame.

default

MethodType

getMethodType

()

Returns the

MethodType

representing the parameter types and
the return type for the method represented by this stack frame.

boolean

isNativeMethod

()

Returns

true

if the method containing the execution point
represented by this stack frame is a native method.

StackTraceElement

toStackTraceElement

()

Gets a

StackTraceElement

for this stack frame.

---

#### Method Summary

Returns the index to the code array of the

Code

attribute
containing the execution point represented by this stack frame.

Gets the

binary name

of the declaring class of the method represented by this stack frame.

Gets the declaring

Class

for the method represented by
this stack frame.

Returns the

descriptor

of the method represented by
this stack frame as defined by

The Java Virtual Machine Specification

.

Returns the name of the source file containing the execution point
represented by this stack frame.

Returns the line number of the source line containing the execution
point represented by this stack frame.

Gets the name of the method represented by this stack frame.

Returns the

MethodType

representing the parameter types and
the return type for the method represented by this stack frame.

Returns

true

if the method containing the execution point
represented by this stack frame is a native method.

Gets a

StackTraceElement

for this stack frame.

============ METHOD DETAIL ==========

- Method Detail

- getClassName

```java
String
getClassName()
```

Gets the

binary name

of the declaring class of the method represented by this stack frame.

**Returns:** the binary name of the declaring class of the method
represented by this stack frame
**See The Java™ Language Specification :** 13.1 The Form of a Binary

- getMethodName

```java
String
getMethodName()
```

Gets the name of the method represented by this stack frame.

**Returns:** the name of the method represented by this stack frame

- getDeclaringClass

```java
Class
<?> getDeclaringClass()
```

Gets the declaring

Class

for the method represented by
this stack frame.

**Returns:** the declaring

Class

of the method represented by
this stack frame
**Throws:** UnsupportedOperationException

- if this

StackWalker

is not configured with

Option.RETAIN_CLASS_REFERENCE

.

- getMethodType

```java
default
MethodType
getMethodType()
```

Returns the

MethodType

representing the parameter types and
the return type for the method represented by this stack frame.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
**Returns:** the

MethodType

for this stack frame
**Throws:** UnsupportedOperationException

- if this

StackWalker

is not configured with

Option.RETAIN_CLASS_REFERENCE

.
**Since:** 10

- getDescriptor

```java
default
String
getDescriptor()
```

Returns the

descriptor

of the method represented by
this stack frame as defined by

The Java Virtual Machine Specification

.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
**Returns:** the descriptor of the method represented by
this stack frame
**Since:** 10
**See Also:** MethodType.fromMethodDescriptorString(String, ClassLoader)

,

MethodType.toMethodDescriptorString()
**See The Java™ Virtual Machine Specification :** 4.3.3 Method Descriptor

- getByteCodeIndex

```java
int getByteCodeIndex()
```

Returns the index to the code array of the

Code

attribute
containing the execution point represented by this stack frame.
The code array gives the actual bytes of Java Virtual Machine code
that implement the method.

**Returns:** the index to the code array of the

Code

attribute
containing the execution point represented by this stack frame,
or a negative number if the method is native.
**See The Java™ Virtual Machine Specification :** 4.7.3 The

Code

Attribute

- getFileName

```java
String
getFileName()
```

Returns the name of the source file containing the execution point
represented by this stack frame. Generally, this corresponds
to the

SourceFile

attribute of the relevant

class

file as defined by

The Java Virtual Machine Specification

.
In some systems, the name may refer to some source code unit
other than a file, such as an entry in a source repository.

**Returns:** the name of the file containing the execution point
represented by this stack frame, or

null

if
this information is unavailable.
**See The Java™ Virtual Machine Specification :** 4.7.10 The

SourceFile

Attribute

- getLineNumber

```java
int getLineNumber()
```

Returns the line number of the source line containing the execution
point represented by this stack frame. Generally, this is
derived from the

LineNumberTable

attribute of the relevant

class

file as defined by

The Java Virtual Machine
Specification

.

**Returns:** the line number of the source line containing the execution
point represented by this stack frame, or a negative number if
this information is unavailable.
**See The Java™ Virtual Machine Specification :** 4.7.12 The

LineNumberTable

Attribute

- isNativeMethod

```java
boolean isNativeMethod()
```

Returns

true

if the method containing the execution point
represented by this stack frame is a native method.

**Returns:** true

if the method containing the execution point
represented by this stack frame is a native method.

- toStackTraceElement

```java
StackTraceElement
toStackTraceElement()
```

Gets a

StackTraceElement

for this stack frame.

**Returns:** StackTraceElement

for this stack frame.

Method Detail

- getClassName

```java
String
getClassName()
```

Gets the

binary name

of the declaring class of the method represented by this stack frame.

**Returns:** the binary name of the declaring class of the method
represented by this stack frame
**See The Java™ Language Specification :** 13.1 The Form of a Binary

- getMethodName

```java
String
getMethodName()
```

Gets the name of the method represented by this stack frame.

**Returns:** the name of the method represented by this stack frame

- getDeclaringClass

```java
Class
<?> getDeclaringClass()
```

Gets the declaring

Class

for the method represented by
this stack frame.

**Returns:** the declaring

Class

of the method represented by
this stack frame
**Throws:** UnsupportedOperationException

- if this

StackWalker

is not configured with

Option.RETAIN_CLASS_REFERENCE

.

- getMethodType

```java
default
MethodType
getMethodType()
```

Returns the

MethodType

representing the parameter types and
the return type for the method represented by this stack frame.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
**Returns:** the

MethodType

for this stack frame
**Throws:** UnsupportedOperationException

- if this

StackWalker

is not configured with

Option.RETAIN_CLASS_REFERENCE

.
**Since:** 10

- getDescriptor

```java
default
String
getDescriptor()
```

Returns the

descriptor

of the method represented by
this stack frame as defined by

The Java Virtual Machine Specification

.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
**Returns:** the descriptor of the method represented by
this stack frame
**Since:** 10
**See Also:** MethodType.fromMethodDescriptorString(String, ClassLoader)

,

MethodType.toMethodDescriptorString()
**See The Java™ Virtual Machine Specification :** 4.3.3 Method Descriptor

- getByteCodeIndex

```java
int getByteCodeIndex()
```

Returns the index to the code array of the

Code

attribute
containing the execution point represented by this stack frame.
The code array gives the actual bytes of Java Virtual Machine code
that implement the method.

**Returns:** the index to the code array of the

Code

attribute
containing the execution point represented by this stack frame,
or a negative number if the method is native.
**See The Java™ Virtual Machine Specification :** 4.7.3 The

Code

Attribute

- getFileName

```java
String
getFileName()
```

Returns the name of the source file containing the execution point
represented by this stack frame. Generally, this corresponds
to the

SourceFile

attribute of the relevant

class

file as defined by

The Java Virtual Machine Specification

.
In some systems, the name may refer to some source code unit
other than a file, such as an entry in a source repository.

**Returns:** the name of the file containing the execution point
represented by this stack frame, or

null

if
this information is unavailable.
**See The Java™ Virtual Machine Specification :** 4.7.10 The

SourceFile

Attribute

- getLineNumber

```java
int getLineNumber()
```

Returns the line number of the source line containing the execution
point represented by this stack frame. Generally, this is
derived from the

LineNumberTable

attribute of the relevant

class

file as defined by

The Java Virtual Machine
Specification

.

**Returns:** the line number of the source line containing the execution
point represented by this stack frame, or a negative number if
this information is unavailable.
**See The Java™ Virtual Machine Specification :** 4.7.12 The

LineNumberTable

Attribute

- isNativeMethod

```java
boolean isNativeMethod()
```

Returns

true

if the method containing the execution point
represented by this stack frame is a native method.

**Returns:** true

if the method containing the execution point
represented by this stack frame is a native method.

- toStackTraceElement

```java
StackTraceElement
toStackTraceElement()
```

Gets a

StackTraceElement

for this stack frame.

**Returns:** StackTraceElement

for this stack frame.

---

#### Method Detail

getClassName

```java
String
getClassName()
```

Gets the

binary name

of the declaring class of the method represented by this stack frame.

**Returns:** the binary name of the declaring class of the method
represented by this stack frame
**See The Java™ Language Specification :** 13.1 The Form of a Binary

---

#### getClassName

String

getClassName()

Gets the

binary name

of the declaring class of the method represented by this stack frame.

getMethodName

```java
String
getMethodName()
```

Gets the name of the method represented by this stack frame.

**Returns:** the name of the method represented by this stack frame

---

#### getMethodName

String

getMethodName()

Gets the name of the method represented by this stack frame.

getDeclaringClass

```java
Class
<?> getDeclaringClass()
```

Gets the declaring

Class

for the method represented by
this stack frame.

**Returns:** the declaring

Class

of the method represented by
this stack frame
**Throws:** UnsupportedOperationException

- if this

StackWalker

is not configured with

Option.RETAIN_CLASS_REFERENCE

.

---

#### getDeclaringClass

Class

<?> getDeclaringClass()

Gets the declaring

Class

for the method represented by
this stack frame.

getMethodType

```java
default
MethodType
getMethodType()
```

Returns the

MethodType

representing the parameter types and
the return type for the method represented by this stack frame.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
**Returns:** the

MethodType

for this stack frame
**Throws:** UnsupportedOperationException

- if this

StackWalker

is not configured with

Option.RETAIN_CLASS_REFERENCE

.
**Since:** 10

---

#### getMethodType

default

MethodType

getMethodType()

Returns the

MethodType

representing the parameter types and
the return type for the method represented by this stack frame.

getDescriptor

```java
default
String
getDescriptor()
```

Returns the

descriptor

of the method represented by
this stack frame as defined by

The Java Virtual Machine Specification

.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
**Returns:** the descriptor of the method represented by
this stack frame
**Since:** 10
**See Also:** MethodType.fromMethodDescriptorString(String, ClassLoader)

,

MethodType.toMethodDescriptorString()
**See The Java™ Virtual Machine Specification :** 4.3.3 Method Descriptor

---

#### getDescriptor

default

String

getDescriptor()

Returns the

descriptor

of the method represented by
this stack frame as defined by

The Java Virtual Machine Specification

.

getByteCodeIndex

```java
int getByteCodeIndex()
```

Returns the index to the code array of the

Code

attribute
containing the execution point represented by this stack frame.
The code array gives the actual bytes of Java Virtual Machine code
that implement the method.

**Returns:** the index to the code array of the

Code

attribute
containing the execution point represented by this stack frame,
or a negative number if the method is native.
**See The Java™ Virtual Machine Specification :** 4.7.3 The

Code

Attribute

---

#### getByteCodeIndex

int getByteCodeIndex()

Returns the index to the code array of the

Code

attribute
containing the execution point represented by this stack frame.
The code array gives the actual bytes of Java Virtual Machine code
that implement the method.

getFileName

```java
String
getFileName()
```

Returns the name of the source file containing the execution point
represented by this stack frame. Generally, this corresponds
to the

SourceFile

attribute of the relevant

class

file as defined by

The Java Virtual Machine Specification

.
In some systems, the name may refer to some source code unit
other than a file, such as an entry in a source repository.

**Returns:** the name of the file containing the execution point
represented by this stack frame, or

null

if
this information is unavailable.
**See The Java™ Virtual Machine Specification :** 4.7.10 The

SourceFile

Attribute

---

#### getFileName

String

getFileName()

Returns the name of the source file containing the execution point
represented by this stack frame. Generally, this corresponds
to the

SourceFile

attribute of the relevant

class

file as defined by

The Java Virtual Machine Specification

.
In some systems, the name may refer to some source code unit
other than a file, such as an entry in a source repository.

getLineNumber

```java
int getLineNumber()
```

Returns the line number of the source line containing the execution
point represented by this stack frame. Generally, this is
derived from the

LineNumberTable

attribute of the relevant

class

file as defined by

The Java Virtual Machine
Specification

.

**Returns:** the line number of the source line containing the execution
point represented by this stack frame, or a negative number if
this information is unavailable.
**See The Java™ Virtual Machine Specification :** 4.7.12 The

LineNumberTable

Attribute

---

#### getLineNumber

int getLineNumber()

Returns the line number of the source line containing the execution
point represented by this stack frame. Generally, this is
derived from the

LineNumberTable

attribute of the relevant

class

file as defined by

The Java Virtual Machine
Specification

.

isNativeMethod

```java
boolean isNativeMethod()
```

Returns

true

if the method containing the execution point
represented by this stack frame is a native method.

**Returns:** true

if the method containing the execution point
represented by this stack frame is a native method.

---

#### isNativeMethod

boolean isNativeMethod()

Returns

true

if the method containing the execution point
represented by this stack frame is a native method.

toStackTraceElement

```java
StackTraceElement
toStackTraceElement()
```

Gets a

StackTraceElement

for this stack frame.

**Returns:** StackTraceElement

for this stack frame.

---

#### toStackTraceElement

StackTraceElement

toStackTraceElement()

Gets a

StackTraceElement

for this stack frame.

---

