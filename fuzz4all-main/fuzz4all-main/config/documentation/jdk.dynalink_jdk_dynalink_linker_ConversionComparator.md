# Interface ConversionComparator

**Source:** `jdk.dynalink\jdk\dynalink\linker\ConversionComparator.html`

### Class Description

```java
public interface
ConversionComparator
```

Optional interface to be implemented by

GuardingTypeConverterFactory

implementers. Language-specific conversions can cause increased overloaded
method resolution ambiguity, as many methods can become applicable because of
additional conversions. The static way of selecting the "most specific"
method will fail more often, because there will be multiple maximally
specific method with unrelated signatures. In these cases, language runtimes
can be asked to resolve the ambiguity by expressing preferences for one
conversion over the other.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ConversionComparator.Comparison
compareConversion​(
Class
<?> sourceType,

Class
<?> targetType1,

Class
<?> targetType2)

Determines which of the two target types is the preferred conversion
target from a source type.

**Parameters:**
- sourceType

- the source type.
- targetType1

- one potential target type
- targetType2

- another potential target type.

**Returns:**
- one of Comparison constants that establish which - if any - of
the target types is preferred for the conversion.

---

### Additional Sections

#### Interface ConversionComparator

```java
public interface
ConversionComparator
```

Optional interface to be implemented by

GuardingTypeConverterFactory

implementers. Language-specific conversions can cause increased overloaded
method resolution ambiguity, as many methods can become applicable because of
additional conversions. The static way of selecting the "most specific"
method will fail more often, because there will be multiple maximally
specific method with unrelated signatures. In these cases, language runtimes
can be asked to resolve the ambiguity by expressing preferences for one
conversion over the other.

public interface

ConversionComparator

Optional interface to be implemented by

GuardingTypeConverterFactory

implementers. Language-specific conversions can cause increased overloaded
method resolution ambiguity, as many methods can become applicable because of
additional conversions. The static way of selecting the "most specific"
method will fail more often, because there will be multiple maximally
specific method with unrelated signatures. In these cases, language runtimes
can be asked to resolve the ambiguity by expressing preferences for one
conversion over the other.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

ConversionComparator.Comparison

Enumeration of possible outcomes of comparing one conversion to another.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ConversionComparator.Comparison

compareConversion

​(

Class

<?> sourceType,

Class

<?> targetType1,

Class

<?> targetType2)

Determines which of the two target types is the preferred conversion
target from a source type.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

ConversionComparator.Comparison

Enumeration of possible outcomes of comparing one conversion to another.

---

#### Nested Class Summary

Enumeration of possible outcomes of comparing one conversion to another.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ConversionComparator.Comparison

compareConversion

​(

Class

<?> sourceType,

Class

<?> targetType1,

Class

<?> targetType2)

Determines which of the two target types is the preferred conversion
target from a source type.

---

#### Method Summary

Determines which of the two target types is the preferred conversion
target from a source type.

============ METHOD DETAIL ==========

- Method Detail

- compareConversion

```java
ConversionComparator.Comparison
compareConversion​(
Class
<?> sourceType,

Class
<?> targetType1,

Class
<?> targetType2)
```

Determines which of the two target types is the preferred conversion
target from a source type.

**Parameters:** sourceType

- the source type.
**Parameters:** targetType1

- one potential target type
**Parameters:** targetType2

- another potential target type.
**Returns:** one of Comparison constants that establish which - if any - of
the target types is preferred for the conversion.

Method Detail

- compareConversion

```java
ConversionComparator.Comparison
compareConversion​(
Class
<?> sourceType,

Class
<?> targetType1,

Class
<?> targetType2)
```

Determines which of the two target types is the preferred conversion
target from a source type.

**Parameters:** sourceType

- the source type.
**Parameters:** targetType1

- one potential target type
**Parameters:** targetType2

- another potential target type.
**Returns:** one of Comparison constants that establish which - if any - of
the target types is preferred for the conversion.

---

#### Method Detail

compareConversion

```java
ConversionComparator.Comparison
compareConversion​(
Class
<?> sourceType,

Class
<?> targetType1,

Class
<?> targetType2)
```

Determines which of the two target types is the preferred conversion
target from a source type.

**Parameters:** sourceType

- the source type.
**Parameters:** targetType1

- one potential target type
**Parameters:** targetType2

- another potential target type.
**Returns:** one of Comparison constants that establish which - if any - of
the target types is preferred for the conversion.

---

#### compareConversion

ConversionComparator.Comparison

compareConversion​(

Class

<?> sourceType,

Class

<?> targetType1,

Class

<?> targetType2)

Determines which of the two target types is the preferred conversion
target from a source type.

---

