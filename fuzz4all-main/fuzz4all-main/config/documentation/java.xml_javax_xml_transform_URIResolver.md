# Interface URIResolver

**Source:** `java.xml\javax\xml\transform\URIResolver.html`

### Class Description

```java
public interface
URIResolver
```

An object that implements this interface that can be called by the processor
to turn a URI used in document(), xsl:import, or xsl:include into a Source object.

**All Known Subinterfaces:** CatalogResolver

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Source
resolve​(
String
href,

String
base)
throws
TransformerException

Called by the processor when it encounters
an xsl:include, xsl:import, or document() function.

**Parameters:**
- href

- An href attribute, which may be relative or absolute.
- base

- The base URI against which the first argument will be made
absolute if the absolute URI is required.

**Returns:**
- A Source object, or null if the href cannot be resolved,
and the processor should try to resolve the URI itself.

**Throws:**
- TransformerException

- if an error occurs when trying to
resolve the URI.

---

### Additional Sections

#### Interface URIResolver

**All Known Subinterfaces:** CatalogResolver

```java
public interface
URIResolver
```

An object that implements this interface that can be called by the processor
to turn a URI used in document(), xsl:import, or xsl:include into a Source object.

**Since:** 1.4

public interface

URIResolver

An object that implements this interface that can be called by the processor
to turn a URI used in document(), xsl:import, or xsl:include into a Source object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Source

resolve

​(

String

href,

String

base)

Called by the processor when it encounters
an xsl:include, xsl:import, or document() function.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Source

resolve

​(

String

href,

String

base)

Called by the processor when it encounters
an xsl:include, xsl:import, or document() function.

---

#### Method Summary

Called by the processor when it encounters
an xsl:include, xsl:import, or document() function.

============ METHOD DETAIL ==========

- Method Detail

- resolve

```java
Source
resolve​(
String
href,

String
base)
throws
TransformerException
```

Called by the processor when it encounters
an xsl:include, xsl:import, or document() function.

**Parameters:** href

- An href attribute, which may be relative or absolute.
**Parameters:** base

- The base URI against which the first argument will be made
absolute if the absolute URI is required.
**Returns:** A Source object, or null if the href cannot be resolved,
and the processor should try to resolve the URI itself.
**Throws:** TransformerException

- if an error occurs when trying to
resolve the URI.

Method Detail

- resolve

```java
Source
resolve​(
String
href,

String
base)
throws
TransformerException
```

Called by the processor when it encounters
an xsl:include, xsl:import, or document() function.

**Parameters:** href

- An href attribute, which may be relative or absolute.
**Parameters:** base

- The base URI against which the first argument will be made
absolute if the absolute URI is required.
**Returns:** A Source object, or null if the href cannot be resolved,
and the processor should try to resolve the URI itself.
**Throws:** TransformerException

- if an error occurs when trying to
resolve the URI.

---

#### Method Detail

resolve

```java
Source
resolve​(
String
href,

String
base)
throws
TransformerException
```

Called by the processor when it encounters
an xsl:include, xsl:import, or document() function.

**Parameters:** href

- An href attribute, which may be relative or absolute.
**Parameters:** base

- The base URI against which the first argument will be made
absolute if the absolute URI is required.
**Returns:** A Source object, or null if the href cannot be resolved,
and the processor should try to resolve the URI itself.
**Throws:** TransformerException

- if an error occurs when trying to
resolve the URI.

---

#### resolve

Source

resolve​(

String

href,

String

base)
throws

TransformerException

Called by the processor when it encounters
an xsl:include, xsl:import, or document() function.

---

