# Class ICC_ColorSpace

**Source:** `java.desktop\java\awt\color\ICC_ColorSpace.html`

### Class Description

```java
public class
ICC_ColorSpace

extends
ColorSpace
```

The ICC_ColorSpace class is an implementation of the abstract
ColorSpace class. This representation of
device independent and device dependent color spaces is based on the
International Color Consortium Specification ICC.1:2001-12, File Format for
Color Profiles (see

http://www.color.org

).

Typically, a Color or ColorModel would be associated with an ICC
Profile which is either an input, display, or output profile (see
the ICC specification). There are other types of ICC Profiles, e.g.
abstract profiles, device link profiles, and named color profiles,
which do not contain information appropriate for representing the color
space of a color, image, or device (see ICC_Profile).
Attempting to create an ICC_ColorSpace object from an inappropriate ICC
Profile is an error.

ICC Profiles represent transformations from the color space of
the profile (e.g. a monitor) to a Profile Connection Space (PCS).
Profiles of interest for tagging images or colors have a
PCS which is one of the device independent
spaces (one CIEXYZ space and two CIELab spaces) defined in the
ICC Profile Format Specification. Most profiles of interest
either have invertible transformations or explicitly specify
transformations going both directions. Should an ICC_ColorSpace
object be used in a way requiring a conversion from PCS to
the profile's native space and there is inadequate data to
correctly perform the conversion, the ICC_ColorSpace object will
produce output in the specified type of color space (e.g. TYPE_RGB,
TYPE_CMYK, etc.), but the specific color values of the output data
will be undefined.

The details of this class are not important for simple applets,
which draw in a default color space or manipulate and display
imported images with a known color space. At most, such applets
would need to get one of the default color spaces via
ColorSpace.getInstance().

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ICC_ColorSpace​(
ICC_Profile
profile)

Constructs a new ICC_ColorSpace from an ICC_Profile object.

**Parameters:**
- profile

- the specified ICC_Profile object

**Throws:**
- IllegalArgumentException

- if profile is inappropriate for
representing a ColorSpace.

---

### Method Details

#### public
ICC_Profile
getProfile()

Returns the ICC_Profile for this ICC_ColorSpace.

**Returns:**
- the ICC_Profile for this ICC_ColorSpace.

---

#### public float[] toRGB​(float[] colorvalue)

Transforms a color value assumed to be in this ColorSpace
into a value in the default CS_sRGB color space.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of this color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of the CS_sRGB color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

**Specified by:**
- toRGB

in class

ColorSpace

**Parameters:**
- colorvalue

- a float array with length of at least the number
of components in this ColorSpace.

**Returns:**
- a float array of length 3.

**Throws:**
- ArrayIndexOutOfBoundsException

- if array length is not
at least the number of components in this ColorSpace.

---

#### public float[] fromRGB​(float[] rgbvalue)

Transforms a color value assumed to be in the default CS_sRGB
color space into this ColorSpace.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of the CS_sRGB color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of this color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

**Specified by:**
- fromRGB

in class

ColorSpace

**Parameters:**
- rgbvalue

- a float array with length of at least 3.

**Returns:**
- a float array with length equal to the number of
components in this ColorSpace.

**Throws:**
- ArrayIndexOutOfBoundsException

- if array length is not
at least 3.

---

#### public float[] toCIEXYZ​(float[] colorvalue)

Transforms a color value assumed to be in this ColorSpace
into the CS_CIEXYZ conversion color space.

This method transforms color values using relative colorimetry,
as defined by the ICC Specification. This
means that the XYZ values returned by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. This
representation is not the same as the XYZ values that would
be measured from the given color value by a colorimeter.
A further transformation is necessary to compute the XYZ values
that would be measured using current CIE recommended practices.
The paragraphs below explain this in more detail.

The ICC standard uses a device independent color space (DICS) as the
mechanism for converting color from one device to another device. In
this architecture, colors are converted from the source device's color
space to the ICC DICS and then from the ICC DICS to the destination
device's color space. The ICC standard defines device profiles which
contain transforms which will convert between a device's color space
and the ICC DICS. The overall conversion of colors from a source
device to colors of a destination device is done by connecting the
device-to-DICS transform of the profile for the source device to the
DICS-to-device transform of the profile for the destination device.
For this reason, the ICC DICS is commonly referred to as the profile
connection space (PCS). The color space used in the methods
toCIEXYZ and fromCIEXYZ is the CIEXYZ PCS defined by the ICC
Specification. This is also the color space represented by
ColorSpace.CS_CIEXYZ.

The XYZ values of a color are often represented as relative to some
white point, so the actual meaning of the XYZ values cannot be known
without knowing the white point of those values. This is known as
relative colorimetry. The PCS uses a white point of D50, so the XYZ
values of the PCS are relative to D50. For example, white in the PCS
will have the XYZ values of D50, which is defined to be X=.9642,
Y=1.000, and Z=0.8249. This white point is commonly used for graphic
arts applications, but others are often used in other applications.

To quantify the color characteristics of a device such as a printer
or monitor, measurements of XYZ values for particular device colors
are typically made. For purposes of this discussion, the term
device XYZ values is used to mean the XYZ values that would be
measured from device colors using current CIE recommended practices.

Converting between device XYZ values and the PCS XYZ values returned
by this method corresponds to converting between the device's color
space, as represented by CIE colorimetric values, and the PCS. There
are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

**Specified by:**
- toCIEXYZ

in class

ColorSpace

**Parameters:**
- colorvalue

- a float array with length of at least the number
of components in this ColorSpace.

**Returns:**
- a float array of length 3.

**Throws:**
- ArrayIndexOutOfBoundsException

- if array length is not
at least the number of components in this ColorSpace.

---

#### public float[] fromCIEXYZ​(float[] colorvalue)

Transforms a color value assumed to be in the CS_CIEXYZ conversion
color space into this ColorSpace.

This method transforms color values using relative colorimetry,
as defined by the ICC Specification. This
means that the XYZ argument values taken by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. The color
values returned by this method are not those that would produce
the XYZ value passed to the method when measured by a colorimeter.
If you have XYZ values corresponding to measurements made using
current CIE recommended practices, they must be converted to D50
relative values before being passed to this method.
The paragraphs below explain this in more detail.

The ICC standard uses a device independent color space (DICS) as the
mechanism for converting color from one device to another device. In
this architecture, colors are converted from the source device's color
space to the ICC DICS and then from the ICC DICS to the destination
device's color space. The ICC standard defines device profiles which
contain transforms which will convert between a device's color space
and the ICC DICS. The overall conversion of colors from a source
device to colors of a destination device is done by connecting the
device-to-DICS transform of the profile for the source device to the
DICS-to-device transform of the profile for the destination device.
For this reason, the ICC DICS is commonly referred to as the profile
connection space (PCS). The color space used in the methods
toCIEXYZ and fromCIEXYZ is the CIEXYZ PCS defined by the ICC
Specification. This is also the color space represented by
ColorSpace.CS_CIEXYZ.

The XYZ values of a color are often represented as relative to some
white point, so the actual meaning of the XYZ values cannot be known
without knowing the white point of those values. This is known as
relative colorimetry. The PCS uses a white point of D50, so the XYZ
values of the PCS are relative to D50. For example, white in the PCS
will have the XYZ values of D50, which is defined to be X=.9642,
Y=1.000, and Z=0.8249. This white point is commonly used for graphic
arts applications, but others are often used in other applications.

To quantify the color characteristics of a device such as a printer
or monitor, measurements of XYZ values for particular device colors
are typically made. For purposes of this discussion, the term
device XYZ values is used to mean the XYZ values that would be
measured from device colors using current CIE recommended practices.

Converting between device XYZ values and the PCS XYZ values taken as
arguments by this method corresponds to converting between the device's
color space, as represented by CIE colorimetric values, and the PCS.
There are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

**Specified by:**
- fromCIEXYZ

in class

ColorSpace

