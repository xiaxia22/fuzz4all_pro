# Interface Messager

**Source:** `java.compiler\javax\annotation\processing\Messager.html`

### Class Description

```java
public interface
Messager
```

A

Messager

provides the way for an annotation processor to
report error messages, warnings, and other notices. Elements,
annotations, and annotation values can be passed to provide a
location hint for the message. However, such location hints may be
unavailable or only approximate.

Printing a message with an

error kind

will

raise an error

.

Note that the messages "printed" by methods in this
interface may or may not appear as textual output to a location
like

System.out

or

System.err

. Implementations may
choose to present this information in a different fashion, such as
messages in a window.

**Since:** 1.6
**See Also:** ProcessingEnvironment.getLocale()

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg)

Prints a message of the specified kind.

**Parameters:**
- kind

- the kind of message
- msg

- the message, or an empty string if none

---

#### void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

Element
e)

Prints a message of the specified kind at the location of the
element.

**Parameters:**
- kind

- the kind of message
- msg

- the message, or an empty string if none
- e

- the element to use as a position hint

---

#### void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

Element
e,

AnnotationMirror
a)

Prints a message of the specified kind at the location of the
annotation mirror of the annotated element.

**Parameters:**
- kind

- the kind of message
- msg

- the message, or an empty string if none
- e

- the annotated element
- a

- the annotation to use as a position hint

---

#### void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

Element
e,

AnnotationMirror
a,

AnnotationValue
v)

Prints a message of the specified kind at the location of the
annotation value inside the annotation mirror of the annotated
element.

**Parameters:**
- kind

- the kind of message
- msg

- the message, or an empty string if none
- e

- the annotated element
- a

- the annotation containing the annotation value
- v

- the annotation value to use as a position hint

---

### Additional Sections

#### Interface Messager

```java
public interface
Messager
```

A

Messager

provides the way for an annotation processor to
report error messages, warnings, and other notices. Elements,
annotations, and annotation values can be passed to provide a
location hint for the message. However, such location hints may be
unavailable or only approximate.

Printing a message with an

error kind

will

raise an error

.

Note that the messages "printed" by methods in this
interface may or may not appear as textual output to a location
like

System.out

or

System.err

. Implementations may
choose to present this information in a different fashion, such as
messages in a window.

**Since:** 1.6
**See Also:** ProcessingEnvironment.getLocale()

public interface

Messager

A

Messager

provides the way for an annotation processor to
report error messages, warnings, and other notices. Elements,
annotations, and annotation values can be passed to provide a
location hint for the message. However, such location hints may be
unavailable or only approximate.

Printing a message with an

error kind

will

raise an error

.

Note that the messages "printed" by methods in this
interface may or may not appear as textual output to a location
like

System.out

or

System.err

. Implementations may
choose to present this information in a different fashion, such as
messages in a window.

Printing a message with an

error kind

will

raise an error

.

Note that the messages "printed" by methods in this
interface may or may not appear as textual output to a location
like

System.out

or

System.err

. Implementations may
choose to present this information in a different fashion, such as
messages in a window.

Note that the messages "printed" by methods in this
interface may or may not appear as textual output to a location
like

System.out

or

System.err

. Implementations may
choose to present this information in a different fashion, such as
messages in a window.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

printMessage

​(

Diagnostic.Kind

kind,

CharSequence

msg)

Prints a message of the specified kind.

void

printMessage

​(

Diagnostic.Kind

kind,

CharSequence

msg,

Element

e)

Prints a message of the specified kind at the location of the
element.

void

printMessage

​(

Diagnostic.Kind

kind,

CharSequence

msg,

Element

e,

AnnotationMirror

a)

Prints a message of the specified kind at the location of the
annotation mirror of the annotated element.

void

printMessage

​(

Diagnostic.Kind

kind,

CharSequence

msg,

Element

e,

AnnotationMirror

a,

AnnotationValue

v)

Prints a message of the specified kind at the location of the
annotation value inside the annotation mirror of the annotated
element.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

printMessage

​(

Diagnostic.Kind

kind,

CharSequence

msg)

Prints a message of the specified kind.

void

printMessage

​(

Diagnostic.Kind

kind,

CharSequence

msg,

Element

e)

Prints a message of the specified kind at the location of the
element.

void

printMessage

​(

Diagnostic.Kind

kind,

CharSequence

msg,

Element

e,

AnnotationMirror

a)

Prints a message of the specified kind at the location of the
annotation mirror of the annotated element.

void

printMessage

​(

Diagnostic.Kind

kind,

CharSequence

msg,

Element

e,

AnnotationMirror

a,

AnnotationValue

v)

Prints a message of the specified kind at the location of the
annotation value inside the annotation mirror of the annotated
element.

---

#### Method Summary

Prints a message of the specified kind.

Prints a message of the specified kind at the location of the
element.

