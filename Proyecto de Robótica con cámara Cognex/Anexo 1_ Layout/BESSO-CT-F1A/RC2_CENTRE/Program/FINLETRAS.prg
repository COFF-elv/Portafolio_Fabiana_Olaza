1 'Configuracón inicial / encendido del robot
2     HOpen 1
3     Ovrd 50
4     Tool 1
5     Base 0
6 '
7     Servo On
8     Wait M_Svo = 1
9 '
10     '
11     Mov P_Safe
12     Dly 0.5
13 '
14 'Variable piezas nulas
15     Dim Pnula(3)
16     Dim Pblan(3)
17 '
18 'Repeticion de letras en palabra
19     Dim Posll(2)
20     a = 1
21 '
22 'Contador de letras por palabra
23 Mtreball = 1
24 Mdel = 1
25 Mescola = 1
26 '
27 'Contador de filas
28 Mfiles = 1
29 '
30 '"memoria" lletres
31   'treball
32     TrebT=0
33     TrebR=0
34     TrebE=0
35     TrebB=0
36     TrebA=0
37     TrebL=0
38   'del
39     delD=0
40     delE=0
41     delL=0
42   'Escola
43     escolaE=0
44     escolaS=0
45     escolaC=0
46     escolaO=0
47     escolaL=0
48     escolaA=0
49 'Contador linea actual
50 'Establecer comunicación con la camara:
51     'Abrir puerto de comunicaciones con la camara en COM2
52 '
53         If M_NvOpen(1) <> 1 Then
54             NVOpen "COM2:" As #1
55         EndIf
56 '
57     'Esperar a que la comunicacion este abierta
58 '
59         Wait M_NvOpen(1) = 1
60 '
61     'Seleccionar programa de la cognex
62 '
63         CProgCAM$ = "PaternD"
64 '
65     'Cargar programa a la camara
66 '
67         NVLoad #1,CProgCAM$
68 '
69 'Bucle de Trabajo
70 *LOOP
71 '
72     'Sumatorio contador de filas
73     If (Mtreb = 7 Or Mdel= 7 Or Mescola = 7) Then Mfiles = Mfiles + 1
74     If Mfiles = 2 Then Mtreb = 0
75     If Mfiles = 3 Then Mdel = 0
76     '
77     Dly 0.5
78     '
79     'Trigger camara
80     '
81     NVRun #1, CProgCAM$
82     '
83     'Leer datos enviados por la camara
84     '
85     EBRead #1,,MNUM,POSLET,C1$
86     '
87     'Condiciones para el seguimiento del programa ante el caso de no administrar mas piezas
88     If (MNUM = 0 And Mfiles = 4) Then GoTo *Casa
89     If (MNUM = 0 And Mfiles < 4) Then GoTo *LOOP
90     '
91     GoTo *ColocacionNOREP
92 'Decision de colocación de letras
93 *ColocacionNOREP
94     'Treball
95     If ((C1$ = "LetraT" Or C1$ = "LetraR" Or C1$ = "LetraE" Or C1$ = "LetraB" Or C1$ = "LetraA" Or C1$ = "LetraL") And Mfiles = 1) Then GoTo *Treball
96     'Del
97     If ((C1$ = "LetraD" Or C1$ = "LetraE" Or C1$ = "LetraL" ) And Mfiles = 2)Then GoTo *Del
98     'Escola
99     If ((C1$ = "LetraE" Or C1$ = "LetraS" Or C1$ = "LetraC" Or C1$ = "LetraO" Or C1$ = "LetraL" Or C1$ = "LetraA" )And Mfiles = 3) Then
100         GoTo *Escola
101     Else
102         GoTo *Negativa
103     EndIf
104 'Colocación de letras que forman "Treball"
105 *Treball
106     If ((TrebT = 1 And C1$= "LetraT") Or (TrebR = 1 And C1$= "LetraR") Or (TrebE = 1 And C1$= "LetraE") Or (TrebB = 1 And C1$= "LetraB") Or (TrebA = 1 And C1$= "LetraA") Or (TrebL = 3 And C1$= "LetraL")) Then GoTo *Negativa
107         GoSub *Pick
108         Select C1$
109         Case "LetraT"
110         Mov Pcol1, -50
111         Dly 0.5
112         Mvs Pcol1
113         Dly 1
114         HOpen 1
115         Dly 0.5
116         Mvs, -50
117         Mtreb = Mtreb + 1
118         TrebT = TrebT + 1
119         Break
120         '
121         Case "LetraR"
122         Mov Pcol2, -50
123         Dly 0.5
124         Mvs Pcol2
125         Dly 1
126         HOpen 1
127         Dly 0.5
128         Mvs, -50
129         Mtreb = Mtreb + 1
130         TrebR = TrebR + 1
131         Break
132         '
133         Case "LetraE"
134         Mov Pcol3, -50
135         Dly 0.5
136         Mvs Pcol3
137         Dly 1
138         HOpen 1
139         Dly 0.5
140         Mvs, -50
141         Mtreb = Mtreb + 1
142         TrebE = TrebE + 1
143         Break
144         '
145         Case "LetraB"
146         Mov Pcol4, -50
147         Dly 0.5
148         Mvs Pcol4
149         Dly 1
150         HOpen 1
151         Dly 0.5
152         Mvs, -50
153         Mtreb = Mtreb + 1
154         TrebB = TrebB + 1
155         Dly 0.5
156         Break
157         '
158         Case "LetraA"
159         Mov Pcol5, -50
160         Dly 0.5
161         Mvs Pcol5
162         Dly 1
163         HOpen 1
164         Dly 0.5
165         Mvs, -50
166         Dly 0.5
167         Mtreb = Mtreb + 1
168         TrebA = TrebA + 1
169         Break
170         '
171         Case "LetraL"
172         Mov Posll(a), -30
173         Dly 0.5
174         Mvs Posll(a)
175         Dly 1
176         HOpen 1
177         Dly 0.5
178         Dly 0.5
179         a = a + 1
180         Mtreb = Mtreb + 1
181         TrebL = TrebL + 1
182         Break
183         End Select
184         Mov P_Safe
185         GoTo *Relectura
186 'Colocación de letras que forman "del"
187 *Del
188     If (delD = 1 And C1$= "LetraD" Or delE = 1 And C1$= "LetraE" Or delL = 1 And C1$= "LetraL") Then GoTo *Negativa
189         GoSub *Pick
190         Select C1$
191         Case "LetraD"
192         Mov Pcol1, -50
193         Dly 0.5
194         Mvs Pcol1
195         Dly 1
196         HOpen 1
197         Dly 0.5
198         Mvs, -50
199         Dly 0.5
200         Mdel = Mdel + 1
201         delD = delD + 1
202         Break
203         '
204         Case "LetraE"
205         Mov Pcol2, -50
206         Dly 0.5
207         Mvs Pcol2
208         Dly 1
209         HOpen 1
210         Dly 0.5
211         Mvs, -50
212         Dly 0.5
213         Mdel = Mdel + 1
214         delE = delE + 1
215         Break
216         '
217         Case "LetraL"
218         Mov Pcol3, -50
219         Dly 0.5
220         Mvs Pcol3
221         Dly 1
222         HOpen 1
223         Dly 0.5
224         Mvs, -50
225         Dly 0.5
226         Mdel = Mdel + 1
227         delL = delL + 1
228         Break
229         End Select
230         Mov P_Safe
231         'Colocación de piezas vacias
232         If Mdel = 4 Then GoSub *ColPNul
233         '
234         GoTo *Relectura
235         '
236 'Colocación de letras que forman "Escola"
237 *Escola
238     If (escolaE = 1 And C1$= "LetraE" Or escolaS = 1 And C1$= "LetraS" Or escolaC = 1 And C1$= "LetraC" Or escolaO = 1 And C1$= "LetraO" Or escolaL = 1 And C1$= "LetraL" Or escolaA = 1 And C1$= "LetraA") Then GoTo *Negativa
239         GoSub *Pick
240         Select C1$
241         Case "LetraE"
242         Mov Pcol1, -50
243         Dly 0.5
244         Mvs Pcol1
245         Dly 1
246         HOpen 1
247         Dly 0.5
248         Mvs, -50
249         Dly 1
250         Mescola = Mescola + 1
251         escolaE = escolaE + 1
252         Break
253         '
254         Case "LetraS"
255         Mov Pcol2, -50
256         Dly 0.5
257         Mvs Pcol2
258         Dly 1
259         HOpen 1
260         Dly 0.5
261         Mvs, -50
262         Dly 0.5
263         Mescola = Mescola + 1
264         escolaS = escolaS + 1
265         Break
266         '
267         Case "LetraC"
268         Mov Pcol3, -50
269         Dly 0.5
270         Mvs Pcol3
271         Dly 1
272         HOpen 1
273         Dly 0.5
274         Mvs, -50
275         Dly 0.5
276         Mescola = Mescola + 1
277         escolaC = escolaC + 1
278         Break
279         '
280         Case "LetraO"
281         Mov Pcol4, -50
282         Dly 0.5
283         Mvs Pcol4
284         Dly 1
285         HOpen 1
286         Dly 0.5
287         Mvs, -50
288         Dly 0.5
289         Mescola = Mescola + 1
290         escolaO = escolaO + 1
291         Break
292         '
293         Case "LetraL"
294         Mov Pcol5, -50
295         Dly 0.5
296         Mvs Pcol5
297         Dly 1
298         HOpen 1
299         Dly 0.5
300         Mvs, -50
301         Mescola = Mescola + 1
302         escolaL = escolaL + 1
303         Dly 0.5
304         Break
305         '
306         Case "LetraA"
307         Mov Pcol6, -50
308         Dly 0.5
309         Mvs Pcol6
310         Dly 1
311         HOpen 1
312         Dly 0.5
313         Mvs, -50
314         Dly 0.5
315         Mescola = Mescola + 1
316         escolaA = escolaA + 1
317         Break
318         End Select
319         Dly 0.5
320         Mov P_Safe
321         GoTo *Relectura
322 '
323 'Espacios en "blanco"
324 *ColPNul
325         For m3 = 1 To 3
326             Mov Pnula(m3), -50
327             Dly 0.5
328             Mvs Pnula(m3)
329             Dly 0.5
330             HClose 1
331             Dly 0.5
332             Mov Pnula(m3), -50
333             Mov P_Safe
334             Mov Pblan(m3), -50
335             Dly 0.5
336             Mvs Pblan(m3)
337             Dly 1
338             HOpen 1
339             Dly 0.5
340             Mvs Pblan(m3), -50
341             Mdel = Mdel + 1
342             Mov P_Safe
343         Next
344         Return
345 'Movimiento de recogida en orientación correcta de la pieza
346 *Pick
347     '
348     Mov Ppick, -50
349     Mov Ppick
350     Dly 0.1
351     HClose 1
352     Dly 1
353     Mov Ppick, -50
354     '
355     Mov Pchoque2
356     Mov Porientacion
357     Dly 1
358     HOpen 1
359     Dly 1
360     Mov Pchoque3
361     Dly 0.5
362     Mov Pchoque4
363     Dly 0.5
364     Mov Pcorreccion, -50
365     Mov Pcorreccion
366     Dly 1
367     HClose 1
368     Dly 1
369     '
370     Mov P_Safe
371     Return
372     '
373 'Rechazar de pieza
374 *Negativa
375     Ovrd 90
376     Mov Pnega1
377     For m2 = 1 To 2
378         Mov Pnega2
379         Mov Pnega3
380     Next
381     Ovrd 50
382     Mov Ppick, -50
383     Mov Ppick
384     Dly 0.1
385     HClose 1
386     Dly 1
387     Mov Ppick, -50
388     '
389     Mov Pno, -50
390     Mov Pno
391     Dly 0.1
392     HOpen 1
393     Dly 1
394     Mov Pno, -50
395     Mov P_Safe
396     GoTo *LOOP
397 '
398 'Rutina Relectura pieza (Con tal de que no se lean 2 veces la misma pieza y se haga  un "falso" pick)
399 *Relectura
400     NVRun #1, CProgCAM$
401     EBRead #1,,MNUM,POSLET,C1$
402     If MNUM = 0 GoTo *LOOP
403     If MNUM = 1 GoTo *Relectura
404 'Rutina de Finalización del programa
405 *Casa
406     For m5 = 1 To 5
407         Mov Palegre1
408         Mov Palegre2
409     Next
410     Mov P_Safe
411     End
Palegre1=(256.920,0.000,689.440,0.000,46.090,0.000)(6,0)
Palegre2=(292.930,0.000,631.920,0.000,69.820,0.000)(6,0)
Pchoque1=(361.620,-94.530,31.540,180.000,0.000,180.000)(7,0)
Pchoque2=(375.350,-81.180,99.210,176.110,-82.540,-9.820)(6,15728640)
Pchoque3=(348.980,-78.630,131.990,175.980,-77.560,-10.580)(6,15728640)
Pchoque4=(348.980,-78.630,131.990,-102.420,-2.810,-104.080)(6,0)
Pcol1=(24.640,215.260,310.130,-180.000,0.000,-92.250)(7,0)
Pcol2=(79.420,215.260,310.130,-180.000,0.000,-92.250)(7,0)
Pcol3=(127.740,215.260,310.130,-180.000,0.000,-92.250)(7,0)
Pcol4=(181.640,215.260,310.130,-180.000,0.000,-92.250)(7,0)
Pcol5=(228.270,215.260,310.130,-180.000,0.000,-92.250)(7,0)
Pcol6=(279.000,215.260,310.130,-180.000,0.000,-92.250)(7,0)
Pcol7=(329.210,215.260,310.130,-180.000,0.000,-92.250)(7,0)
Pcorreccion=(371.350,-89.520,26.250,-180.000,0.000,157.650)(7,0)
Pnega1=(322.240,0.000,562.880,-180.000,85.790,-180.000)(7,0)
Pnega2=(322.240,-28.750,562.880,-95.250,36.680,-93.140)(7,0)
Pnega3=(322.240,28.750,562.880,95.340,37.940,91.630)(7,0)
Pnegativa=(361.620,5.000,6.160,180.000,0.000,-180.000)(7,0)
Pno=(361.620,5.000,6.160,180.000,0.000,-180.000)(7,0)
Porientacion=(375.350,-81.180,21.370,176.110,-82.540,-9.820)(6,0)
POSLET=(0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000)(0,0)
Ppick=(361.620,-94.530,6.160,180.000,0.000,-180.000)(7,0)
PREF=(361.620,-94.530,6.160,180.000,0.000,-180.000)(7,0)
Pblan(1)=(177.680,215.260,310.130,180.000,0.000,-92.250)(7,0)
Pblan(2)=(232.670,215.260,310.130,180.000,0.000,-92.250)(7,0)
Pblan(3)=(281.980,215.260,310.130,180.000,0.000,-92.250)(7,0)
Pnula(1)=(-1.070,-334.710,23.000,180.000,0.000,90.000)(7,0)
Pnula(2)=(98.320,-334.710,23.000,180.000,0.960,90.000)(7,0)
Pnula(3)=(194.980,-333.360,23.000,180.000,0.960,90.000)(7,0)
Posll(1)=(279.000,215.260,310.130,180.000,0.000,-92.250,0.000,0.000)(7,0)
Posll(2)=(329.210,215.260,310.130,180.000,0.000,-92.250,0.000,0.000)(7,0)