**Parameters:**
- colorvalue

- a float array with length of at least 3.

**Returns:**
- a float array with length equal to the number of
components in this ColorSpace.

**Throws:**
- ArrayIndexOutOfBoundsException

- if array length is not
at least 3.

---

#### public float getMinValue​(int component)

Returns the minimum normalized color component value for the
specified component. For TYPE_XYZ spaces, this method returns
minimum values of 0.0 for all components. For TYPE_Lab spaces,
this method returns 0.0 for L and -128.0 for a and b components.
This is consistent with the encoding of the XYZ and Lab Profile
Connection Spaces in the ICC specification. For all other types, this
method returns 0.0 for all components. When using an ICC_ColorSpace
with a profile that requires different minimum component values,
it is necessary to subclass this class and override this method.

**Overrides:**
- getMinValue

in class

ColorSpace

**Parameters:**
- component

- The component index.

**Returns:**
- The minimum normalized component value.

**Throws:**
- IllegalArgumentException

- if component is less than 0 or
greater than numComponents - 1.

**Since:**
- 1.4

---

#### public float getMaxValue​(int component)

Returns the maximum normalized color component value for the
specified component. For TYPE_XYZ spaces, this method returns
maximum values of 1.0 + (32767.0 / 32768.0) for all components.
For TYPE_Lab spaces,
this method returns 100.0 for L and 127.0 for a and b components.
This is consistent with the encoding of the XYZ and Lab Profile
Connection Spaces in the ICC specification. For all other types, this
method returns 1.0 for all components. When using an ICC_ColorSpace
with a profile that requires different maximum component values,
it is necessary to subclass this class and override this method.

**Overrides:**
- getMaxValue

in class

ColorSpace

**Parameters:**
- component

- The component index.

**Returns:**
- The maximum normalized component value.

**Throws:**
- IllegalArgumentException

- if component is less than 0 or
greater than numComponents - 1.

**Since:**
- 1.4

---

### Additional Sections

#### Class ICC_ColorSpace

java.lang.Object

- java.awt.color.ColorSpace
- - java.awt.color.ICC_ColorSpace

java.awt.color.ColorSpace

- java.awt.color.ICC_ColorSpace

java.awt.color.ICC_ColorSpace

**All Implemented Interfaces:** Serializable

```java
public class
ICC_ColorSpace

extends
ColorSpace
```

The ICC_ColorSpace class is an implementation of the abstract
ColorSpace class. This representation of
device independent and device dependent color spaces is based on the
International Color Consortium Specification ICC.1:2001-12, File Format for
Color Profiles (see

http://www.color.org

).

Typically, a Color or ColorModel would be associated with an ICC
Profile which is either an input, display, or output profile (see
the ICC specification). There are other types of ICC Profiles, e.g.
abstract profiles, device link profiles, and named color profiles,
which do not contain information appropriate for representing the color
space of a color, image, or device (see ICC_Profile).
Attempting to create an ICC_ColorSpace object from an inappropriate ICC
Profile is an error.

ICC Profiles represent transformations from the color space of
the profile (e.g. a monitor) to a Profile Connection Space (PCS).
Profiles of interest for tagging images or colors have a
PCS which is one of the device independent
spaces (one CIEXYZ space and two CIELab spaces) defined in the
ICC Profile Format Specification. Most profiles of interest
either have invertible transformations or explicitly specify
transformations going both directions. Should an ICC_ColorSpace
object be used in a way requiring a conversion from PCS to
the profile's native space and there is inadequate data to
correctly perform the conversion, the ICC_ColorSpace object will
produce output in the specified type of color space (e.g. TYPE_RGB,
TYPE_CMYK, etc.), but the specific color values of the output data
will be undefined.

The details of this class are not important for simple applets,
which draw in a default color space or manipulate and display
imported images with a known color space. At most, such applets
would need to get one of the default color spaces via
ColorSpace.getInstance().

**See Also:** ColorSpace

,

ICC_Profile

,

Serialized Form

public class

ICC_ColorSpace

extends

ColorSpace

The ICC_ColorSpace class is an implementation of the abstract
ColorSpace class. This representation of
device independent and device dependent color spaces is based on the
International Color Consortium Specification ICC.1:2001-12, File Format for
Color Profiles (see

http://www.color.org

).

Typically, a Color or ColorModel would be associated with an ICC
Profile which is either an input, display, or output profile (see
the ICC specification). There are other types of ICC Profiles, e.g.
abstract profiles, device link profiles, and named color profiles,
which do not contain information appropriate for representing the color
space of a color, image, or device (see ICC_Profile).
Attempting to create an ICC_ColorSpace object from an inappropriate ICC
Profile is an error.

ICC Profiles represent transformations from the color space of
the profile (e.g. a monitor) to a Profile Connection Space (PCS).
Profiles of interest for tagging images or colors have a
PCS which is one of the device independent
spaces (one CIEXYZ space and two CIELab spaces) defined in the
ICC Profile Format Specification. Most profiles of interest
either have invertible transformations or explicitly specify
transformations going both directions. Should an ICC_ColorSpace
object be used in a way requiring a conversion from PCS to
the profile's native space and there is inadequate data to
correctly perform the conversion, the ICC_ColorSpace object will
produce output in the specified type of color space (e.g. TYPE_RGB,
TYPE_CMYK, etc.), but the specific color values of the output data
will be undefined.

The details of this class are not important for simple applets,
which draw in a default color space or manipulate and display
imported images with a known color space. At most, such applets
would need to get one of the default color spaces via
ColorSpace.getInstance().

Typically, a Color or ColorModel would be associated with an ICC
Profile which is either an input, display, or output profile (see
the ICC specification). There are other types of ICC Profiles, e.g.
abstract profiles, device link profiles, and named color profiles,
which do not contain information appropriate for representing the color
space of a color, image, or device (see ICC_Profile).
Attempting to create an ICC_ColorSpace object from an inappropriate ICC
Profile is an error.

ICC Profiles represent transformations from the color space of
the profile (e.g. a monitor) to a Profile Connection Space (PCS).
Profiles of interest for tagging images or colors have a
PCS which is one of the device independent
spaces (one CIEXYZ space and two CIELab spaces) defined in the
ICC Profile Format Specification. Most profiles of interest
either have invertible transformations or explicitly specify
transformations going both directions. Should an ICC_ColorSpace
object be used in a way requiring a conversion from PCS to
the profile's native space and there is inadequate data to
correctly perform the conversion, the ICC_ColorSpace object will
produce output in the specified type of color space (e.g. TYPE_RGB,
TYPE_CMYK, etc.), but the specific color values of the output data
will be undefined.

The details of this class are not important for simple applets,
which draw in a default color space or manipulate and display
imported images with a known color space. At most, such applets
would need to get one of the default color spaces via
ColorSpace.getInstance().

ICC Profiles represent transformations from the color space of
the profile (e.g. a monitor) to a Profile Connection Space (PCS).
Profiles of interest for tagging images or colors have a
PCS which is one of the device independent
spaces (one CIEXYZ space and two CIELab spaces) defined in the
ICC Profile Format Specification. Most profiles of interest
either have invertible transformations or explicitly specify
transformations going both directions. Should an ICC_ColorSpace
object be used in a way requiring a conversion from PCS to
the profile's native space and there is inadequate data to
correctly perform the conversion, the ICC_ColorSpace object will
produce output in the specified type of color space (e.g. TYPE_RGB,
TYPE_CMYK, etc.), but the specific color values of the output data
will be undefined.

The details of this class are not important for simple applets,
which draw in a default color space or manipulate and display
imported images with a known color space. At most, such applets
would need to get one of the default color spaces via
ColorSpace.getInstance().

The details of this class are not important for simple applets,
which draw in a default color space or manipulate and display
imported images with a known color space. At most, such applets
would need to get one of the default color spaces via
ColorSpace.getInstance().

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.awt.color.

ColorSpace

CS_CIEXYZ

,

CS_GRAY

