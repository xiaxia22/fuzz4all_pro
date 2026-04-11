# Class AbstractProcessor

**Source:** `java.compiler\javax\annotation\processing\AbstractProcessor.html`

### Class Description

```java
public abstract class
AbstractProcessor

extends
Object

implements
Processor
```

An abstract annotation processor designed to be a convenient
superclass for most concrete annotation processors. This class
examines annotation values to compute the

options

,

annotation types

, and

source version

supported by its
subtypes.

The getter methods may

issue
warnings

about noteworthy conditions using the facilities available
after the processor has been

initialized

.

Subclasses are free to override the implementation and
specification of any of the methods in this class as long as the
general

Processor

contract for that method is obeyed.

**All Implemented Interfaces:** Processor

---

### Field Details

#### protected
ProcessingEnvironment
processingEnv

Processing environment providing by the tool framework.

---

### Constructor Details

#### protected AbstractProcessor()

Constructor for subclasses to call.

---

### Method Details

#### public
Set
<
String
> getSupportedOptions()

If the processor class is annotated with

SupportedOptions

, return an unmodifiable set with the same set
of strings as the annotation. If the class is not so
annotated, an empty set is returned.

**Specified by:**
- getSupportedOptions

in interface

Processor

**Returns:**
- the options recognized by this processor, or an empty
set if none

**See Also:**
- SupportedOptions

---

#### public
Set
<
String
> getSupportedAnnotationTypes()

If the processor class is annotated with

SupportedAnnotationTypes

, return an unmodifiable set with the
same set of strings as the annotation. If the class is not so
annotated, an empty set is returned.

If the

source
version

does not support modules, in other words if it is less
than or equal to

RELEASE_8

,
then any leading

module prefixes

are stripped from the names.

**Specified by:**
- getSupportedAnnotationTypes

in interface

Processor

**Returns:**
- the names of the annotation types supported by this
processor, or an empty set if none

**See Also:**
- SupportedAnnotationTypes

---

#### public
SourceVersion
getSupportedSourceVersion()

If the processor class is annotated with

SupportedSourceVersion

, return the source version in the
annotation. If the class is not so annotated,

SourceVersion.RELEASE_6

is returned.

**Specified by:**
- getSupportedSourceVersion

in interface

Processor

**Returns:**
- the latest source version supported by this processor

**See Also:**
- SupportedSourceVersion

,

ProcessingEnvironment.getSourceVersion()

---

#### public void init​(
ProcessingEnvironment
processingEnv)

Initializes the processor with the processing environment by
setting the

processingEnv

field to the value of the

processingEnv

argument. An

IllegalStateException

will be thrown if this method is called
more than once on the same object.

**Specified by:**
- init

in interface

Processor

**Parameters:**
- processingEnv

- environment to access facilities the tool framework
provides to the processor

**Throws:**
- IllegalStateException

- if this method is called more than once.

---

#### public
Iterable
<? extends
Completion
> getCompletions​(
Element
element,

AnnotationMirror
annotation,

ExecutableElement
member,

String
userText)

Returns an empty iterable of completions.

**Specified by:**
- getCompletions

in interface

Processor

**Parameters:**
- element

- the element being annotated
- annotation

- the (perhaps partial) annotation being
applied to the element
- member

- the annotation member to return possible completions for
- userText

- source code text to be completed

**Returns:**
- suggested completions to the annotation

---

#### protected boolean isInitialized()

Returns

true

if this object has been

initialized

,

false

otherwise.

**Returns:**
- true

if this object has been initialized,

false

otherwise.

---

### Additional Sections

#### Class AbstractProcessor

java.lang.Object

- javax.annotation.processing.AbstractProcessor

javax.annotation.processing.AbstractProcessor

**All Implemented Interfaces:** Processor

```java
public abstract class
AbstractProcessor

extends
Object

implements
Processor
```

An abstract annotation processor designed to be a convenient
superclass for most concrete annotation processors. This class
examines annotation values to compute the

options

,

annotation types

, and

source version

supported by its
subtypes.

The getter methods may

issue
warnings

about noteworthy conditions using the facilities available
after the processor has been

initialized

.

Subclasses are free to override the implementation and
specification of any of the methods in this class as long as the
general

Processor

contract for that method is obeyed.

**Since:** 1.6

public abstract class

AbstractProcessor

extends

Object

implements

Processor

An abstract annotation processor designed to be a convenient
superclass for most concrete annotation processors. This class
examines annotation values to compute the

options

,

annotation types

, and

source version

supported by its
subtypes.

The getter methods may

issue
warnings

about noteworthy conditions using the facilities available
after the processor has been

initialized

.

Subclasses are free to override the implementation and
specification of any of the methods in this class as long as the
general

Processor

contract for that method is obeyed.

