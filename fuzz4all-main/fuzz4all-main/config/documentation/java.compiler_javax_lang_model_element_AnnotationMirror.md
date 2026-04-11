# Interface AnnotationMirror

**Source:** `java.compiler\javax\lang\model\element\AnnotationMirror.html`

### Class Description

```java
public interface
AnnotationMirror
```

Represents an annotation. An annotation associates a value with
each element of an annotation type.

Annotations should be compared using the

equals

method. There is no guarantee that any particular annotation will
always be represented by the same object.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### DeclaredType
getAnnotationType()

Returns the type of this annotation.

**Returns:**
- the type of this annotation

---

#### Map
<? extends
ExecutableElement
,​? extends
AnnotationValue
> getElementValues()

Returns the values of this annotation's elements.
This is returned in the form of a map that associates elements
with their corresponding values.
Only those elements with values explicitly present in the
annotation are included, not those that are implicitly assuming
their default values.
The order of the map matches the order in which the
values appear in the annotation's source.

Note that an annotation mirror of a marker annotation type
will by definition have an empty map.

To fill in default values, use

getElementValuesWithDefaults

.

**Returns:**
- the values of this annotation's elements,
or an empty map if there are none

---

### Additional Sections

#### Interface AnnotationMirror

```java
public interface
AnnotationMirror
```

Represents an annotation. An annotation associates a value with
each element of an annotation type.

Annotations should be compared using the

equals

method. There is no guarantee that any particular annotation will
always be represented by the same object.

**Since:** 1.6

public interface

AnnotationMirror

Represents an annotation. An annotation associates a value with
each element of an annotation type.

Annotations should be compared using the

equals

method. There is no guarantee that any particular annotation will
always be represented by the same object.

Annotations should be compared using the

equals

method. There is no guarantee that any particular annotation will
always be represented by the same object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

DeclaredType

getAnnotationType

()

Returns the type of this annotation.

Map

<? extends

ExecutableElement

,​? extends

AnnotationValue

>

getElementValues

()

Returns the values of this annotation's elements.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

DeclaredType

getAnnotationType

()

Returns the type of this annotation.

Map

<? extends

ExecutableElement

,​? extends

AnnotationValue

>

getElementValues

()

Returns the values of this annotation's elements.

---

#### Method Summary

Returns the type of this annotation.

Returns the values of this annotation's elements.

============ METHOD DETAIL ==========

- Method Detail

- getAnnotationType

```java
DeclaredType
getAnnotationType()
```

Returns the type of this annotation.

**Returns:** the type of this annotation

- getElementValues

```java
Map
<? extends
ExecutableElement
,​? extends
AnnotationValue
> getElementValues()
```

Returns the values of this annotation's elements.
This is returned in the form of a map that associates elements
with their corresponding values.
Only those elements with values explicitly present in the
annotation are included, not those that are implicitly assuming
their default values.
The order of the map matches the order in which the
values appear in the annotation's source.

Note that an annotation mirror of a marker annotation type
will by definition have an empty map.

To fill in default values, use

getElementValuesWithDefaults

.

**Returns:** the values of this annotation's elements,
or an empty map if there are none

Method Detail

- getAnnotationType

```java
DeclaredType
getAnnotationType()
```

Returns the type of this annotation.

**Returns:** the type of this annotation

- getElementValues

```java
Map
<? extends
ExecutableElement
,​? extends
AnnotationValue
> getElementValues()
```

Returns the values of this annotation's elements.
This is returned in the form of a map that associates elements
with their corresponding values.
Only those elements with values explicitly present in the
annotation are included, not those that are implicitly assuming
their default values.
The order of the map matches the order in which the
values appear in the annotation's source.

Note that an annotation mirror of a marker annotation type
will by definition have an empty map.

To fill in default values, use

getElementValuesWithDefaults

.

**Returns:** the values of this annotation's elements,
or an empty map if there are none

---

#### Method Detail

getAnnotationType

```java
DeclaredType
getAnnotationType()
```

Returns the type of this annotation.

**Returns:** the type of this annotation

---

#### getAnnotationType

DeclaredType

getAnnotationType()

Returns the type of this annotation.

getElementValues

```java
Map
<? extends
ExecutableElement
,​? extends
AnnotationValue
> getElementValues()
```

Returns the values of this annotation's elements.
This is returned in the form of a map that associates elements
with their corresponding values.
Only those elements with values explicitly present in the
annotation are included, not those that are implicitly assuming
their default values.
The order of the map matches the order in which the
values appear in the annotation's source.

Note that an annotation mirror of a marker annotation type
will by definition have an empty map.

To fill in default values, use

getElementValuesWithDefaults

.

**Returns:** the values of this annotation's elements,
or an empty map if there are none

---

#### getElementValues

Map

<? extends

ExecutableElement

,​? extends

AnnotationValue

> getElementValues()

Returns the values of this annotation's elements.
This is returned in the form of a map that associates elements
with their corresponding values.
Only those elements with values explicitly present in the
annotation are included, not those that are implicitly assuming
their default values.
The order of the map matches the order in which the
values appear in the annotation's source.

Note that an annotation mirror of a marker annotation type
will by definition have an empty map.

To fill in default values, use

getElementValuesWithDefaults

.

Note that an annotation mirror of a marker annotation type
will by definition have an empty map.

To fill in default values, use

getElementValuesWithDefaults

.

To fill in default values, use

getElementValuesWithDefaults

.

---