,

CS_LINEAR_RGB

,

CS_PYCC

,

CS_sRGB

,

TYPE_2CLR

,

TYPE_3CLR

,

TYPE_4CLR

,

TYPE_5CLR

,

TYPE_6CLR

,

TYPE_7CLR

,

TYPE_8CLR

,

TYPE_9CLR

,

TYPE_ACLR

,

TYPE_BCLR

,

TYPE_CCLR

,

TYPE_CMY

,

TYPE_CMYK

,

TYPE_DCLR

,

TYPE_ECLR

,

TYPE_FCLR

,

TYPE_GRAY

,

TYPE_HLS

,

TYPE_HSV

,

TYPE_Lab

,

TYPE_Luv

,

TYPE_RGB

,

TYPE_XYZ

,

TYPE_YCbCr

,

TYPE_Yxy

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ICC_ColorSpace

​(

ICC_Profile

profile)

Constructs a new ICC_ColorSpace from an ICC_Profile object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

float[]

fromCIEXYZ

​(float[] colorvalue)

Transforms a color value assumed to be in the CS_CIEXYZ conversion
color space into this ColorSpace.

float[]

fromRGB

​(float[] rgbvalue)

Transforms a color value assumed to be in the default CS_sRGB
color space into this ColorSpace.

float

getMaxValue

​(int component)

Returns the maximum normalized color component value for the
specified component.

float

getMinValue

​(int component)

Returns the minimum normalized color component value for the
specified component.

ICC_Profile

getProfile

()

Returns the ICC_Profile for this ICC_ColorSpace.

float[]

toCIEXYZ

​(float[] colorvalue)

Transforms a color value assumed to be in this ColorSpace
into the CS_CIEXYZ conversion color space.

float[]

toRGB

​(float[] colorvalue)

Transforms a color value assumed to be in this ColorSpace
into a value in the default CS_sRGB color space.

- Methods declared in class java.awt.color.

ColorSpace

getInstance

,

getName

,

getNumComponents

,

getType

,

isCS_sRGB

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

- Fields declared in class java.awt.color.

ColorSpace

CS_CIEXYZ

,

CS_GRAY

,

CS_LINEAR_RGB

,

CS_PYCC

,

CS_sRGB

,

TYPE_2CLR

,

TYPE_3CLR

,

TYPE_4CLR

,

TYPE_5CLR

,

TYPE_6CLR

,

TYPE_7CLR

,

TYPE_8CLR

,

TYPE_9CLR

,

TYPE_ACLR

,

TYPE_BCLR

,

TYPE_CCLR

,

TYPE_CMY

,

TYPE_CMYK

,

TYPE_DCLR

,

TYPE_ECLR

,

TYPE_FCLR

,

TYPE_GRAY

,

TYPE_HLS

,

TYPE_HSV

,

TYPE_Lab

,

TYPE_Luv

,

TYPE_RGB

,

TYPE_XYZ

,

TYPE_YCbCr

,

TYPE_Yxy

---

#### Field Summary

Fields declared in class java.awt.color.

ColorSpace

CS_CIEXYZ

,

CS_GRAY

,

CS_LINEAR_RGB

,

CS_PYCC

,

CS_sRGB

,

TYPE_2CLR

,

TYPE_3CLR

,

TYPE_4CLR

,

TYPE_5CLR

,

TYPE_6CLR

,

TYPE_7CLR

,

TYPE_8CLR

,

TYPE_9CLR

,

TYPE_ACLR

,

TYPE_BCLR

,

TYPE_CCLR

,

TYPE_CMY

,

TYPE_CMYK

,

TYPE_DCLR

,

TYPE_ECLR

,

TYPE_FCLR

,

TYPE_GRAY

,

TYPE_HLS

,

TYPE_HSV

,

TYPE_Lab

,

TYPE_Luv

,

TYPE_RGB

,

TYPE_XYZ

,

TYPE_YCbCr

,

TYPE_Yxy

---

#### Fields declared in class java.awt.color. ColorSpace

Constructor Summary

Constructors

Constructor

Description

ICC_ColorSpace

​(

ICC_Profile

profile)

Constructs a new ICC_ColorSpace from an ICC_Profile object.

---

#### Constructor Summary

Constructs a new ICC_ColorSpace from an ICC_Profile object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

float[]

fromCIEXYZ

​(float[] colorvalue)

Transforms a color value assumed to be in the CS_CIEXYZ conversion
color space into this ColorSpace.

float[]

fromRGB

​(float[] rgbvalue)

Transforms a color value assumed to be in the default CS_sRGB
color space into this ColorSpace.

float

getMaxValue

​(int component)

Returns the maximum normalized color component value for the
specified component.

float

getMinValue

​(int component)

Returns the minimum normalized color component value for the
specified component.

ICC_Profile

getProfile

()

Returns the ICC_Profile for this ICC_ColorSpace.

float[]

toCIEXYZ

​(float[] colorvalue)

Transforms a color value assumed to be in this ColorSpace
into the CS_CIEXYZ conversion color space.

float[]

toRGB

​(float[] colorvalue)

Transforms a color value assumed to be in this ColorSpace
into a value in the default CS_sRGB color space.

- Methods declared in class java.awt.color.

ColorSpace

getInstance

,

getName

,

getNumComponents

,

getType

,

isCS_sRGB

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

Transforms a color value assumed to be in the CS_CIEXYZ conversion
color space into this ColorSpace.

Transforms a color value assumed to be in the default CS_sRGB
color space into this ColorSpace.

Returns the maximum normalized color component value for the
specified component.

Returns the minimum normalized color component value for the
specified component.

Returns the ICC_Profile for this ICC_ColorSpace.

Transforms a color value assumed to be in this ColorSpace
into the CS_CIEXYZ conversion color space.

Transforms a color value assumed to be in this ColorSpace
into a value in the default CS_sRGB color space.

Methods declared in class java.awt.color.

ColorSpace

getInstance

,

getName

,

getNumComponents

,

getType

,

isCS_sRGB

---

#### Methods declared in class java.awt.color. ColorSpace

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ICC_ColorSpace

```java
public ICC_ColorSpace​(
ICC_Profile
profile)
```

Constructs a new ICC_ColorSpace from an ICC_Profile object.

**Parameters:** profile

- the specified ICC_Profile object
**Throws:** IllegalArgumentException

- if profile is inappropriate for
representing a ColorSpace.

============ METHOD DETAIL ==========

- Method Detail

- getProfile

```java
public
ICC_Profile
getProfile()
```

Returns the ICC_Profile for this ICC_ColorSpace.

**Returns:** the ICC_Profile for this ICC_ColorSpace.

- toRGB

```java
public float[] toRGB​(float[] colorvalue)
```

Transforms a color value assumed to be in this ColorSpace
into a value in the default CS_sRGB color space.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of this color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of the CS_sRGB color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

**Specified by:** toRGB

in class

ColorSpace
**Parameters:** colorvalue

- a float array with length of at least the number
of components in this ColorSpace.
**Returns:** a float array of length 3.
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least the number of components in this ColorSpace.

- fromRGB

```java
public float[] fromRGB​(float[] rgbvalue)
```

Transforms a color value assumed to be in the default CS_sRGB
color space into this ColorSpace.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of the CS_sRGB color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of this color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

**Specified by:** fromRGB

in class

ColorSpace
**Parameters:** rgbvalue

- a float array with length of at least 3.
**Returns:** a float array with length equal to the number of
components in this ColorSpace.
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least 3.

- toCIEXYZ

```java
public float[] toCIEXYZ​(float[] colorvalue)
```

Transforms a color value assumed to be in this ColorSpace
into the CS_CIEXYZ conversion color space.

This method transforms color values using relative colorimetry,
as defined by the ICC Specification. This
means that the XYZ values returned by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. This
representation is not the same as the XYZ values that would
be measured from the given color value by a colorimeter.
A further transformation is necessary to compute the XYZ values
that would be measured using current CIE recommended practices.
The paragraphs below explain this in more detail.

