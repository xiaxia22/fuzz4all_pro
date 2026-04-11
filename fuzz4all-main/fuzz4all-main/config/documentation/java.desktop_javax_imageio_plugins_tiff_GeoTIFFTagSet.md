# Class GeoTIFFTagSet

**Source:** `java.desktop\javax\imageio\plugins\tiff\GeoTIFFTagSet.html`

### Class Description

```java
public final class
GeoTIFFTagSet

extends
TIFFTagSet
```

A class representing the tags found in a GeoTIFF IFD. GeoTIFF is a
standard for annotating georeferenced or geocoded raster imagery.
This class does

not

handle the

GeoKey

s referenced
from a

GeoKeyDirectoryTag

as those are not TIFF tags per se.

The definitions of the data types referenced by the field
definitions may be found in the

TIFFTag

class.

**Since:** 9

---

### Field Details

#### public static final int TAG_MODEL_PIXEL_SCALE

A tag used to specify the size of raster pixel spacing in
model space units.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_MODEL_TRANSFORMATION

A tag used to specify the transformation matrix between the raster
space and the model space.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_MODEL_TIE_POINT

A tag used to store raster-to-model tiepoint pairs.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GEO_KEY_DIRECTORY

A tag used to store the

GeoKey

directory.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GEO_DOUBLE_PARAMS

A tag used to store all

double

-values

GeoKey

s.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GEO_ASCII_PARAMS

A tag used to store all ASCII-values

GeoKey

s.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### public static
GeoTIFFTagSet
getInstance()

Returns a shared instance of a

GeoTIFFTagSet

.

**Returns:**
- a

GeoTIFFTagSet

instance.

---

### Additional Sections

#### Class GeoTIFFTagSet

java.lang.Object

- javax.imageio.plugins.tiff.TIFFTagSet
- - javax.imageio.plugins.tiff.GeoTIFFTagSet

javax.imageio.plugins.tiff.TIFFTagSet

- javax.imageio.plugins.tiff.GeoTIFFTagSet

javax.imageio.plugins.tiff.GeoTIFFTagSet

```java
public final class
GeoTIFFTagSet

extends
TIFFTagSet
```

A class representing the tags found in a GeoTIFF IFD. GeoTIFF is a
standard for annotating georeferenced or geocoded raster imagery.
This class does

not

handle the

GeoKey

s referenced
from a

GeoKeyDirectoryTag

as those are not TIFF tags per se.

The definitions of the data types referenced by the field
definitions may be found in the

TIFFTag

class.

**Since:** 9

public final class

GeoTIFFTagSet

extends

TIFFTagSet

A class representing the tags found in a GeoTIFF IFD. GeoTIFF is a
standard for annotating georeferenced or geocoded raster imagery.
This class does

not

handle the

GeoKey

s referenced
from a

GeoKeyDirectoryTag

as those are not TIFF tags per se.

The definitions of the data types referenced by the field
definitions may be found in the

TIFFTag

class.

The definitions of the data types referenced by the field
definitions may be found in the

TIFFTag

class.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

TAG_GEO_ASCII_PARAMS

A tag used to store all ASCII-values

GeoKey

s.

static int

TAG_GEO_DOUBLE_PARAMS

A tag used to store all

double

-values

GeoKey

s.

static int

TAG_GEO_KEY_DIRECTORY

A tag used to store the

GeoKey

directory.

static int

TAG_MODEL_PIXEL_SCALE

A tag used to specify the size of raster pixel spacing in
model space units.

static int

TAG_MODEL_TIE_POINT

A tag used to store raster-to-model tiepoint pairs.

static int

TAG_MODEL_TRANSFORMATION

A tag used to specify the transformation matrix between the raster
space and the model space.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

GeoTIFFTagSet

getInstance

()

Returns a shared instance of a

GeoTIFFTagSet

.

- Methods declared in class javax.imageio.plugins.tiff.

TIFFTagSet

getTag

,

getTag

,

getTagNames

,

getTagNumbers

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

TAG_GEO_ASCII_PARAMS

A tag used to store all ASCII-values

GeoKey

s.

static int

TAG_GEO_DOUBLE_PARAMS

A tag used to store all

double

-values

GeoKey

s.

static int

TAG_GEO_KEY_DIRECTORY

A tag used to store the

GeoKey

directory.

static int

TAG_MODEL_PIXEL_SCALE

A tag used to specify the size of raster pixel spacing in
model space units.

static int

TAG_MODEL_TIE_POINT

A tag used to store raster-to-model tiepoint pairs.

static int

TAG_MODEL_TRANSFORMATION

A tag used to specify the transformation matrix between the raster
space and the model space.

---

#### Field Summary

A tag used to store all ASCII-values

GeoKey

s.

A tag used to store all

double

-values

GeoKey

s.

A tag used to store the

GeoKey

directory.

A tag used to specify the size of raster pixel spacing in
model space units.

A tag used to store raster-to-model tiepoint pairs.

A tag used to specify the transformation matrix between the raster
space and the model space.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

GeoTIFFTagSet

getInstance

()

Returns a shared instance of a

GeoTIFFTagSet

.

- Methods declared in class javax.imageio.plugins.tiff.

TIFFTagSet

getTag

,

getTag

,

getTagNames

,

getTagNumbers

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

Returns a shared instance of a

GeoTIFFTagSet

.

Methods declared in class javax.imageio.plugins.tiff.

TIFFTagSet

getTag

,

getTag

,

getTagNames

,

getTagNumbers

---

#### Methods declared in class javax.imageio.plugins.tiff. TIFFTagSet

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

============ FIELD DETAIL ===========

- Field Detail