The getter methods may

issue
warnings

about noteworthy conditions using the facilities available
after the processor has been

initialized

.

Subclasses are free to override the implementation and
specification of any of the methods in this class as long as the
general

Processor

contract for that method is obeyed.

Subclasses are free to override the implementation and
specification of any of the methods in this class as long as the
general

Processor

contract for that method is obeyed.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

ProcessingEnvironment

processingEnv

Processing environment providing by the tool framework.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractProcessor

()

Constructor for subclasses to call.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Iterable

<? extends

Completion

>

getCompletions

​(

Element

element,

AnnotationMirror

annotation,

ExecutableElement

member,

String

userText)

Returns an empty iterable of completions.

Set

<

String

>

getSupportedAnnotationTypes

()

If the processor class is annotated with

SupportedAnnotationTypes

, return an unmodifiable set with the
same set of strings as the annotation.

Set

<

String

>

getSupportedOptions

()

If the processor class is annotated with

SupportedOptions

, return an unmodifiable set with the same set
of strings as the annotation.

SourceVersion

getSupportedSourceVersion

()

If the processor class is annotated with

SupportedSourceVersion

, return the source version in the
annotation.

void

init

​(

ProcessingEnvironment

processingEnv)

Initializes the processor with the processing environment by
setting the

processingEnv

field to the value of the

processingEnv

argument.

protected boolean

isInitialized

()

Returns

true

if this object has been

initialized

,

false

otherwise.

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

- Methods declared in interface javax.annotation.processing.

Processor

process

Field Summary

Fields

Modifier and Type

Field

Description

protected

ProcessingEnvironment

processingEnv

Processing environment providing by the tool framework.

---

#### Field Summary

Processing environment providing by the tool framework.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractProcessor

()

Constructor for subclasses to call.

---

#### Constructor Summary

Constructor for subclasses to call.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Iterable

<? extends

Completion

>

getCompletions

​(

Element

element,

AnnotationMirror

annotation,

ExecutableElement

member,

String

userText)

Returns an empty iterable of completions.

Set

<

String

>

getSupportedAnnotationTypes

()

If the processor class is annotated with

SupportedAnnotationTypes

, return an unmodifiable set with the
same set of strings as the annotation.

Set

<

String

>

getSupportedOptions

()

If the processor class is annotated with

SupportedOptions

, return an unmodifiable set with the same set
of strings as the annotation.

SourceVersion

getSupportedSourceVersion

()

If the processor class is annotated with

SupportedSourceVersion

, return the source version in the
annotation.

void

init

​(

ProcessingEnvironment

processingEnv)

Initializes the processor with the processing environment by
setting the

processingEnv

field to the value of the

processingEnv

argument.

protected boolean

isInitialized

()

Returns

true

if this object has been

initialized

,

false

otherwise.

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

- Methods declared in interface javax.annotation.processing.

Processor

process

---

#### Method Summary

Returns an empty iterable of completions.

If the processor class is annotated with

SupportedAnnotationTypes

, return an unmodifiable set with the
same set of strings as the annotation.

If the processor class is annotated with

SupportedOptions

, return an unmodifiable set with the same set
of strings as the annotation.

If the processor class is annotated with

SupportedSourceVersion

, return the source version in the
annotation.

Initializes the processor with the processing environment by
setting the

processingEnv

field to the value of the

processingEnv

argument.

Returns

true

if this object has been

initialized

,

false

otherwise.

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

Methods declared in interface javax.annotation.processing.

Processor

process

---

#### Methods declared in interface javax.annotation.processing. Processor

============ FIELD DETAIL ===========

- Field Detail

- processingEnv

```java
protected
ProcessingEnvironment
processingEnv
```

Processing environment providing by the tool framework.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractProcessor

```java
protected AbstractProcessor()
```

Constructor for subclasses to call.

============ METHOD DETAIL ==========

- Method Detail

- getSupportedOptions

```java
public
Set
<
String
> getSupportedOptions()
```

If the processor class is annotated with

SupportedOptions

, return an unmodifiable set with the same set
of strings as the annotation. If the class is not so
annotated, an empty set is returned.

**Specified by:** getSupportedOptions

in interface

Processor
**Returns:** the options recognized by this processor, or an empty
set if none
**See Also:** SupportedOptions

- getSupportedAnnotationTypes

```java
public
Set
<
String
> getSupportedAnnotationTypes()
```

If the processor class is annotated with

SupportedAnnotationTypes

, return an unmodifiable set with the
same set of strings as the annotation. If the class is not so
annotated, an empty set is returned.

If the

source
version

does not support modules, in other words if it is less
than or equal to

RELEASE_8

,
then any leading

module prefixes

are stripped from the names.

**Specified by:** getSupportedAnnotationTypes