The ICC standard uses a device independent color space (DICS) as the
mechanism for converting color from one device to another device. In
this architecture, colors are converted from the source device's color
space to the ICC DICS and then from the ICC DICS to the destination
device's color space. The ICC standard defines device profiles which
contain transforms which will convert between a device's color space
and the ICC DICS. The overall conversion of colors from a source
device to colors of a destination device is done by connecting the
device-to-DICS transform of the profile for the source device to the
DICS-to-device transform of the profile for the destination device.
For this reason, the ICC DICS is commonly referred to as the profile
connection space (PCS). The color space used in the methods
toCIEXYZ and fromCIEXYZ is the CIEXYZ PCS defined by the ICC
Specification. This is also the color space represented by
ColorSpace.CS_CIEXYZ.

The XYZ values of a color are often represented as relative to some
white point, so the actual meaning of the XYZ values cannot be known
without knowing the white point of those values. This is known as
relative colorimetry. The PCS uses a white point of D50, so the XYZ
values of the PCS are relative to D50. For example, white in the PCS
will have the XYZ values of D50, which is defined to be X=.9642,
Y=1.000, and Z=0.8249. This white point is commonly used for graphic
arts applications, but others are often used in other applications.

To quantify the color characteristics of a device such as a printer
or monitor, measurements of XYZ values for particular device colors
are typically made. For purposes of this discussion, the term
device XYZ values is used to mean the XYZ values that would be
measured from device colors using current CIE recommended practices.

Converting between device XYZ values and the PCS XYZ values returned
by this method corresponds to converting between the device's color
space, as represented by CIE colorimetric values, and the PCS. There
are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

**Specified by:** toCIEXYZ

in class

ColorSpace
**Parameters:** colorvalue

- a float array with length of at least the number
of components in this ColorSpace.
**Returns:** a float array of length 3.
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least the number of components in this ColorSpace.

- fromCIEXYZ

```java
public float[] fromCIEXYZ​(float[] colorvalue)
```

Transforms a color value assumed to be in the CS_CIEXYZ conversion
color space into this ColorSpace.

This method transforms color values using relative colorimetry,
as defined by the ICC Specification. This
means that the XYZ argument values taken by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. The color
values returned by this method are not those that would produce
the XYZ value passed to the method when measured by a colorimeter.
If you have XYZ values corresponding to measurements made using
current CIE recommended practices, they must be converted to D50
relative values before being passed to this method.
The paragraphs below explain this in more detail.

The ICC standard uses a device independent color space (DICS) as the
mechanism for converting color from one device to another device. In
this architecture, colors are converted from the source device's color
space to the ICC DICS and then from the ICC DICS to the destination
device's color space. The ICC standard defines device profiles which
contain transforms which will convert between a device's color space
and the ICC DICS. The overall conversion of colors from a source
device to colors of a destination device is done by connecting the
device-to-DICS transform of the profile for the source device to the
DICS-to-device transform of the profile for the destination device.
For this reason, the ICC DICS is commonly referred to as the profile
connection space (PCS). The color space used in the methods
toCIEXYZ and fromCIEXYZ is the CIEXYZ PCS defined by the ICC
Specification. This is also the color space represented by
ColorSpace.CS_CIEXYZ.

The XYZ values of a color are often represented as relative to some
white point, so the actual meaning of the XYZ values cannot be known
without knowing the white point of those values. This is known as
relative colorimetry. The PCS uses a white point of D50, so the XYZ
values of the PCS are relative to D50. For example, white in the PCS
will have the XYZ values of D50, which is defined to be X=.9642,
Y=1.000, and Z=0.8249. This white point is commonly used for graphic
arts applications, but others are often used in other applications.

To quantify the color characteristics of a device such as a printer
or monitor, measurements of XYZ values for particular device colors
are typically made. For purposes of this discussion, the term
device XYZ values is used to mean the XYZ values that would be
measured from device colors using current CIE recommended practices.

Converting between device XYZ values and the PCS XYZ values taken as
arguments by this method corresponds to converting between the device's
color space, as represented by CIE colorimetric values, and the PCS.
There are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

**Specified by:** fromCIEXYZ

in class

ColorSpace
**Parameters:** colorvalue

- a float array with length of at least 3.
**Returns:** a float array with length equal to the number of
components in this ColorSpace.
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least 3.

- getMinValue

```java
public float getMinValue​(int component)
```

Returns the minimum normalized color component value for the
specified component. For TYPE_XYZ spaces, this method returns
minimum values of 0.0 for all components. For TYPE_Lab spaces,
this method returns 0.0 for L and -128.0 for a and b components.
This is consistent with the encoding of the XYZ and Lab Profile
Connection Spaces in the ICC specification. For all other types, this
method returns 0.0 for all components. When using an ICC_ColorSpace
with a profile that requires different minimum component values,
it is necessary to subclass this class and override this method.

**Overrides:** getMinValue

in class

ColorSpace
**Parameters:** component

- The component index.
**Returns:** The minimum normalized component value.
**Throws:** IllegalArgumentException

- if component is less than 0 or
greater than numComponents - 1.
**Since:** 1.4

- getMaxValue

```java
public float getMaxValue​(int component)
```

Returns the maximum normalized color component value for the
specified component. For TYPE_XYZ spaces, this method returns
maximum values of 1.0 + (32767.0 / 32768.0) for all components.
For TYPE_Lab spaces,
this method returns 100.0 for L and 127.0 for a and b components.
This is consistent with the encoding of the XYZ and Lab Profile
Connection Spaces in the ICC specification. For all other types, this
method returns 1.0 for all components. When using an ICC_ColorSpace
with a profile that requires different maximum component values,
it is necessary to subclass this class and override this method.

**Overrides:** getMaxValue

in class

ColorSpace
**Parameters:** component

- The component index.
**Returns:** The maximum normalized component value.
**Throws:** IllegalArgumentException

- if component is less than 0 or
greater than numComponents - 1.
**Since:** 1.4

Constructor Detail

- ICC_ColorSpace

```java
public ICC_ColorSpace​(
ICC_Profile
profile)
```

Constructs a new ICC_ColorSpace from an ICC_Profile object.

**Parameters:** profile

- the specified ICC_Profile object
**Throws:** IllegalArgumentException

- if profile is inappropriate for
representing a ColorSpace.

---

#### Constructor Detail

ICC_ColorSpace

```java
public ICC_ColorSpace​(
ICC_Profile
profile)
```

Constructs a new ICC_ColorSpace from an ICC_Profile object.

**Parameters:** profile

- the specified ICC_Profile object
**Throws:** IllegalArgumentException

- if profile is inappropriate for
representing a ColorSpace.

---

#### ICC_ColorSpace

public ICC_ColorSpace​(

ICC_Profile

profile)

Constructs a new ICC_ColorSpace from an ICC_Profile object.

Method Detail

- getProfile

```java
public
ICC_Profile
getProfile()
```

Returns the ICC_Profile for this ICC_ColorSpace.

**Returns:** the ICC_Profile for this ICC_ColorSpace.

- toRGB

```java
public float[] toRGB​(float[] colorvalue)
```

Transforms a color value assumed to be in this ColorSpace
into a value in the default CS_sRGB color space.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of this color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of the CS_sRGB color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

**Specified by:** toRGB

in class

ColorSpace
**Parameters:** colorvalue

- a float array with length of at least the number
of components in this ColorSpace.
**Returns:** a float array of length 3.
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least the number of components in this ColorSpace.

- fromRGB

```java
public float[] fromRGB​(float[] rgbvalue)
```

Transforms a color value assumed to be in the default CS_sRGB
color space into this ColorSpace.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of the CS_sRGB color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of this color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

**Specified by:** fromRGB

in class

ColorSpace
**Parameters:** rgbvalue

- a float array with length of at least 3.
**Returns:** a float array with length equal to the number of
components in this ColorSpace.
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least 3.