Prints a message of the specified kind at the location of the
annotation mirror of the annotated element.

Prints a message of the specified kind at the location of the
annotation value inside the annotation mirror of the annotated
element.

============ METHOD DETAIL ==========

- Method Detail

- printMessage

```java
void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg)
```

Prints a message of the specified kind.

**Parameters:** kind

- the kind of message
**Parameters:** msg

- the message, or an empty string if none

- printMessage

```java
void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

Element
e)
```

Prints a message of the specified kind at the location of the
element.

**Parameters:** kind

- the kind of message
**Parameters:** msg

- the message, or an empty string if none
**Parameters:** e

- the element to use as a position hint

- printMessage

```java
void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

Element
e,

AnnotationMirror
a)
```

Prints a message of the specified kind at the location of the
annotation mirror of the annotated element.

**Parameters:** kind

- the kind of message
**Parameters:** msg

- the message, or an empty string if none
**Parameters:** e

- the annotated element
**Parameters:** a

- the annotation to use as a position hint

- printMessage

```java
void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

Element
e,

AnnotationMirror
a,

AnnotationValue
v)
```

Prints a message of the specified kind at the location of the
annotation value inside the annotation mirror of the annotated
element.

**Parameters:** kind

- the kind of message
**Parameters:** msg

- the message, or an empty string if none
**Parameters:** e

- the annotated element
**Parameters:** a

- the annotation containing the annotation value
**Parameters:** v

- the annotation value to use as a position hint

Method Detail

- printMessage

```java
void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg)
```

Prints a message of the specified kind.

**Parameters:** kind

- the kind of message
**Parameters:** msg

- the message, or an empty string if none

- printMessage

```java
void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

Element
e)
```

Prints a message of the specified kind at the location of the
element.

**Parameters:** kind

- the kind of message
**Parameters:** msg

- the message, or an empty string if none
**Parameters:** e

- the element to use as a position hint

- printMessage

```java
void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

Element
e,

AnnotationMirror
a)
```

Prints a message of the specified kind at the location of the
annotation mirror of the annotated element.

**Parameters:** kind

- the kind of message
**Parameters:** msg

- the message, or an empty string if none
**Parameters:** e

- the annotated element
**Parameters:** a

- the annotation to use as a position hint

- printMessage

```java
void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

Element
e,

AnnotationMirror
a,

AnnotationValue
v)
```

Prints a message of the specified kind at the location of the
annotation value inside the annotation mirror of the annotated
element.

**Parameters:** kind

- the kind of message
**Parameters:** msg

- the message, or an empty string if none
**Parameters:** e

- the annotated element
**Parameters:** a

- the annotation containing the annotation value
**Parameters:** v

- the annotation value to use as a position hint

---

#### Method Detail

printMessage

```java
void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg)
```

Prints a message of the specified kind.

**Parameters:** kind

- the kind of message
**Parameters:** msg

- the message, or an empty string if none

---

#### printMessage

void printMessage​(

Diagnostic.Kind

kind,

CharSequence

msg)

Prints a message of the specified kind.

printMessage

```java
void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

Element
e)
```

Prints a message of the specified kind at the location of the
element.

**Parameters:** kind

- the kind of message
**Parameters:** msg

- the message, or an empty string if none
**Parameters:** e

- the element to use as a position hint

---

#### printMessage

void printMessage​(

Diagnostic.Kind

kind,

CharSequence

msg,

Element

e)

Prints a message of the specified kind at the location of the
element.

printMessage

```java
void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

Element
e,

AnnotationMirror
a)
```

Prints a message of the specified kind at the location of the
annotation mirror of the annotated element.

**Parameters:** kind

- the kind of message
**Parameters:** msg

- the message, or an empty string if none
**Parameters:** e

- the annotated element
**Parameters:** a

- the annotation to use as a position hint

---

#### printMessage

void printMessage​(

Diagnostic.Kind

kind,

CharSequence

msg,

Element

e,

AnnotationMirror

a)

Prints a message of the specified kind at the location of the
annotation mirror of the annotated element.

printMessage

```java
void printMessage​(
Diagnostic.Kind
kind,

CharSequence
msg,

Element
e,

AnnotationMirror
a,

AnnotationValue
v)
```

Prints a message of the specified kind at the location of the
annotation value inside the annotation mirror of the annotated
element.

**Parameters:** kind

- the kind of message
**Parameters:** msg

- the message, or an empty string if none
**Parameters:** e

- the annotated element
**Parameters:** a

- the annotation containing the annotation value
**Parameters:** v

- the annotation value to use as a position hint

---

#### printMessage

void printMessage​(

Diagnostic.Kind

kind,

CharSequence

msg,

Element

e,

AnnotationMirror

a,

AnnotationValue

v)

Prints a message of the specified kind at the location of the
annotation value inside the annotation mirror of the annotated
element.

---