in interface

Processor
**Returns:** the names of the annotation types supported by this
processor, or an empty set if none
**See Also:** SupportedAnnotationTypes

- getSupportedSourceVersion

```java
public
SourceVersion
getSupportedSourceVersion()
```

If the processor class is annotated with

SupportedSourceVersion

, return the source version in the
annotation. If the class is not so annotated,

SourceVersion.RELEASE_6

is returned.

**Specified by:** getSupportedSourceVersion

in interface

Processor
**Returns:** the latest source version supported by this processor
**See Also:** SupportedSourceVersion

,

ProcessingEnvironment.getSourceVersion()

- init

```java
public void init​(
ProcessingEnvironment
processingEnv)
```

Initializes the processor with the processing environment by
setting the

processingEnv

field to the value of the

processingEnv

argument. An

IllegalStateException

will be thrown if this method is called
more than once on the same object.

**Specified by:** init

in interface

Processor
**Parameters:** processingEnv

- environment to access facilities the tool framework
provides to the processor
**Throws:** IllegalStateException

- if this method is called more than once.

- getCompletions

```java
public
Iterable
<? extends
Completion
> getCompletions​(
Element
element,

AnnotationMirror
annotation,

ExecutableElement
member,

String
userText)
```

Returns an empty iterable of completions.

**Specified by:** getCompletions

in interface

Processor
**Parameters:** element

- the element being annotated
**Parameters:** annotation

- the (perhaps partial) annotation being
applied to the element
**Parameters:** member

- the annotation member to return possible completions for
**Parameters:** userText

- source code text to be completed
**Returns:** suggested completions to the annotation

- isInitialized

```java
protected boolean isInitialized()
```

Returns

true

if this object has been

initialized

,

false

otherwise.

**Returns:** true

if this object has been initialized,

false

otherwise.

Field Detail

- processingEnv

```java
protected
ProcessingEnvironment
processingEnv
```

Processing environment providing by the tool framework.

---

#### Field Detail

processingEnv

```java
protected
ProcessingEnvironment
processingEnv
```

Processing environment providing by the tool framework.

---

#### processingEnv

protected

ProcessingEnvironment

processingEnv

Processing environment providing by the tool framework.

Constructor Detail

- AbstractProcessor

```java
protected AbstractProcessor()
```

Constructor for subclasses to call.

---

#### Constructor Detail

AbstractProcessor

```java
protected AbstractProcessor()
```

Constructor for subclasses to call.

---

#### AbstractProcessor

protected AbstractProcessor()

Constructor for subclasses to call.

Method Detail

- getSupportedOptions

```java
public
Set
<
String
> getSupportedOptions()
```

If the processor class is annotated with

SupportedOptions

, return an unmodifiable set with the same set
of strings as the annotation. If the class is not so
annotated, an empty set is returned.

**Specified by:** getSupportedOptions

in interface

Processor
**Returns:** the options recognized by this processor, or an empty
set if none
**See Also:** SupportedOptions

- getSupportedAnnotationTypes

```java
public
Set
<
String
> getSupportedAnnotationTypes()
```

If the processor class is annotated with

SupportedAnnotationTypes

, return an unmodifiable set with the
same set of strings as the annotation. If the class is not so
annotated, an empty set is returned.

If the

source
version

does not support modules, in other words if it is less
than or equal to

RELEASE_8

,
then any leading

module prefixes

are stripped from the names.

**Specified by:** getSupportedAnnotationTypes

in interface

Processor
**Returns:** the names of the annotation types supported by this
processor, or an empty set if none
**See Also:** SupportedAnnotationTypes

- getSupportedSourceVersion

```java
public
SourceVersion
getSupportedSourceVersion()
```

If the processor class is annotated with

SupportedSourceVersion

, return the source version in the
annotation. If the class is not so annotated,

SourceVersion.RELEASE_6

is returned.

**Specified by:** getSupportedSourceVersion

in interface

Processor
**Returns:** the latest source version supported by this processor
**See Also:** SupportedSourceVersion

,

ProcessingEnvironment.getSourceVersion()

- init

```java
public void init​(
ProcessingEnvironment
processingEnv)
```

Initializes the processor with the processing environment by
setting the

processingEnv

field to the value of the

processingEnv

argument. An

IllegalStateException

will be thrown if this method is called
more than once on the same object.

**Specified by:** init

in interface

Processor
**Parameters:** processingEnv

- environment to access facilities the tool framework
provides to the processor
**Throws:** IllegalStateException

- if this method is called more than once.

- getCompletions

```java
public
Iterable
<? extends
Completion
> getCompletions​(
Element
element,

AnnotationMirror
annotation,

ExecutableElement
member,

String
userText)
```

Returns an empty iterable of completions.