- toCIEXYZ

```java
public float[] toCIEXYZ​(float[] colorvalue)
```

Transforms a color value assumed to be in this ColorSpace
into the CS_CIEXYZ conversion color space.

This method transforms color values using relative colorimetry,
as defined by the ICC Specification. This
means that the XYZ values returned by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. This
representation is not the same as the XYZ values that would
be measured from the given color value by a colorimeter.
A further transformation is necessary to compute the XYZ values
that would be measured using current CIE recommended practices.
The paragraphs below explain this in more detail.

The ICC standard uses a device independent color space (DICS) as the
mechanism for converting color from one device to another device. In
this architecture, colors are converted from the source device's color
space to the ICC DICS and then from the ICC DICS to the destination
device's color space. The ICC standard defines device profiles which
contain transforms which will convert between a device's color space
and the ICC DICS. The overall conversion of colors from a source
device to colors of a destination device is done by connecting the
device-to-DICS transform of the profile for the source device to the
DICS-to-device transform of the profile for the destination device.
For this reason, the ICC DICS is commonly referred to as the profile
connection space (PCS). The color space used in the methods
toCIEXYZ and fromCIEXYZ is the CIEXYZ PCS defined by the ICC
Specification. This is also the color space represented by
ColorSpace.CS_CIEXYZ.

The XYZ values of a color are often represented as relative to some
white point, so the actual meaning of the XYZ values cannot be known
without knowing the white point of those values. This is known as
relative colorimetry. The PCS uses a white point of D50, so the XYZ
values of the PCS are relative to D50. For example, white in the PCS
will have the XYZ values of D50, which is defined to be X=.9642,
Y=1.000, and Z=0.8249. This white point is commonly used for graphic
arts applications, but others are often used in other applications.

To quantify the color characteristics of a device such as a printer
or monitor, measurements of XYZ values for particular device colors
are typically made. For purposes of this discussion, the term
device XYZ values is used to mean the XYZ values that would be
measured from device colors using current CIE recommended practices.

Converting between device XYZ values and the PCS XYZ values returned
by this method corresponds to converting between the device's color
space, as represented by CIE colorimetric values, and the PCS. There
are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

**Specified by:** toCIEXYZ

in class

ColorSpace
**Parameters:** colorvalue

- a float array with length of at least the number
of components in this ColorSpace.
**Returns:** a float array of length 3.
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least the number of components in this ColorSpace.

- fromCIEXYZ

```java
public float[] fromCIEXYZ​(float[] colorvalue)
```

Transforms a color value assumed to be in the CS_CIEXYZ conversion
color space into this ColorSpace.

This method transforms color values using relative colorimetry,
as defined by the ICC Specification. This
means that the XYZ argument values taken by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. The color
values returned by this method are not those that would produce
the XYZ value passed to the method when measured by a colorimeter.
If you have XYZ values corresponding to measurements made using
current CIE recommended practices, they must be converted to D50
relative values before being passed to this method.
The paragraphs below explain this in more detail.

The ICC standard uses a device independent color space (DICS) as the
mechanism for converting color from one device to another device. In
this architecture, colors are converted from the source device's color
space to the ICC DICS and then from the ICC DICS to the destination
device's color space. The ICC standard defines device profiles which
contain transforms which will convert between a device's color space
and the ICC DICS. The overall conversion of colors from a source
device to colors of a destination device is done by connecting the
device-to-DICS transform of the profile for the source device to the
DICS-to-device transform of the profile for the destination device.
For this reason, the ICC DICS is commonly referred to as the profile
connection space (PCS). The color space used in the methods
toCIEXYZ and fromCIEXYZ is the CIEXYZ PCS defined by the ICC
Specification. This is also the color space represented by
ColorSpace.CS_CIEXYZ.

The XYZ values of a color are often represented as relative to some
white point, so the actual meaning of the XYZ values cannot be known
without knowing the white point of those values. This is known as
relative colorimetry. The PCS uses a white point of D50, so the XYZ
values of the PCS are relative to D50. For example, white in the PCS
will have the XYZ values of D50, which is defined to be X=.9642,
Y=1.000, and Z=0.8249. This white point is commonly used for graphic
arts applications, but others are often used in other applications.

To quantify the color characteristics of a device such as a printer
or monitor, measurements of XYZ values for particular device colors
are typically made. For purposes of this discussion, the term
device XYZ values is used to mean the XYZ values that would be
measured from device colors using current CIE recommended practices.

Converting between device XYZ values and the PCS XYZ values taken as
arguments by this method corresponds to converting between the device's
color space, as represented by CIE colorimetric values, and the PCS.
There are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

**Specified by:** fromCIEXYZ

in class

ColorSpace
**Parameters:** colorvalue

- a float array with length of at least 3.
**Returns:** a float array with length equal to the number of
components in this ColorSpace.
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least 3.

- getMinValue

```java
public float getMinValue​(int component)
```

Returns the minimum normalized color component value for the
specified component. For TYPE_XYZ spaces, this method returns
minimum values of 0.0 for all components. For TYPE_Lab spaces,
this method returns 0.0 for L and -128.0 for a and b components.
This is consistent with the encoding of the XYZ and Lab Profile
Connection Spaces in the ICC specification. For all other types, this
method returns 0.0 for all components. When using an ICC_ColorSpace
with a profile that requires different minimum component values,
it is necessary to subclass this class and override this method.

**Overrides:** getMinValue

in class

ColorSpace
**Parameters:** component

- The component index.
**Returns:** The minimum normalized component value.
**Throws:** IllegalArgumentException

- if component is less than 0 or
greater than numComponents - 1.
**Since:** 1.4

- getMaxValue

```java
public float getMaxValue​(int component)
```

Returns the maximum normalized color component value for the
specified component. For TYPE_XYZ spaces, this method returns
maximum values of 1.0 + (32767.0 / 32768.0) for all components.
For TYPE_Lab spaces,
this method returns 100.0 for L and 127.0 for a and b components.
This is consistent with the encoding of the XYZ and Lab Profile
Connection Spaces in the ICC specification. For all other types, this
method returns 1.0 for all components. When using an ICC_ColorSpace
with a profile that requires different maximum component values,
it is necessary to subclass this class and override this method.

**Overrides:** getMaxValue

in class

ColorSpace
**Parameters:** component

- The component index.
**Returns:** The maximum normalized component value.
**Throws:** IllegalArgumentException

- if component is less than 0 or
greater than numComponents - 1.
**Since:** 1.4

---

#### Method Detail

getProfile

```java
public
ICC_Profile
getProfile()
```

Returns the ICC_Profile for this ICC_ColorSpace.

**Returns:** the ICC_Profile for this ICC_ColorSpace.

---

#### getProfile

public

ICC_Profile

getProfile()

Returns the ICC_Profile for this ICC_ColorSpace.

toRGB

```java
public float[] toRGB​(float[] colorvalue)
```

Transforms a color value assumed to be in this ColorSpace
into a value in the default CS_sRGB color space.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of this color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of the CS_sRGB color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

**Specified by:** toRGB

in class

ColorSpace
**Parameters:** colorvalue

- a float array with length of at least the number
of components in this ColorSpace.
**Returns:** a float array of length 3.
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least the number of components in this ColorSpace.

---

#### toRGB

public float[] toRGB​(float[] colorvalue)

Transforms a color value assumed to be in this ColorSpace
into a value in the default CS_sRGB color space.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of this color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of the CS_sRGB color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of this color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of the CS_sRGB color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

fromRGB

```java
public float[] fromRGB​(float[] rgbvalue)
```

Transforms a color value assumed to be in the default CS_sRGB
color space into this ColorSpace.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of the CS_sRGB color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of this color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

**Specified by:** fromRGB

in class

ColorSpace
**Parameters:** rgbvalue

- a float array with length of at least 3.
**Returns:** a float array with length equal to the number of
components in this ColorSpace.
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least 3.

---

#### fromRGB

