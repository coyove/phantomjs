a = [a.strip() for a in """
/lib/aarch64-linux-gnu/libQt5Network.so.5
/lib/aarch64-linux-gnu/libQt5Widgets.so.5
/lib/aarch64-linux-gnu/libQt5Gui.so.5
/lib/aarch64-linux-gnu/libQt5Core.so.5
/lib/aarch64-linux-gnu/libstdc++.so.6
/lib/aarch64-linux-gnu/libm.so.6
/lib/aarch64-linux-gnu/libgcc_s.so.1
/lib/aarch64-linux-gnu/libc.so.6
/lib/aarch64-linux-gnu/libz.so.1
/lib/aarch64-linux-gnu/libgssapi_krb5.so.2
/lib/aarch64-linux-gnu/libicudata.so.70
/lib/aarch64-linux-gnu/libicui18n.so.70
/lib/aarch64-linux-gnu/libicuuc.so.70
/lib/aarch64-linux-gnu/libQt5Positioning.so.5
/lib/aarch64-linux-gnu/libxml2.so.2
/lib/aarch64-linux-gnu/libsqlite3.so.0
/lib/aarch64-linux-gnu/libxslt.so.1
/lib/aarch64-linux-gnu/libwoff2dec.so.1.0.2
/lib/aarch64-linux-gnu/libpng16.so.16
/lib/aarch64-linux-gnu/libwebpdemux.so.2
/lib/aarch64-linux-gnu/libwebp.so.7
/lib/aarch64-linux-gnu/libharfbuzz.so.0
/lib/aarch64-linux-gnu/libharfbuzz-icu.so.0
/lib/aarch64-linux-gnu/libfreetype.so.6
/lib/aarch64-linux-gnu/libhyphen.so.0
/lib/aarch64-linux-gnu/libtasn1.so.6
/lib/aarch64-linux-gnu/libgcrypt.so.20
/lib/aarch64-linux-gnu/libgpg-error.so.0
/lib/aarch64-linux-gnu/libGL.so.1
/lib/aarch64-linux-gnu/libmd4c.so.0
/lib/aarch64-linux-gnu/libdouble-conversion.so.3
/lib/aarch64-linux-gnu/libpcre2-16.so.0
/lib/aarch64-linux-gnu/libzstd.so.1
/lib/aarch64-linux-gnu/libglib-2.0.so.0
/lib/aarch64-linux-gnu/libkrb5.so.3
/lib/aarch64-linux-gnu/libk5crypto.so.3
/lib/aarch64-linux-gnu/libcom_err.so.2
/lib/aarch64-linux-gnu/libkrb5support.so.0
/lib/aarch64-linux-gnu/liblzma.so.5
/lib/aarch64-linux-gnu/libwoff2common.so.1.0.2
/lib/aarch64-linux-gnu/libbrotlidec.so.1
/lib/aarch64-linux-gnu/libgraphite2.so.3
/lib/aarch64-linux-gnu/libGLdispatch.so.0
/lib/aarch64-linux-gnu/libGLX.so.0
/lib/aarch64-linux-gnu/libpcre.so.3
/lib/aarch64-linux-gnu/libkeyutils.so.1
/lib/aarch64-linux-gnu/libresolv.so.2
/lib/aarch64-linux-gnu/libbrotlicommon.so.1
/lib/aarch64-linux-gnu/libX11.so.6
/lib/aarch64-linux-gnu/libxcb.so.1
/lib/aarch64-linux-gnu/libXau.so.6
/lib/aarch64-linux-gnu/libXdmcp.so.6
/lib/aarch64-linux-gnu/libbsd.so.0
/lib/aarch64-linux-gnu/libmd.so.0
/lib/aarch64-linux-gnu/libssl.so
/lib/aarch64-linux-gnu/libcrypto.so
/lib/aarch64-linux-gnu/libfontconfig.so.1
/lib/aarch64-linux-gnu/libexpat.so.1
/lib/aarch64-linux-gnu/libuuid.so.1
/lib/aarch64-linux-gnu/libjpeg.so.8
/lib/aarch64-linux-gnu/libQt5Svg.so.5
/lib/aarch64-linux-gnu/libQt5DBus.so.5
/lib/aarch64-linux-gnu/liblz4.so.1
/lib/aarch64-linux-gnu/libdbus-1.so.3
/lib/aarch64-linux-gnu/libcap.so.2
    """.split('\n') if a.strip()]

import re, os.path, shutil
from pathlib import Path

os.makedirs('lib', exist_ok=True)

for p in a:
    r = str(Path(p).resolve())
    dd = os.path.dirname(p)[1:]
    fn = os.path.basename(p)
    #print(p, dd, r)
    shutil.copyfile(r, 'lib/' + fn)