- TAG_MODEL_PIXEL_SCALE

```java
public static final int TAG_MODEL_PIXEL_SCALE
```

A tag used to specify the size of raster pixel spacing in
model space units.

**See Also:** Constant Field Values

- TAG_MODEL_TRANSFORMATION

```java
public static final int TAG_MODEL_TRANSFORMATION
```

A tag used to specify the transformation matrix between the raster
space and the model space.

**See Also:** Constant Field Values

- TAG_MODEL_TIE_POINT

```java
public static final int TAG_MODEL_TIE_POINT
```

A tag used to store raster-to-model tiepoint pairs.

**See Also:** Constant Field Values

- TAG_GEO_KEY_DIRECTORY

```java
public static final int TAG_GEO_KEY_DIRECTORY
```

A tag used to store the

GeoKey

directory.

**See Also:** Constant Field Values

- TAG_GEO_DOUBLE_PARAMS

```java
public static final int TAG_GEO_DOUBLE_PARAMS
```

A tag used to store all

double

-values

GeoKey

s.

**See Also:** Constant Field Values

- TAG_GEO_ASCII_PARAMS

```java
public static final int TAG_GEO_ASCII_PARAMS
```

A tag used to store all ASCII-values

GeoKey

s.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getInstance

```java
public static
GeoTIFFTagSet
getInstance()
```

Returns a shared instance of a

GeoTIFFTagSet

.

**Returns:** a

GeoTIFFTagSet

instance.

Field Detail

- TAG_MODEL_PIXEL_SCALE

```java
public static final int TAG_MODEL_PIXEL_SCALE
```

A tag used to specify the size of raster pixel spacing in
model space units.

**See Also:** Constant Field Values

- TAG_MODEL_TRANSFORMATION

```java
public static final int TAG_MODEL_TRANSFORMATION
```

A tag used to specify the transformation matrix between the raster
space and the model space.

**See Also:** Constant Field Values

- TAG_MODEL_TIE_POINT

```java
public static final int TAG_MODEL_TIE_POINT
```

A tag used to store raster-to-model tiepoint pairs.

**See Also:** Constant Field Values

- TAG_GEO_KEY_DIRECTORY

```java
public static final int TAG_GEO_KEY_DIRECTORY
```

A tag used to store the

GeoKey

directory.

**See Also:** Constant Field Values

- TAG_GEO_DOUBLE_PARAMS

```java
public static final int TAG_GEO_DOUBLE_PARAMS
```

A tag used to store all

double

-values

GeoKey

s.

**See Also:** Constant Field Values

- TAG_GEO_ASCII_PARAMS

```java
public static final int TAG_GEO_ASCII_PARAMS
```

A tag used to store all ASCII-values

GeoKey

s.

**See Also:** Constant Field Values

---

#### Field Detail

TAG_MODEL_PIXEL_SCALE

```java
public static final int TAG_MODEL_PIXEL_SCALE
```

A tag used to specify the size of raster pixel spacing in
model space units.

**See Also:** Constant Field Values

---

#### TAG_MODEL_PIXEL_SCALE

public static final int TAG_MODEL_PIXEL_SCALE

A tag used to specify the size of raster pixel spacing in
model space units.

TAG_MODEL_TRANSFORMATION

```java
public static final int TAG_MODEL_TRANSFORMATION
```

A tag used to specify the transformation matrix between the raster
space and the model space.

**See Also:** Constant Field Values

---

#### TAG_MODEL_TRANSFORMATION

public static final int TAG_MODEL_TRANSFORMATION

A tag used to specify the transformation matrix between the raster
space and the model space.

TAG_MODEL_TIE_POINT

```java
public static final int TAG_MODEL_TIE_POINT
```

A tag used to store raster-to-model tiepoint pairs.

**See Also:** Constant Field Values

---

#### TAG_MODEL_TIE_POINT

public static final int TAG_MODEL_TIE_POINT

A tag used to store raster-to-model tiepoint pairs.

TAG_GEO_KEY_DIRECTORY

```java
public static final int TAG_GEO_KEY_DIRECTORY
```

A tag used to store the

GeoKey

directory.

**See Also:** Constant Field Values

---

#### TAG_GEO_KEY_DIRECTORY

public static final int TAG_GEO_KEY_DIRECTORY

A tag used to store the

GeoKey

directory.

TAG_GEO_DOUBLE_PARAMS

```java
public static final int TAG_GEO_DOUBLE_PARAMS
```

A tag used to store all

double

-values

GeoKey

s.

**See Also:** Constant Field Values

---

#### TAG_GEO_DOUBLE_PARAMS

public static final int TAG_GEO_DOUBLE_PARAMS

A tag used to store all

double

-values

GeoKey

s.

TAG_GEO_ASCII_PARAMS

```java
public static final int TAG_GEO_ASCII_PARAMS
```

A tag used to store all ASCII-values

GeoKey

s.

**See Also:** Constant Field Values

---

#### TAG_GEO_ASCII_PARAMS

public static final int TAG_GEO_ASCII_PARAMS

A tag used to store all ASCII-values

GeoKey

s.

Method Detail

- getInstance

```java
public static
GeoTIFFTagSet
getInstance()
```

Returns a shared instance of a

GeoTIFFTagSet

.

**Returns:** a

GeoTIFFTagSet

instance.

---

#### Method Detail

getInstance

```java
public static
GeoTIFFTagSet
getInstance()
```

Returns a shared instance of a

GeoTIFFTagSet

.

**Returns:** a

GeoTIFFTagSet

instance.

---

#### getInstance

public static

GeoTIFFTagSet

getInstance()

Returns a shared instance of a

GeoTIFFTagSet

.

---