public float[] fromRGB​(float[] rgbvalue)

Transforms a color value assumed to be in the default CS_sRGB
color space into this ColorSpace.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of the CS_sRGB color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of this color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of the CS_sRGB color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of this color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

toCIEXYZ

```java
public float[] toCIEXYZ​(float[] colorvalue)
```

Transforms a color value assumed to be in this ColorSpace
into the CS_CIEXYZ conversion color space.

This method transforms color values using relative colorimetry,
as defined by the ICC Specification. This
means that the XYZ values returned by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. This
representation is not the same as the XYZ values that would
be measured from the given color value by a colorimeter.
A further transformation is necessary to compute the XYZ values
that would be measured using current CIE recommended practices.
The paragraphs below explain this in more detail.

The ICC standard uses a device independent color space (DICS) as the
mechanism for converting color from one device to another device. In
this architecture, colors are converted from the source device's color
space to the ICC DICS and then from the ICC DICS to the destination
device's color space. The ICC standard defines device profiles which
contain transforms which will convert between a device's color space
and the ICC DICS. The overall conversion of colors from a source
device to colors of a destination device is done by connecting the
device-to-DICS transform of the profile for the source device to the
DICS-to-device transform of the profile for the destination device.
For this reason, the ICC DICS is commonly referred to as the profile
connection space (PCS). The color space used in the methods
toCIEXYZ and fromCIEXYZ is the CIEXYZ PCS defined by the ICC
Specification. This is also the color space represented by
ColorSpace.CS_CIEXYZ.

The XYZ values of a color are often represented as relative to some
white point, so the actual meaning of the XYZ values cannot be known
without knowing the white point of those values. This is known as
relative colorimetry. The PCS uses a white point of D50, so the XYZ
values of the PCS are relative to D50. For example, white in the PCS
will have the XYZ values of D50, which is defined to be X=.9642,
Y=1.000, and Z=0.8249. This white point is commonly used for graphic
arts applications, but others are often used in other applications.

To quantify the color characteristics of a device such as a printer
or monitor, measurements of XYZ values for particular device colors
are typically made. For purposes of this discussion, the term
device XYZ values is used to mean the XYZ values that would be
measured from device colors using current CIE recommended practices.

Converting between device XYZ values and the PCS XYZ values returned
by this method corresponds to converting between the device's color
space, as represented by CIE colorimetric values, and the PCS. There
are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

**Specified by:** toCIEXYZ

in class

ColorSpace
**Parameters:** colorvalue

- a float array with length of at least the number
of components in this ColorSpace.
**Returns:** a float array of length 3.
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least the number of components in this ColorSpace.

---

#### toCIEXYZ

public float[] toCIEXYZ​(float[] colorvalue)

Transforms a color value assumed to be in this ColorSpace
into the CS_CIEXYZ conversion color space.

This method transforms color values using relative colorimetry,
as defined by the ICC Specification. This
means that the XYZ values returned by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. This
representation is not the same as the XYZ values that would
be measured from the given color value by a colorimeter.
A further transformation is necessary to compute the XYZ values
that would be measured using current CIE recommended practices.
The paragraphs below explain this in more detail.

The ICC standard uses a device independent color space (DICS) as the
mechanism for converting color from one device to another device. In
this architecture, colors are converted from the source device's color
space to the ICC DICS and then from the ICC DICS to the destination
device's color space. The ICC standard defines device profiles which
contain transforms which will convert between a device's color space
and the ICC DICS. The overall conversion of colors from a source
device to colors of a destination device is done by connecting the
device-to-DICS transform of the profile for the source device to the
DICS-to-device transform of the profile for the destination device.
For this reason, the ICC DICS is commonly referred to as the profile
connection space (PCS). The color space used in the methods
toCIEXYZ and fromCIEXYZ is the CIEXYZ PCS defined by the ICC
Specification. This is also the color space represented by
ColorSpace.CS_CIEXYZ.

The XYZ values of a color are often represented as relative to some
white point, so the actual meaning of the XYZ values cannot be known
without knowing the white point of those values. This is known as
relative colorimetry. The PCS uses a white point of D50, so the XYZ
values of the PCS are relative to D50. For example, white in the PCS
will have the XYZ values of D50, which is defined to be X=.9642,
Y=1.000, and Z=0.8249. This white point is commonly used for graphic
arts applications, but others are often used in other applications.

To quantify the color characteristics of a device such as a printer
or monitor, measurements of XYZ values for particular device colors
are typically made. For purposes of this discussion, the term
device XYZ values is used to mean the XYZ values that would be
measured from device colors using current CIE recommended practices.

Converting between device XYZ values and the PCS XYZ values returned
by this method corresponds to converting between the device's color
space, as represented by CIE colorimetric values, and the PCS. There
are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

This method transforms color values using relative colorimetry,
as defined by the ICC Specification. This
means that the XYZ values returned by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. This
representation is not the same as the XYZ values that would
be measured from the given color value by a colorimeter.
A further transformation is necessary to compute the XYZ values
that would be measured using current CIE recommended practices.
The paragraphs below explain this in more detail.

The ICC standard uses a device independent color space (DICS) as the
mechanism for converting color from one device to another device. In
this architecture, colors are converted from the source device's color
space to the ICC DICS and then from the ICC DICS to the destination
device's color space. The ICC standard defines device profiles which
contain transforms which will convert between a device's color space
and the ICC DICS. The overall conversion of colors from a source
device to colors of a destination device is done by connecting the
device-to-DICS transform of the profile for the source device to the
DICS-to-device transform of the profile for the destination device.
For this reason, the ICC DICS is commonly referred to as the profile
connection space (PCS). The color space used in the methods
toCIEXYZ and fromCIEXYZ is the CIEXYZ PCS defined by the ICC
Specification. This is also the color space represented by
ColorSpace.CS_CIEXYZ.

The XYZ values of a color are often represented as relative to some
white point, so the actual meaning of the XYZ values cannot be known
without knowing the white point of those values. This is known as
relative colorimetry. The PCS uses a white point of D50, so the XYZ
values of the PCS are relative to D50. For example, white in the PCS
will have the XYZ values of D50, which is defined to be X=.9642,
Y=1.000, and Z=0.8249. This white point is commonly used for graphic
arts applications, but others are often used in other applications.

To quantify the color characteristics of a device such as a printer
or monitor, measurements of XYZ values for particular device colors
are typically made. For purposes of this discussion, the term
device XYZ values is used to mean the XYZ values that would be
measured from device colors using current CIE recommended practices.

Converting between device XYZ values and the PCS XYZ values returned
by this method corresponds to converting between the device's color
space, as represented by CIE colorimetric values, and the PCS. There
are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

The ICC standard uses a device independent color space (DICS) as the
mechanism for converting color from one device to another device. In
this architecture, colors are converted from the source device's color
space to the ICC DICS and then from the ICC DICS to the destination
device's color space. The ICC standard defines device profiles which
contain transforms which will convert between a device's color space
and the ICC DICS. The overall conversion of colors from a source
device to colors of a destination device is done by connecting the
device-to-DICS transform of the profile for the source device to the
DICS-to-device transform of the profile for the destination device.
For this reason, the ICC DICS is commonly referred to as the profile
connection space (PCS). The color space used in the methods
toCIEXYZ and fromCIEXYZ is the CIEXYZ PCS defined by the ICC
Specification. This is also the color space represented by
ColorSpace.CS_CIEXYZ.

The XYZ values of a color are often represented as relative to some
white point, so the actual meaning of the XYZ values cannot be known
without knowing the white point of those values. This is known as
relative colorimetry. The PCS uses a white point of D50, so the XYZ
values of the PCS are relative to D50. For example, white in the PCS
will have the XYZ values of D50, which is defined to be X=.9642,
Y=1.000, and Z=0.8249. This white point is commonly used for graphic
arts applications, but others are often used in other applications.

