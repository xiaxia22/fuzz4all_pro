# Interface AnnotationDesc

**Source:** `jdk.javadoc\com\sun\javadoc\AnnotationDesc.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
AnnotationDesc
```

Represents an annotation.
An annotation associates a value with each element of an annotation type.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### AnnotationTypeDoc
annotationType()

Returns the annotation type of this annotation.

**Returns:**
- the annotation type of this annotation.

---

#### AnnotationDesc.ElementValuePair
[] elementValues()

Returns this annotation's elements and their values.
Only those explicitly present in the annotation are
included, not those assuming their default values.
Returns an empty array if there are none.

**Returns:**
- this annotation's elements and their values.

---

#### boolean isSynthesized()

Check for the synthesized bit on the annotation.

**Returns:**
- true if the annotation is synthesized.

---

### Additional Sections

#### Interface AnnotationDesc

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
AnnotationDesc
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

Represents an annotation.
An annotation associates a value with each element of an annotation type.

**Since:** 1.5

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

AnnotationDesc

Represents an annotation.
An annotation associates a value with each element of an annotation type.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

AnnotationDesc.ElementValuePair

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

AnnotationTypeDoc

annotationType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the annotation type of this annotation.

AnnotationDesc.ElementValuePair

[]

elementValues

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this annotation's elements and their values.

boolean

isSynthesized

()

Deprecated, for removal: This API element is subject to removal in a future version.

Check for the synthesized bit on the annotation.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

AnnotationDesc.ElementValuePair

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.

---

#### Nested Class Summary

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

AnnotationTypeDoc

annotationType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the annotation type of this annotation.

AnnotationDesc.ElementValuePair

[]

elementValues

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this annotation's elements and their values.

boolean

isSynthesized

()

Deprecated, for removal: This API element is subject to removal in a future version.

Check for the synthesized bit on the annotation.

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the annotation type of this annotation.

Returns this annotation's elements and their values.

Check for the synthesized bit on the annotation.

============ METHOD DETAIL ==========

- Method Detail

- annotationType

```java
AnnotationTypeDoc
annotationType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the annotation type of this annotation.

**Returns:** the annotation type of this annotation.

- elementValues

```java
AnnotationDesc.ElementValuePair
[] elementValues()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this annotation's elements and their values.
Only those explicitly present in the annotation are
included, not those assuming their default values.
Returns an empty array if there are none.

**Returns:** this annotation's elements and their values.

- isSynthesized

```java
boolean isSynthesized()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Check for the synthesized bit on the annotation.

**Returns:** true if the annotation is synthesized.

Method Detail

- annotationType

```java
AnnotationTypeDoc
annotationType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the annotation type of this annotation.

**Returns:** the annotation type of this annotation.

- elementValues

```java
AnnotationDesc.ElementValuePair
[] elementValues()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this annotation's elements and their values.
Only those explicitly present in the annotation are
included, not those assuming their default values.
Returns an empty array if there are none.

**Returns:** this annotation's elements and their values.

- isSynthesized

```java
boolean isSynthesized()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Check for the synthesized bit on the annotation.

**Returns:** true if the annotation is synthesized.

---

#### Method Detail

annotationType

```java
AnnotationTypeDoc
annotationType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the annotation type of this annotation.

**Returns:** the annotation type of this annotation.

---

#### annotationType

AnnotationTypeDoc

annotationType()

Returns the annotation type of this annotation.

elementValues

```java
AnnotationDesc.ElementValuePair
[] elementValues()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this annotation's elements and their values.
Only those explicitly present in the annotation are
included, not those assuming their default values.
Returns an empty array if there are none.

**Returns:** this annotation's elements and their values.

---

#### elementValues

AnnotationDesc.ElementValuePair

[] elementValues()

Returns this annotation's elements and their values.
Only those explicitly present in the annotation are
included, not those assuming their default values.
Returns an empty array if there are none.

isSynthesized

```java
boolean isSynthesized()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Check for the synthesized bit on the annotation.

**Returns:** true if the annotation is synthesized.

---

#### isSynthesized

boolean isSynthesized()

Check for the synthesized bit on the annotation.

---