**Specified by:** getCompletions

in interface

Processor
**Parameters:** element

- the element being annotated
**Parameters:** annotation

- the (perhaps partial) annotation being
applied to the element
**Parameters:** member

- the annotation member to return possible completions for
**Parameters:** userText

- source code text to be completed
**Returns:** suggested completions to the annotation

- isInitialized

```java
protected boolean isInitialized()
```

Returns

true

if this object has been

initialized

,

false

otherwise.

**Returns:** true

if this object has been initialized,

false

otherwise.

---

#### Method Detail

getSupportedOptions

```java
public
Set
<
String
> getSupportedOptions()
```

If the processor class is annotated with

SupportedOptions

, return an unmodifiable set with the same set
of strings as the annotation. If the class is not so
annotated, an empty set is returned.

**Specified by:** getSupportedOptions

in interface

Processor
**Returns:** the options recognized by this processor, or an empty
set if none
**See Also:** SupportedOptions

---

#### getSupportedOptions

public

Set

<

String

> getSupportedOptions()

If the processor class is annotated with

SupportedOptions

, return an unmodifiable set with the same set
of strings as the annotation. If the class is not so
annotated, an empty set is returned.

getSupportedAnnotationTypes

```java
public
Set
<
String
> getSupportedAnnotationTypes()
```

If the processor class is annotated with

SupportedAnnotationTypes

, return an unmodifiable set with the
same set of strings as the annotation. If the class is not so
annotated, an empty set is returned.

If the

source
version

does not support modules, in other words if it is less
than or equal to

RELEASE_8

,
then any leading

module prefixes

are stripped from the names.

**Specified by:** getSupportedAnnotationTypes

in interface

Processor
**Returns:** the names of the annotation types supported by this
processor, or an empty set if none
**See Also:** SupportedAnnotationTypes

---

#### getSupportedAnnotationTypes

public

Set

<

String

> getSupportedAnnotationTypes()

If the processor class is annotated with

SupportedAnnotationTypes

, return an unmodifiable set with the
same set of strings as the annotation. If the class is not so
annotated, an empty set is returned.

If the

source
version

does not support modules, in other words if it is less
than or equal to

RELEASE_8

,
then any leading

module prefixes

are stripped from the names.

getSupportedSourceVersion

```java
public
SourceVersion
getSupportedSourceVersion()
```

If the processor class is annotated with

SupportedSourceVersion

, return the source version in the
annotation. If the class is not so annotated,

SourceVersion.RELEASE_6

is returned.

**Specified by:** getSupportedSourceVersion

in interface

Processor
**Returns:** the latest source version supported by this processor
**See Also:** SupportedSourceVersion

,

ProcessingEnvironment.getSourceVersion()

---

#### getSupportedSourceVersion

public

SourceVersion

getSupportedSourceVersion()

If the processor class is annotated with

SupportedSourceVersion

, return the source version in the
annotation. If the class is not so annotated,

SourceVersion.RELEASE_6

is returned.

init

```java
public void init​(
ProcessingEnvironment
processingEnv)
```

Initializes the processor with the processing environment by
setting the

processingEnv

field to the value of the

processingEnv

argument. An

IllegalStateException

will be thrown if this method is called
more than once on the same object.

**Specified by:** init

in interface

Processor
**Parameters:** processingEnv

- environment to access facilities the tool framework
provides to the processor
**Throws:** IllegalStateException

- if this method is called more than once.

---

#### init

public void init​(

ProcessingEnvironment

processingEnv)

Initializes the processor with the processing environment by
setting the

processingEnv

field to the value of the

processingEnv

argument. An

IllegalStateException

will be thrown if this method is called
more than once on the same object.

getCompletions

```java
public
Iterable
<? extends
Completion
> getCompletions​(
Element
element,

AnnotationMirror
annotation,

ExecutableElement
member,

String
userText)
```

Returns an empty iterable of completions.

**Specified by:** getCompletions

in interface

Processor
**Parameters:** element

- the element being annotated
**Parameters:** annotation

- the (perhaps partial) annotation being
applied to the element
**Parameters:** member

- the annotation member to return possible completions for
**Parameters:** userText

- source code text to be completed
**Returns:** suggested completions to the annotation

---

#### getCompletions

public

Iterable

<? extends

Completion

> getCompletions​(

Element

element,

AnnotationMirror

annotation,

ExecutableElement

member,

String

userText)

Returns an empty iterable of completions.

isInitialized

```java
protected boolean isInitialized()
```

Returns

true

if this object has been

initialized

,

false

otherwise.

**Returns:** true

if this object has been initialized,

false

otherwise.

---

#### isInitialized

protected boolean isInitialized()

Returns

true

if this object has been

initialized

,

false

otherwise.

---