To quantify the color characteristics of a device such as a printer
or monitor, measurements of XYZ values for particular device colors
are typically made. For purposes of this discussion, the term
device XYZ values is used to mean the XYZ values that would be
measured from device colors using current CIE recommended practices.

Converting between device XYZ values and the PCS XYZ values returned
by this method corresponds to converting between the device's color
space, as represented by CIE colorimetric values, and the PCS. There
are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

The XYZ values of a color are often represented as relative to some
white point, so the actual meaning of the XYZ values cannot be known
without knowing the white point of those values. This is known as
relative colorimetry. The PCS uses a white point of D50, so the XYZ
values of the PCS are relative to D50. For example, white in the PCS
will have the XYZ values of D50, which is defined to be X=.9642,
Y=1.000, and Z=0.8249. This white point is commonly used for graphic
arts applications, but others are often used in other applications.

To quantify the color characteristics of a device such as a printer
or monitor, measurements of XYZ values for particular device colors
are typically made. For purposes of this discussion, the term
device XYZ values is used to mean the XYZ values that would be
measured from device colors using current CIE recommended practices.

Converting between device XYZ values and the PCS XYZ values returned
by this method corresponds to converting between the device's color
space, as represented by CIE colorimetric values, and the PCS. There
are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

To quantify the color characteristics of a device such as a printer
or monitor, measurements of XYZ values for particular device colors
are typically made. For purposes of this discussion, the term
device XYZ values is used to mean the XYZ values that would be
measured from device colors using current CIE recommended practices.

Converting between device XYZ values and the PCS XYZ values returned
by this method corresponds to converting between the device's color
space, as represented by CIE colorimetric values, and the PCS. There
are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

Converting between device XYZ values and the PCS XYZ values returned
by this method corresponds to converting between the device's color
space, as represented by CIE colorimetric values, and the PCS. There
are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

fromCIEXYZ

```java
public float[] fromCIEXYZ​(float[] colorvalue)
```

Transforms a color value assumed to be in the CS_CIEXYZ conversion
color space into this ColorSpace.

This method transforms color values using relative colorimetry,
as defined by the ICC Specification. This
means that the XYZ argument values taken by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. The color
values returned by this method are not those that would produce
the XYZ value passed to the method when measured by a colorimeter.
If you have XYZ values corresponding to measurements made using
current CIE recommended practices, they must be converted to D50
relative values before being passed to this method.
The paragraphs below explain this in more detail.

The ICC standard uses a device independent color space (DICS) as the
mechanism for converting color from one device to another device. In
this architecture, colors are converted from the source device's color
space to the ICC DICS and then from the ICC DICS to the destination
device's color space. The ICC standard defines device profiles which
contain transforms which will convert between a device's color space
and the ICC DICS. The overall conversion of colors from a source
device to colors of a destination device is done by connecting the
device-to-DICS transform of the profile for the source device to the
DICS-to-device transform of the profile for the destination device.
For this reason, the ICC DICS is commonly referred to as the profile
connection space (PCS). The color space used in the methods
toCIEXYZ and fromCIEXYZ is the CIEXYZ PCS defined by the ICC
Specification. This is also the color space represented by
ColorSpace.CS_CIEXYZ.

The XYZ values of a color are often represented as relative to some
white point, so the actual meaning of the XYZ values cannot be known
without knowing the white point of those values. This is known as
relative colorimetry. The PCS uses a white point of D50, so the XYZ
values of the PCS are relative to D50. For example, white in the PCS
will have the XYZ values of D50, which is defined to be X=.9642,
Y=1.000, and Z=0.8249. This white point is commonly used for graphic
arts applications, but others are often used in other applications.

To quantify the color characteristics of a device such as a printer
or monitor, measurements of XYZ values for particular device colors
are typically made. For purposes of this discussion, the term
device XYZ values is used to mean the XYZ values that would be
measured from device colors using current CIE recommended practices.

Converting between device XYZ values and the PCS XYZ values taken as
arguments by this method corresponds to converting between the device's
color space, as represented by CIE colorimetric values, and the PCS.
There are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

**Specified by:** fromCIEXYZ

in class

ColorSpace
**Parameters:** colorvalue

- a float array with length of at least 3.
**Returns:** a float array with length equal to the number of
components in this ColorSpace.
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least 3.

---

#### fromCIEXYZ

public float[] fromCIEXYZ​(float[] colorvalue)

Transforms a color value assumed to be in the CS_CIEXYZ conversion
color space into this ColorSpace.

This method transforms color values using relative colorimetry,
as defined by the ICC Specification. This
means that the XYZ argument values taken by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. The color
values returned by this method are not those that would produce
the XYZ value passed to the method when measured by a colorimeter.
If you have XYZ values corresponding to measurements made using
current CIE recommended practices, they must be converted to D50
relative values before being passed to this method.
The paragraphs below explain this in more detail.

The ICC standard uses a device independent color space (DICS) as the
mechanism for converting color from one device to another device. In
this architecture, colors are converted from the source device's color
space to the ICC DICS and then from the ICC DICS to the destination
device's color space. The ICC standard defines device profiles which
contain transforms which will convert between a device's color space
and the ICC DICS. The overall conversion of colors from a source
device to colors of a destination device is done by connecting the
device-to-DICS transform of the profile for the source device to the
DICS-to-device transform of the profile for the destination device.
For this reason, the ICC DICS is commonly referred to as the profile
connection space (PCS). The color space used in the methods
toCIEXYZ and fromCIEXYZ is the CIEXYZ PCS defined by the ICC
Specification. This is also the color space represented by
ColorSpace.CS_CIEXYZ.

The XYZ values of a color are often represented as relative to some
white point, so the actual meaning of the XYZ values cannot be known
without knowing the white point of those values. This is known as
relative colorimetry. The PCS uses a white point of D50, so the XYZ
values of the PCS are relative to D50. For example, white in the PCS
will have the XYZ values of D50, which is defined to be X=.9642,
Y=1.000, and Z=0.8249. This white point is commonly used for graphic
arts applications, but others are often used in other applications.

To quantify the color characteristics of a device such as a printer
or monitor, measurements of XYZ values for particular device colors
are typically made. For purposes of this discussion, the term
device XYZ values is used to mean the XYZ values that would be
measured from device colors using current CIE recommended practices.

Converting between device XYZ values and the PCS XYZ values taken as
arguments by this method corresponds to converting between the device's
color space, as represented by CIE colorimetric values, and the PCS.
There are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

This method transforms color values using relative colorimetry,
as defined by the ICC Specification. This
means that the XYZ argument values taken by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. The color
values returned by this method are not those that would produce
the XYZ value passed to the method when measured by a colorimeter.
If you have XYZ values corresponding to measurements made using
current CIE recommended practices, they must be converted to D50
relative values before being passed to this method.
The paragraphs below explain this in more detail.

The ICC standard uses a device independent color space (DICS) as the
mechanism for converting color from one device to another device. In
this architecture, colors are converted from the source device's color
space to the ICC DICS and then from the ICC DICS to the destination
device's color space. The ICC standard defines device profiles which
contain transforms which will convert between a device's color space
and the ICC DICS. The overall conversion of colors from a source
device to colors of a destination device is done by connecting the
device-to-DICS transform of the profile for the source device to the
DICS-to-device transform of the profile for the destination device.
For this reason, the ICC DICS is commonly referred to as the profile
connection space (PCS). The color space used in the methods
toCIEXYZ and fromCIEXYZ is the CIEXYZ PCS defined by the ICC
Specification. This is also the color space represented by
ColorSpace.CS_CIEXYZ.

The XYZ values of a color are often represented as relative to some
white point, so the actual meaning of the XYZ values cannot be known
without knowing the white point of those values. This is known as
relative colorimetry. The PCS uses a white point of D50, so the XYZ
values of the PCS are relative to D50. For example, white in the PCS
will have the XYZ values of D50, which is defined to be X=.9642,
Y=1.000, and Z=0.8249. This white point is commonly used for graphic
arts applications, but others are often used in other applications.

