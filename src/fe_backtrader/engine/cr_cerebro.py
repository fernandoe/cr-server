def save_cerebro_image(
    cerebro,
    numfigs=1,
    iplot=True,
    start=None,
    end=None,
    width=16,
    height=9,
    dpi=300,
    tight=True,
    use=None,
    file_path="",
    **kwargs
):
    from backtrader import plot

    if cerebro.p.oldsync:
        plotter = plot.Plot_OldSync(**kwargs)
    else:
        plotter = plot.Plot(**kwargs)

    figs = []
    for stratlist in cerebro.runstrats:
        for si, strat in enumerate(stratlist):
            rfig = plotter.plot(
                strat,
                figid=si * 100,
                numfigs=numfigs,
                iplot=iplot,
                start=start,
                end=end,
                use=use,
            )
            figs.append(rfig)

    for fig in figs:
        for f in fig:
            f.savefig(file_path, bbox_inches="tight")
    return figs


#
# saveplots(cerebro, file_path = 'savefig.png') #run it


# class CRCerebro(Cerebro):
#     def plot(
#         self,
#         plotter=None,
#         numfigs=1,
#         iplot=True,
#         start=None,
#         end=None,
#         width=16,
#         height=9,
#         dpi=300,
#         tight=True,
#         use=None,
#         savefig=False,
#         figfilename="backtrader-plot-{j}-{i}.png",
#         **kwargs
#     ):
#         if self._exactbars > 0:
#             return
#
#         if not plotter:
#             from . import plot
#
#             if self.p.oldsync:
#                 plotter = plot.Plot_OldSync(**kwargs)
#             else:
#                 plotter = plot.Plot(**kwargs)
#
#         # pfillers = {self.datas[i]: self._plotfillers[i]
#         # for i, x in enumerate(self._plotfillers)}
#
#         # pfillers2 = {self.datas[i]: self._plotfillers2[i]
#         # for i, x in enumerate(self._plotfillers2)}
#
#         figs = []
#         for stratlist in self.runstrats:
#             for si, strat in enumerate(stratlist):
#                 rfig = plotter.plot(
#                     strat,
#                     figid=si * 100,
#                     numfigs=numfigs,
#                     iplot=iplot,
#                     start=start,
#                     end=end,
#                     use=use,
#                 )
#                 # pfillers=pfillers2)
#
#                 figs.append(rfig)
#
#             plotter.show()
#
#         return figs