To quantify the color characteristics of a device such as a printer
or monitor, measurements of XYZ values for particular device colors
are typically made. For purposes of this discussion, the term
device XYZ values is used to mean the XYZ values that would be
measured from device colors using current CIE recommended practices.

Converting between device XYZ values and the PCS XYZ values taken as
arguments by this method corresponds to converting between the device's
color space, as represented by CIE colorimetric values, and the PCS.
There are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

The ICC standard uses a device independent color space (DICS) as the
mechanism for converting color from one device to another device. In
this architecture, colors are converted from the source device's color
space to the ICC DICS and then from the ICC DICS to the destination
device's color space. The ICC standard defines device profiles which
contain transforms which will convert between a device's color space
and the ICC DICS. The overall conversion of colors from a source
device to colors of a destination device is done by connecting the
device-to-DICS transform of the profile for the source device to the
DICS-to-device transform of the profile for the destination device.
For this reason, the ICC DICS is commonly referred to as the profile
connection space (PCS). The color space used in the methods
toCIEXYZ and fromCIEXYZ is the CIEXYZ PCS defined by the ICC
Specification. This is also the color space represented by
ColorSpace.CS_CIEXYZ.

The XYZ values of a color are often represented as relative to some
white point, so the actual meaning of the XYZ values cannot be known
without knowing the white point of those values. This is known as
relative colorimetry. The PCS uses a white point of D50, so the XYZ
values of the PCS are relative to D50. For example, white in the PCS
will have the XYZ values of D50, which is defined to be X=.9642,
Y=1.000, and Z=0.8249. This white point is commonly used for graphic
arts applications, but others are often used in other applications.

To quantify the color characteristics of a device such as a printer
or monitor, measurements of XYZ values for particular device colors
are typically made. For purposes of this discussion, the term
device XYZ values is used to mean the XYZ values that would be
measured from device colors using current CIE recommended practices.

Converting between device XYZ values and the PCS XYZ values taken as
arguments by this method corresponds to converting between the device's
color space, as represented by CIE colorimetric values, and the PCS.
There are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

The XYZ values of a color are often represented as relative to some
white point, so the actual meaning of the XYZ values cannot be known
without knowing the white point of those values. This is known as
relative colorimetry. The PCS uses a white point of D50, so the XYZ
values of the PCS are relative to D50. For example, white in the PCS
will have the XYZ values of D50, which is defined to be X=.9642,
Y=1.000, and Z=0.8249. This white point is commonly used for graphic
arts applications, but others are often used in other applications.

To quantify the color characteristics of a device such as a printer
or monitor, measurements of XYZ values for particular device colors
are typically made. For purposes of this discussion, the term
device XYZ values is used to mean the XYZ values that would be
measured from device colors using current CIE recommended practices.

Converting between device XYZ values and the PCS XYZ values taken as
arguments by this method corresponds to converting between the device's
color space, as represented by CIE colorimetric values, and the PCS.
There are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

To quantify the color characteristics of a device such as a printer
or monitor, measurements of XYZ values for particular device colors
are typically made. For purposes of this discussion, the term
device XYZ values is used to mean the XYZ values that would be
measured from device colors using current CIE recommended practices.

Converting between device XYZ values and the PCS XYZ values taken as
arguments by this method corresponds to converting between the device's
color space, as represented by CIE colorimetric values, and the PCS.
There are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

Converting between device XYZ values and the PCS XYZ values taken as
arguments by this method corresponds to converting between the device's
color space, as represented by CIE colorimetric values, and the PCS.
There are many factors involved in this process, some of which are quite
subtle. The most important, however, is the adjustment made to account
for differences between the device's white point and the white point of
the PCS. There are many techniques for doing this and it is the
subject of much current research and controversy. Some commonly used
methods are XYZ scaling, the von Kries transform, and the Bradford
transform. The proper method to use depends upon each particular
application.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

The simplest method is XYZ scaling. In this method each device XYZ
value is converted to a PCS XYZ value by multiplying it by the ratio
of the PCS white point (D50) to the device white point.

```java
Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)
```

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

Xd, Yd, Zd are the device XYZ values
Xdw, Ydw, Zdw are the device XYZ white point values
Xp, Yp, Zp are the PCS XYZ values
Xd50, Yd50, Zd50 are the PCS XYZ white point values

Xp = Xd * (Xd50 / Xdw)
Yp = Yd * (Yd50 / Ydw)
Zp = Zd * (Zd50 / Zdw)

Conversion from the PCS to the device would be done by inverting these
equations:

```java
Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)
```

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

Xd = Xp * (Xdw / Xd50)
Yd = Yp * (Ydw / Yd50)
Zd = Zp * (Zdw / Zd50)

Note that the media white point tag in an ICC profile is not the same
as the device white point. The media white point tag is expressed in
PCS values and is used to represent the difference between the XYZ of
device illuminant and the XYZ of the device media when measured under
that illuminant. The device white point is expressed as the device
XYZ values corresponding to white displayed on the device. For
example, displaying the RGB color (1.0, 1.0, 1.0) on an sRGB device
will result in a measured device XYZ value of D65. This will not
be the same as the media white point tag XYZ value in the ICC
profile for an sRGB device.

getMinValue

```java
public float getMinValue​(int component)
```

Returns the minimum normalized color component value for the
specified component. For TYPE_XYZ spaces, this method returns
minimum values of 0.0 for all components. For TYPE_Lab spaces,
this method returns 0.0 for L and -128.0 for a and b components.
This is consistent with the encoding of the XYZ and Lab Profile
Connection Spaces in the ICC specification. For all other types, this
method returns 0.0 for all components. When using an ICC_ColorSpace
with a profile that requires different minimum component values,
it is necessary to subclass this class and override this method.

**Overrides:** getMinValue

in class

ColorSpace
**Parameters:** component

- The component index.
**Returns:** The minimum normalized component value.
**Throws:** IllegalArgumentException

- if component is less than 0 or
greater than numComponents - 1.
**Since:** 1.4

---

#### getMinValue

public float getMinValue​(int component)

Returns the minimum normalized color component value for the
specified component. For TYPE_XYZ spaces, this method returns
minimum values of 0.0 for all components. For TYPE_Lab spaces,
this method returns 0.0 for L and -128.0 for a and b components.
This is consistent with the encoding of the XYZ and Lab Profile
Connection Spaces in the ICC specification. For all other types, this
method returns 0.0 for all components. When using an ICC_ColorSpace
with a profile that requires different minimum component values,
it is necessary to subclass this class and override this method.

getMaxValue

```java
public float getMaxValue​(int component)
```

Returns the maximum normalized color component value for the
specified component. For TYPE_XYZ spaces, this method returns
maximum values of 1.0 + (32767.0 / 32768.0) for all components.
For TYPE_Lab spaces,
this method returns 100.0 for L and 127.0 for a and b components.
This is consistent with the encoding of the XYZ and Lab Profile
Connection Spaces in the ICC specification. For all other types, this
method returns 1.0 for all components. When using an ICC_ColorSpace
with a profile that requires different maximum component values,
it is necessary to subclass this class and override this method.

**Overrides:** getMaxValue

in class

ColorSpace
**Parameters:** component

- The component index.
**Returns:** The maximum normalized component value.
**Throws:** IllegalArgumentException

- if component is less than 0 or
greater than numComponents - 1.
**Since:** 1.4

---

#### getMaxValue

public float getMaxValue​(int component)

Returns the maximum normalized color component value for the
specified component. For TYPE_XYZ spaces, this method returns
maximum values of 1.0 + (32767.0 / 32768.0) for all components.
For TYPE_Lab spaces,
this method returns 100.0 for L and 127.0 for a and b components.
This is consistent with the encoding of the XYZ and Lab Profile
Connection Spaces in the ICC specification. For all other types, this
method returns 1.0 for all components. When using an ICC_ColorSpace
with a profile that requires different maximum component values,
it is necessary to subclass this class and override this method.

---

